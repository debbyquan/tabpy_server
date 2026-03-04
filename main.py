import os
import subprocess
import textwrap

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))

    conf_text = textwrap.dedent(f"""
    [TabPy]
    StateFilePath = tabpy_state.pkl
    LogFilePath = tabpy.log

    [Server]
    Host = 0.0.0.0
    Port = {port}
    """كتور).strip() + "\n"

    with open("tabpy.conf", "w", encoding="utf-8") as f:
        f.write(conf_text)

    # Start TabPy using its supported CLI
    subprocess.check_call(["/app/.venv/bin/tabpy", "--config", "tabpy.conf", "--disable-auth-warning"])
