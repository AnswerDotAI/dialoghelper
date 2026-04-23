"""Read and edit Solveit dialog (or Jupyter) .ipynb files from a CLI / script. Solveit is a notebook application (like Jupyter with AI integration) where each notebook is called a "dialog" and is stored as an `.ipynb` file containing `code`, `note` (markdown), and `prompt` (markdown with a special delimiter) messages (aka "cells"). The `dialoghelper` package provides tools for reading, searching, adding, updating, and deleting those messages.

dialoghelper's tools can run *inside* a Solveit kernel where the active dialog is auto-detected; however this pyskill explains how to drive the same tools from *outside* a Solveit kernel — e.g. from a terminal tool such as an AI coding system. Whilst it's possible to use direct ipynb editing tools (such as pyskills.edit's functions), these won't cause open dialogs to dynamically update. Also reading and updating prompt message format is directly supported in dialoghelper. Therefore it's preferred to use dialoghelper.

All dialoghelper.termskill functions are usable from a pyrun sandbox.

## Requirements

- The dialog file must exist on disk under Solveit's data directory. Dialog names are paths *relative to that data root*, with no `.ipynb` suffix (e.g. `/aai-ws/dialoghelper/nbs/00_core`).
- The dialog does NOT need to be open in a browser for most operations. Closed dialogs are updated on disk; open ones additionally receive live DOM updates.

## Specifying the active dialog

From a terminal you must supply the dialog name through either of these approaches:

1. **Per-call absolute `dname`** — pass `dname='/aai-ws/.../dialogname'` (leading `/`, no `.ipynb`) to every tool call. Resolved relative to the Solveit data root, not the filesystem.
2. **Pin once** — `set_dialog('/aai-ws/.../dialogname')`. Subsequent calls default to this. Relative `dname` values in later calls are then resolved relative to this pinned dialog's folder.

All dialog tools are `async`, so `await` them.

## Example

    from dialoghelper.termskill import view_dlg, msg_str_replace

    dname = '/aai-ws/dialoghelper/nbs/00_core'
    print(await view_dlg(nums=True))
    await msg_str_replace(id='_abc123', old_str='foo', new_str='bar')
"""

from dialoghelper.core import *

__all__ = ['set_dialog', 'curr_dialog', 'msg_idx', 'read_msg', 'read_msgid', 'view_msg', 'view_dlg', 'find_msgs',
    'add_msg', 'update_msg', 'del_msg', 'msg_str_replace', 'msg_strs_replace', 'msg_replace_lines', 'msg_insert_line',
    'msg_del_lines', 'msg_ast_replace', 'msg_pyrun', 'create_or_run_dialog', 'stop_dialog', 'realpath', 'list_dialogs']

def set_dialog(dname:str):
    "Set active dialog path for subsequent calls (absolute, no `.ipynb`)"
    dh_settings['dname'] = dname.removeprefix('/').removesuffix('.ipynb')
    return dh_settings['dname']
