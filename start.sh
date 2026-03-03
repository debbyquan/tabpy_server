import os
from tabpy.tabpy_server.app.app import app  # Flask app used by TabPy

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "9004"))
    # Railway needs 0.0.0.0 so it is reachable from the internet
    app.run(host="0.0.0.0", port=port)
