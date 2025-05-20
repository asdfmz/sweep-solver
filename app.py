import os
from flask import Flask
from routes.init_matrix import bp as init_matrix_bp
from routes.interactive import bp as interactive_bp
from routes.main import bp as main_bp

app = Flask(__name__)
app.secret_key = "a-secure-key"

app.register_blueprint(main_bp)  # handles "/"
app.register_blueprint(init_matrix_bp, url_prefix="/init")
app.register_blueprint(interactive_bp, url_prefix="/solve")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
