import os
import subprocess
from pathlib import Path

if __name__ == "__main__":
    port = os.environ.get("PORT", "8080")

    # Writable location in Railway/Linux
    state_dir = os.environ.get("TABPY_STATE_DIR", "/tmp/tabpy_state")
    Path(state_dir).mkdir(parents=True, exist_ok=True)

    # Config: include BOTH common variants (TabPy has had config changes across versions)
    conf_text = (
        "[Service]\n"
        "host = 0.0.0.0\n"
        f"port = {port}\n"
        "\n"
        "[Server]\n"
        "Host = 0.0.0.0\n"
        f"Port = {port}\n"
        "\n"
        "[TabPy]\n"
        f"state_path = {state_dir}\n"
        "\n"
        "[State]\n"
        f"path = {state_dir}\n"
    )

    with open("tabpy.conf", "w", encoding="utf-8") as f:
        f.write(conf_text)

    print("PORT env:", port)
    print("TABPY_STATE_DIR:", state_dir)
    print("=== tabpy.conf ===")
    print(conf_text)

    # NOTE: no --state-path here (your tabpy CLI doesn't support it)
    subprocess.check_call(
        [
            "/app/.venv/bin/tabpy",
            "--config",
            "tabpy.conf",
            "--disable-auth-warning",
        ]
    )
