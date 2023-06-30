import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def deploy_py():
    """Example Deploy App route."""
    name = os.environ.get("NAME", "App")
    return f"Deploy {name}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
