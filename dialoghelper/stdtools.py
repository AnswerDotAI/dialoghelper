from dialoghelper import *
from dialoghelper.solveitskill import *
from ipykernel_helper import *
from fastcore.tools import *
from toolslm.xml import *
from toolslm.inspecttools import *
from pyskills import allow,doc,list_pyskills
from pyskills.edit import *
from pyskills.files import *
from exhash.skill import *
from safepyrun.core import allow_imports
from safecmd import bash
from safepyrun import RunPython

for o in ('fastllm', 'PIL', 'fastspec'): allow_imports.add(o)
from exhash import lnhashview_file,exhash_file
allow(lnhashview_file, exhash_file)

