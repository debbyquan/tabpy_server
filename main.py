import os
from tabpy.tabpy_server.app.app import main as tabpy_main

def run():
    port = int(os.environ.get("PORT", "9004"))

    # Paths where Railway will have your TLS cert/key (you must provide these)
    cert_file = os.environ.get("TABPY_CERT_FILE", "/app/certs/fullchain.pem")
    key_file  = os.environ.get("TABPY_KEY_FILE",  "/app/certs/privkey.pem")

    config_text = f"""
[TabPy]
TABPY_PORT = {port}
TABPY_TRANSFER_PROTOCOL = https
TABPY_CERTIFICATE_FILE = {cert_file}
TABPY_KEY_FILE = {key_file}

# Optional but common in hosted environments:
TABPY_STATE_PATH = /tmp/tabpy_state
TABPY_QUERY_OBJECT_PATH = /tmp/query_objects
"""

    cfg_path = "/tmp/tabpy.conf"
    with open(cfg_path, "w", encoding="utf-8") as f:
        f.write(config_text)

    # Start TabPy (blocks)
    tabpy_main(["--config", cfg_path])

if __name__ == "__main__":
    run()
