"""Bootstrap a solveit dialog kernel. Kernel config loads this IPython extension everywhere solveit kernels run: the image's `/etc/ipython/ipython_kernel_config.py`, a dev venv's symlink to that file, and CI's copy of it. The dialog name arrives in `__DIALOG_NAME` (spawn environment) and the process starts in the dialog's folder. Folder-local pyskills bind to this opening folder before the tool layer loads. Working-directory changes and dialog moves do not change their scope; restart the kernel to adopt a new folder. Without `__DIALOG_NAME` the extension does nothing, so the config can load it in every kernel of a shared venv. A failure here does not stop the kernel: IPython reports it and boots on, and the broken environment surfaces at first use of the tool layer."""

import os
from pathlib import Path

def repoint(nm):
    "Point this kernel at a gateway-relative dialog filename under its established root"
    from IPython import get_ipython
    from dialoghelper.core import dh_settings
    fname = Path(dh_settings['root'])/nm
    os.chdir(fname.parent)
    get_ipython().ex(f'''import aidialog.dlgskill as dsk, dialoghelper.core as dh
dsk.set_dlg({str(fname)!r}, cls=dh.Dialog)
__dialog_name = {nm!r}''')

def load_ipython_extension(ip):
    "Populate the kernel namespace for the dialog named by `__DIALOG_NAME`; quiet no-op without it"
    nm = os.environ.get('__DIALOG_NAME')
    if not nm: return
    from pyskills import enable_local_skills
    enable_local_skills(Path.cwd())
    from dialoghelper.core import dh_settings
    root = Path.cwd()
    for _ in Path(nm).parent.parts: root = root.parent
    dh_settings['root'] = str(root)
    ip.ex('''from dialoghelper.stdtools import *
py = RunPython()''')
    repoint(nm)
