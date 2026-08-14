"""Bootstrap a solveit dialog kernel. Kernel config loads this IPython extension everywhere solveit kernels run: the image's `/etc/ipython/ipython_kernel_config.py`, a dev venv's symlink to that file, and CI's copy of it. The dialog name arrives in `__DIALOG_NAME` (spawn environment) and the process starts in the dialog's folder. Without `__DIALOG_NAME` the extension does nothing, so the config can load it in every kernel of a shared venv. A failure here does not stop the kernel: IPython reports it and boots on, and the broken environment surfaces at first use of the tool layer."""

import os
from pathlib import Path

def repoint(nm, folder=None):
    "Point this kernel at dialog `nm` in `folder` (default cwd): working directory, kernel-side names, and dsk's current dialog"
    from IPython import get_ipython
    folder = Path(folder) if folder else Path.cwd()
    os.chdir(folder)
    root = folder
    for _ in Path(nm).parent.parts: root = root.parent
    from dialoghelper.core import dh_settings
    dh_settings['root'] = str(root)
    fname = folder/f'{Path(nm).name}.ipynb'
    get_ipython().ex(f'''import aidialog.dlgskill as dsk, dialoghelper.core as dh
dsk.set_dlg({str(fname)!r}, cls=dh.Dialog)
__dialog_name = {nm!r}''')

def load_ipython_extension(ip):
    "Populate the kernel namespace for the dialog named by `__DIALOG_NAME`; quiet no-op without it"
    nm = os.environ.get('__DIALOG_NAME')
    if not nm: return
    ip.ex('''from dialoghelper.stdtools import *
py = RunPython()''')
    repoint(nm)
