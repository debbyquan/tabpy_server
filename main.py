import os
import subprocess
from pathlib import Path

if __name__ == "__main__":
    port = os.environ.get("PORT")
    if not port:
        # local fallback only
        port = "8080"

    state_dir = os.environ.get("TABPY_STATE_DIR", "/tmp/tabpy_state")
    Path(state_dir).mkdir(parents=True, exist_ok=True)

    state_file = str(Path(state_dir) / "tabpy_state.pkl")
    log_file = str(Path(state_dir) / "tabpy.log")

    conf_text = (
        "[TabPy]\n"
        f"StateFilePath = {state_file}\n"
        f"LogFilePath = {log_file}\n"
        "\n"
        "[Server]\n"
        "Host = 0.0.0.0\n"
        f"Port = {port}\n"
    )

    with open("tabpy.conf", "w", encoding="utf-8") as f:
        f.write(conf_text)

    print("PORT env:", port)
    print("TABPY_STATE_DIR:", state_dir)
    print("=== tabpy.conf ===")
    print(conf_text)

    subprocess.check_call(
        ["/app/.venv/bin/tabpy", "--config", "tabpy.conf", "--disable-auth-warning"]
    )
