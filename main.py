import os
import subprocess

if __name__ == "__main__":
    port = os.environ.get("PORT", "8080")

    conf_text = (
        "[TabPy]\n"
        "StateFilePath = tabpy_state.pkl\n"
        "LogFilePath = tabpy.log\n"
        "\n"
        "[Server]\n"
        "Host = 0.0.0.0\n"
        f"Port = {port}\n"
    )

    with open("tabpy.conf", "w", encoding="utf-8") as f:
        f.write(conf_text)

    # Start TabPy using its supported CLI
    subprocess.check_call([
        "/app/.venv/bin/tabpy",
        "--config", "tabpy.conf",
        "--disable-auth-warning",
    ])
