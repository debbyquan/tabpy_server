import os
import subprocess

if __name__ == "__main__":
    port = os.environ.get("PORT", "8080")

    # Write a config that covers common TabPy 2.x config formats
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
    print("=== tabpy.conf ===")
    print(conf_text)

    subprocess.check_call([
        "/app/.venv/bin/tabpy",
        "--config", "tabpy.conf",
        "--disable-auth-warning",
    ])
