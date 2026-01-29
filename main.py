"""
This is the main file of the Flask application.
It registers the file_explorer blueprint and starts the server.
"""

from flask import Flask
from flask_file_explorer.file_explorer import file_explorer_bp
from flask_file_explorer.filters import register_filters

app = Flask(__name__)
app.config["FFE_BASE_DIRECTORY"] = "flask_file_explorer/static"
app.register_blueprint(file_explorer_bp, url_prefix="/file-explorer")
register_filters(app)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
