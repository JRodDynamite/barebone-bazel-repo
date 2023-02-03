import sys
print(sys.version)
for path in sys.path:
    print(path)

# 2 ways to import
# 1. complete project path (no additional changes needed in code)
from backend.utils.src.utils.logging import log

# 2. Need to add imports parameter in BUILD and extend_path in library's __init__ file
from utils.logging import log

import requests