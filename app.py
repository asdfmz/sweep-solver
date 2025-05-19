from flask import Flask
from routes.interactive import bp as interactive_bp
import os

app = Flask(__name__)
app.secret_key = "a-secure-key"
app.register_blueprint(interactive_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
