import os

if __name__ == "__main__":
    port = os.environ.get("PORT", "9004")
    os.execvp(
        "tabpy-server",
        ["tabpy-server", "--host", "0.0.0.0", "--port", str(port)],
    )
