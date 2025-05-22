import sys
import os

# Add the project root directory (TodoApp) to the Python path.
# os.path.dirname(__file__) gets the directory of this conftest.py file (TodoApp/test).
# os.path.join(..., '..') goes one level up to the TodoApp directory.
# os.path.abspath() ensures it's an absolute path.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))