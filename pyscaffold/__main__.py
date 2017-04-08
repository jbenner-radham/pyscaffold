from pathlib import Path
import os.path

dir = '__scaffold__'
files = ['MANIFEST.in', 'README.rst', 'setup.cfg', 'setup.py']

print(f'Hello world! Scaffolding out to {dir}.')
Path(dir).mkdir(exist_ok=True)

for file in files:
    filepath = os.path.join(dir, file)
    Path(filepath).touch()
