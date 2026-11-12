"Everything `from dialoghelper.stdtools import *` provides, by module."
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

def _provided():
    "Module -> names this file imports from it, read from its own import statements"
    import ast, sys
    res = {}
    for o in ast.parse(open(__file__).read()).body:
        if isinstance(o, ast.ImportFrom): res[o.module] = xdir(sys.modules[o.module]) if o.names[0].name=='*' else [a.name for a in o.names]
        elif isinstance(o, ast.Import): res.update({a.name: [a.asname] for a in o.names})
    return res

provided = _provided()
__doc__ += '\n\n' + '\n'.join(f"- `{m}`: {', '.join(f'`{n}`' for n in ns)}" for m,ns in provided.items())

