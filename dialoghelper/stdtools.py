from dialoghelper import *
from fastcore.tools import *
from toolslm.xml import *
from toolslm.inspecttools import *
from pyskills import allow,doc,list_pyskills
from pyskills.edit import *
from safepyrun.core import allow_imports

for o in ('fastllm', 'PIL'): allow_imports.add(o)

