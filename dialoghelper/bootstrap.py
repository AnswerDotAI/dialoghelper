"Bootstrap gateway kernels bound to a notebook. Rustygate supplies the stable `RUSTYGATE_KERNEL_ID` and the notebook path in `RUSTYGATE_KERNEL_PATH` on each spawn. Folder-local pyskills bind to the opening cwd before the tool layer loads. When rustygate renames the notebook, it sends a `rustygate.events` comm, and the kernel repoints its cwd, aidialog and dialoghelper's current path; the skill scope stays until restart. Kernels without a notebook binding are left unchanged. IPython reports extension failures and continues booting."

import os
from pathlib import Path

def repoint(nm):
    "Point this kernel at a gateway-relative dialog filename under its established root"
    from IPython import get_ipython
    from dialoghelper.core import dh_settings
    dh_settings['path'] = nm
    fname = Path(dh_settings['root'])/nm
    os.chdir(fname.parent)
    get_ipython().ex(f'''import aidialog.dlgskill as dsk, dialoghelper.core as dh
dsk.set_dlg({str(fname)!r})''')

def _on_event(comm, msg):
    "Repoint the kernel when rustygate's `rustygate.events` comm reports that its notebook was renamed"
    data = msg['content']['data']
    if data.get('event')=='rename': repoint(data['path'])

def load_ipython_extension(ip):
    "Load Solveit's tools and bind aidialog to the notebook."
    if not os.environ.get('RUSTYGATE_KERNEL_PATH'): return
    nm = os.environ['RUSTYGATE_KERNEL_PATH']
    from pyskills import enable_local_skills
    enable_local_skills(Path.cwd())
    from dialoghelper.core import dh_settings
    root = Path.cwd()
    for _ in Path(nm).parent.parts: root = root.parent
    dh_settings['root'] = str(root)
    ip.ex('from dialoghelper.stdtools import *')
    from comm import get_comm_manager
    get_comm_manager().register_target('rustygate.events', _on_event)
    repoint(nm)
