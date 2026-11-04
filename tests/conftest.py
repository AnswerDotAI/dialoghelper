import shutil
from pathlib import Path
import pytest_asyncio
from fastcore.nbio import new_nb, mk_cell, write_nb
from jupyasyncclient import JupyAsyncKernelClient
from rustygate.tools import start_gateway


@pytest_asyncio.fixture
async def kernel(tmp_path):
    from test_core import RUN
    shutil.copy(Path(__file__).with_name('test_core.py'), tmp_path)
    write_nb(new_nb([mk_cell(RUN, id='checks')]), tmp_path/'api.ipynb')
    gateway = start_gateway(['rustygate', '--root', str(tmp_path)])
    try:
        client = await JupyAsyncKernelClient.connect(gateway.url, path='api.ipynb')
        try: yield client
        finally: await client.shutdown_kernel()
    finally: gateway.stop()
