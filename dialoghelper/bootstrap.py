"Bootstrap gateway kernels bound to a notebook. Folder-local pyskills bind to the opening cwd before the tool layer loads. Kernels without a notebook binding get only the display patches, not Solveit's tools. IPython reports extension failures and continues booting."

import os
from pathlib import Path
from IPython.core.formatters import DisplayFormatter
from fastcore.basics import patch

prose_types = {'pandas.DataFrame', 'pandas.io.formats.style.Styler', 'polars.dataframe.frame.DataFrame', 'polars.series.series.Series'}

def _is_prose(o): return any(f'{c.__module__}.{c.__qualname__}' in prose_types for c in type(o).__mro__)


def load_ipython_extension(ip):
    "Enable display patches; for notebook-bound kernels, also load Solveit's tools"
    import ipymini.term.display  # chkstyle: ignore
    _previous_format = DisplayFormatter.format

    @patch
    def format(self:DisplayFormatter, obj, include=None, exclude=None):
        data,meta = _previous_format(self, obj, include=include, exclude=exclude)
        if 'text/html' in data and _is_prose(obj): meta.setdefault('text/html', {})['prose'] = True
        return data,meta

    if not os.environ.get('JUPYGATE_KERNEL_PATH'): return
    from pyskills import enable_local_skills
    enable_local_skills(Path.cwd())
    ip.ex('from dialoghelper.stdtools import *')
