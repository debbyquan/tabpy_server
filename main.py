import os
import sys
import glob
import subprocess

def debug():
    print("Python:", sys.executable)
    print("PORT:", os.environ.get("PORT"))
    print("PATH:", os.environ.get("PATH", ""))
    print("cwd:", os.getcwd())

    # Show what executables exist in the venv bin directory (Railway commonly uses /app/.venv)
    for p in ["/app/.venv/bin", os.path.join(os.path.dirname(sys.executable), "")]:
        print("Checking:", p)
        try:
            print("  bin contents sample:", sorted(os.listdir(p))[:50])
        except Exception as e:
            print("  cannot list:", e)

    # Find any tabpy-related executables
    print("tabpy executables:", glob.glob("/app/.venv/bin/*tabpy*"))

def main():
    port = os.environ.get("PORT", "9004")

    # Most common location on Railway python deployments:
    candidates = [
        "/app/.venv/bin/tabpy-server",
        "/app/.venv/bin/tabpy",
    ]

    for exe in candidates:
        if os.path.exists(exe):
            # tabpy-server preferred
            if exe.endswith("tabpy-server"):
                cmd = [exe, "--host", "0.0.0.0", "--port", str(port)]
            else:
                # Some installs provide `tabpy` CLI with a `server` subcommand
                cmd = [exe, "server", "--host", "0.0.0.0", "--port", str(port)]

            print("Starting:", " ".join(cmd))
            os.execv(cmd[0], cmd)

    # If we got here, nothing was found
    print("ERROR: Could not find tabpy-server or tabpy CLI in /app/.venv/bin")
    debug()
    sys.exit(1)

if __name__ == "__main__":
    main()
