"""Experimental `dialoghelper` capabilities."""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_experimental.ipynb.

# %% auto 0
__all__ = ['iife', 'start_screen_share', 'stop_screen_share', 'capture_screen']

# %% ../nbs/01_experimental.ipynb
from importlib import resources
import uuid
from fasthtml.common import Div, Script
from time import sleep
import base64
import json
import time
from claudette import ToolResult
from .core import *
from dataclasses import dataclass
from httpx import get as xget, post as xpost

# %% ../nbs/01_experimental.ipynb
def _wait_for_pop_data(data_id, timeout=20, retry_interval=1, condition=None):
    "Wait for data from pop endpoint with optional condition validation."
    max_attempts = int(timeout / retry_interval)
    for attempt in range(max_attempts):
        result = xpost('http://localhost:5001/pop_data_', data={'data_id': data_id})
        if result.status_code == 200 and result.text.strip():
            try:
                data = result.json()
                if condition and not condition(data):
                    time.sleep(retry_interval)
                    continue
                return data
            except json.JSONDecodeError: pass
        time.sleep(retry_interval)
    return None

# %% ../nbs/01_experimental.ipynb
_js_loaded = False

def _load_screenshot_js(timeout=10, retry_interval=1):
    "Load screenshot capability and wait for confirmation it's ready."
    global _js_loaded
    if _js_loaded: return True    
    js_content = (resources.files('dialoghelper') / 'screenshot.js').read_text()
    ready_id = str(uuid.uuid4())
    js_with_ready = js_content + f'\n\n// Signal ready\nsendDataToServer("{ready_id}", {{"js_status": "ready"}});'
    add_html(Div(Script(js_with_ready), hx_swap_oob='beforeend:#js-script'))
    print("Loading screenshot.js ...")    
    data = _wait_for_pop_data(ready_id, timeout, retry_interval, condition=lambda d: d.get('js_status') == 'ready')
    if data and data.get('js_status') == 'ready':
        _js_loaded = True
        print("Screenshot.js loaded and ready")
        return True
    else:
        print("Failed to load screenshot.js")
        return False

# %% ../nbs/01_experimental.ipynb
def iife(code: str) -> str:
    "Wrap javascript code string in an IIFE"
    return f'''
(async () => {{
{code}
}})();
'''

# %% ../nbs/01_experimental.ipynb
_screen_share_active = False

def start_screen_share(timeout=30, retry_interval=1):
    "Start persistent screen sharing session, waiting for confirmation."
    global _screen_share_active
    _load_screenshot_js()
    status_id = str(uuid.uuid4())
    trigger_script = iife(f'startPersistentScreenShare("{status_id}");')
    add_html(Div(Script(trigger_script), hx_swap_oob=f'beforeend:#js-script'))
    print("Requesting screen share permission ...")
    data = _wait_for_pop_data(status_id, timeout, retry_interval, condition=lambda d: d.get('js_status') == 'ready')
    if not data: print(f"Screen share timed out after {timeout} seconds.")
    js_status = data.get('js_status')
    if js_status == 'ready':
        _screen_share_active = True
        print("Screen share started successfully.")
    elif js_status == 'error': print(f"Screen share failed: {data.get('error', 'Unknown error')}")
    elif js_status == 'connecting': print("Screen share timed out after {timeout} seconds.")

# %% ../nbs/01_experimental.ipynb
def stop_screen_share():
  "Stop persistent screen sharing session."
  global _screen_share_active
  _load_screenshot_js()
  trigger_script = iife('stopPersistentScreenShare();')
  add_html(Div(Script(trigger_script), hx_swap_oob=f'beforeend:#js-script'))
  _screen_share_active = False
  print("Screen share stopped.")

# %% ../nbs/01_experimental.ipynb
def capture_screen():
    "Capture screenshot, automatically starting screen share if needed."
    global _screen_share_active
    _load_screenshot_js()
    if not _screen_share_active:
        print("🔄 No active screen share, starting one...")
        result = start_screen_share()
        if not _screen_share_active: return f"Failed to start screen share: {result}"
    data_id = str(uuid.uuid4())
    screenshot_code = f'captureScreenFromStream("{data_id}");'
    print("📸 Capturing from persistent stream...")
    trigger_script = iife(screenshot_code)
    add_html(Div(Script(trigger_script), hx_swap_oob=f'beforeend:#js-script'))
    data = _wait_for_pop_data(data_id, timeout=10, retry_interval=1, condition=lambda d: 'img_data' in d and 'img_type' in d)
    if not data: return "Screenshot capture timed out"
    if 'error' in data: return f"Screenshot failed: {data['error']}"
    return ToolResult(data=data['img_data'], result_type=data['img_type'])
