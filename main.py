import os
import subprocess
import sys

if __name__ == "__main__":
    port = os.environ.get("PORT", "9004")

    # Run TabPy's installed console command
    cmd = ["tabpy-server", "--host", "0.0.0.0", "--port", str(port)]

    # Replace this process with tabpy-server
    os.execvp(cmd[0], cmd)
