import os
import subprocess
from pathlib import Path

if __name__ == "__main__":
    port = os.environ.get("PORT", "8080")

    # Use a writable, POSIX-friendly state path on Railway/Linux
    state_path = os.environ.get("TABPY_STATE_PATH", "/tmp/tabpy_state")
    Path(state_path).mkdir(parents=True, exist_ok=True)

    conf_text = (
        "[Service]\n"
        "host = 0.0.0.0\n"
        f"port = {port}\n"
        "\n"
        "[Server]\n"
        "Host = 0.0.0.0\n"
        f"Port = {port}\n"
    )

    with open("tabpy.conf", "w", encoding="utf-8") as f:
        f.write(conf_text)

    print("PORT env:", port)
    print("TABPY_STATE_PATH:", state_path)
    print("=== tabpy.conf ===")
    print(conf_text)

    subprocess.check_call(
        [
            "/app/.venv/bin/tabpy",
            "--config",
            "tabpy.conf",
            "--disable-auth-warning",
            "--state-path",
            state_path,
        ]
    )
