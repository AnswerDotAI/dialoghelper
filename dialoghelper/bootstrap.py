"""Bootstrap kernels marked `SOLVEIT_KERNEL`. Rustygate supplies the stable `RUSTYGATE_KERNEL_ID` and the current binding in `RUSTYGATE_KERNEL_PATH` on each spawn. Folder-local pyskills bind to the opening cwd before the tool layer loads; rename repoints cwd and aidialog without changing that skill scope until restart. Unmarked kernels do not load Solveit's tools. IPython reports extension failures and continues booting."""

import os
from pathlib import Path

def repoint(nm):
    "Point this kernel at a gateway-relative dialog filename under its established root"
    from IPython import get_ipython
    from dialoghelper.core import dh_settings
    fname = Path(dh_settings['root'])/nm
    os.chdir(fname.parent)
    get_ipython().ex(f'''import aidialog.dlgskill as dsk, dialoghelper.core as dh
dsk.set_dlg({str(fname)!r}, cls=dh.Dialog)''')

def load_ipython_extension(ip):
    "Load Solveit's tools and point aidialog at the current notebook binding"
    if not os.environ.get('SOLVEIT_KERNEL'): return
    nm = os.environ['RUSTYGATE_KERNEL_PATH']
    from pyskills import enable_local_skills
    enable_local_skills(Path.cwd())
    from dialoghelper.core import dh_settings
    root = Path.cwd()
    for _ in Path(nm).parent.parts: root = root.parent
    dh_settings['root'] = str(root)
    ip.ex('''from dialoghelper.stdtools import *
py = RunPython()''')
    repoint(nm)
