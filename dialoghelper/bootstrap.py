"Bootstrap gateway kernels bound to a notebook. Rustygate supplies the stable `RUSTYGATE_KERNEL_ID` and the notebook path in `RUSTYGATE_KERNEL_PATH` on each spawn. Folder-local pyskills bind to the opening cwd before the tool layer loads. When rustygate renames the notebook, it sends a `rustygate.events` comm, and the kernel repoints its cwd, aidialog and dialoghelper's current path; the skill scope stays until restart. Kernels without a notebook binding get only the display patches, not Solveit's tools. IPython reports extension failures and continues booting."

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

prose_types = {'pandas.DataFrame', 'pandas.io.formats.style.Styler', 'polars.dataframe.frame.DataFrame', 'polars.series.series.Series'}

def _is_prose(o): return any(f'{c.__module__}.{c.__qualname__}' in prose_types for c in type(o).__mro__)

def _patch_display():
    "Mark `prose_types` HTML as prose, give display objects reprs showing their content, and stop text displays guessing URLs and filenames"
    from pathlib import PurePath
    from IPython.core.formatters import DisplayFormatter
    from IPython.display import DisplayObject, TextDisplayObject
    from fastcore.basics import patch
    from fastcore.xtras import truncstr

    @patch
    def format(self:DisplayFormatter, obj, include=None, exclude=None):
        data,meta = self._orig_format(obj, include=include, exclude=exclude)
        if 'text/html' in data and _is_prose(obj): meta.setdefault('text/html', {})['prose'] = True
        return data,meta

    @patch
    def __repr__(self:DisplayObject):
        s = self.data or self.url or self.filename
        if s is None: return object.__repr__(self)
        return f"{type(self).__name__}({s if isinstance(s, str) else truncstr(str(s), 30)})"

    # IPython's `DisplayObject.__init__` fetches `data` as a URL when it starts with `http`, and loads it as a file when one of that name exists
    @patch
    def __init__(self:TextDisplayObject, data=None, url=None, filename=None, metadata=None):
        if isinstance(data, PurePath): data = str(data)
        self.url,self.filename,self.data = url,filename,data
        if metadata is not None: self.metadata = metadata
        elif self.metadata is None: self.metadata = {}
        self.reload()
        self._check_data()

def load_ipython_extension(ip):
    "Patch IPython displays; in a notebook-bound kernel, also load Solveit's tools and point aidialog at the current notebook binding"
    _patch_display()
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
