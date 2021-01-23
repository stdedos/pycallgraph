#!/usr/bin/env python
"""
Execute all pycallgraph examples in this directory.
"""
import subprocess
from pathlib import Path

current_path = Path(__file__).parent  # Get the directory of the current file
all_py_files = list(current_path.glob("*.py"))
examples = [ex for ex in all_py_files if ex.stem != "all"]

for example in examples:
    print(f"Running {example} ...")
    subprocess.call(f"python {example}", shell=True)
