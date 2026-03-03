import os
import subprocess

port = int(os.environ.get('PORT', 9004))
print(f"Starting TabPy on port {port}")

subprocess.run(['python', '-m', 'tabpy', '--port', str(port)])
