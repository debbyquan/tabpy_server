import os
import subprocess
import sys

if __name__ == "__main__":
    port = os.environ.get("PORT", "9004")

    # Start TabPy listening on Railway's assigned port
    cmd = [
        sys.executable, "-m", "tabpy",
        "--host", "0.0.0.0",
        "--port", str(port),
    ]

    # Replace current process with TabPy (cleaner for containers)
    os.execvp(cmd[0], cmd)
