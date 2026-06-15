from dialoghelper import *
from fastcore.tools import *
from toolslm.xml import *
from toolslm.inspecttools import *
from pyskills import allow,doc,list_pyskills,xdir
from pyskills.edit import *
from safepyrun.core import allow_imports
from safecmd import bash
from safepyrun import RunPython

for o in ('fastllm', 'PIL', 'fastspec'): allow_imports.add(o)
from exhash import lnhashview_file,exhash_file
allow(lnhashview_file, exhash_file)

