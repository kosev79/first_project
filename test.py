import os
import sys

python_path = os.path.dirname(sys.executable)

python_version = sys.version

print(f"путь к интерпретатору {python_path},\n версия {python_version} ")

