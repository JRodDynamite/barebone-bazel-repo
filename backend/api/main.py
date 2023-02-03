import sys
print(sys.version)
for path in sys.path:
    print(path)

from backend.utils.src.utils.logging import log
from utils.logging import log

import requests