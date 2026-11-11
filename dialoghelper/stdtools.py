"Everything `from dialoghelper.stdtools import *` provides, by defining module."
from dialoghelper import *
from dialoghelper.solveitskill import *
from fastcore.tools import *
from fastcore.funccall import call_func_async
from toolslm.inspecttools import *
from pyskills import *
from rgapi import *
from exhash.skill import *
from safepyrun.core import allow_imports
from safecmd import bash
from safepyrun import RunPython
import aidialog.dlgskill as dsk

allow_imports.update(['PIL'])

def _doc_rows():
    "One row per module: the public names here that it defines"
    import types
    groups = {}
    for nm,o in list(globals().items()):
        if nm.startswith('_'): continue
        if isinstance(o, types.ModuleType):
            if o.__name__.rsplit('.', 1)[-1] == nm: continue
            src = o.__name__
        else: src = getattr(o, '__module__', None)
        if not src or src == 'builtins': src = 'other'
        groups.setdefault(src, []).append(nm)
    return [f"- `{src}`: " + ', '.join(f'`{nm}`' for nm in nms) for src,nms in sorted(groups.items())]

__doc__ += '\n\n' + '\n'.join(_doc_rows())

