"Bootstrap gateway kernels bound to a notebook. Rustygate supplies the stable `RUSTYGATE_KERNEL_ID` and the notebook path in `RUSTYGATE_KERNEL_PATH` on each spawn. Folder-local pyskills bind to the opening cwd before the tool layer loads. When rustygate renames the notebook, it sends a `rustygate.events` comm, and the kernel repoints its cwd, aidialog and dialoghelper's current path; the skill scope stays until restart. Kernels without a notebook binding get only the display patches, not Solveit's tools. IPython reports extension failures and continues booting."

import os
from pathlib import Path
from IPython.core.formatters import DisplayFormatter
from fastcore.basics import patch

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

prose_types = {'pandas.DataFrame', 'pandas.io.formats.style.Styler', 'polars.dataframe.frame.DataFrame', 'polars.series.series.Series'}

def _is_prose(o): return any(f'{c.__module__}.{c.__qualname__}' in prose_types for c in type(o).__mro__)


def load_ipython_extension(ip):
    "Enable display patches; for notebook-bound kernels, also load Solveit's tools and set the notebook binding"
    import ipymini.term.display  # chkstyle: ignore
    _previous_format = DisplayFormatter.format

    @patch
    def format(self:DisplayFormatter, obj, include=None, exclude=None):
        data,meta = _previous_format(self, obj, include=include, exclude=exclude)
        if 'text/html' in data and _is_prose(obj): meta.setdefault('text/html', {})['prose'] = True
        return data,meta

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
