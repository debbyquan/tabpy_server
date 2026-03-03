import os, subprocess, threading

def start_tabpy():
    port = os.environ.get("PORT", "9004")
    subprocess.check_call(["tabpy", "--host", "0.0.0.0", "--port", str(port)])

threading.Thread(target=start_tabpy, daemon=True).start()

def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [b"TabPy process launched.\n"]
