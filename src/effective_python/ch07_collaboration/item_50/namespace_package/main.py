from analysis.utils import log_base2_bucket
from frontend.utils import stringify
# from analysis.utils import inspect
# from frontend.utils import inspect  # 덮어씀!
from analysis.utils import inspect as analysis_inspect
from frontend.utils import inspect as frontend_inspect


bucket = stringify(log_base2_bucket(33))

value = 33
if analysis_inspect(value) == frontend_inspect(value):
    print('Inspection equal!')
