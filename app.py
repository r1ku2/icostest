from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.getenv("TARGET", "World")
    return f"Hello from Code Engine, {name}!\n"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
