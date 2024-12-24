# copied from: https://github.com/navdeep-G/samplemod/blob/master/tests/context.py


import sys
from pathlib import Path

# Add the root directory to sys.path
root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(root_path))

