#!/usr/bin/python3
"""
This is the main Flask application for your API.
"""

import os
from flask import Flask, jsonify
from models import storage
from flask_cors import CORS, cross_origin
from api.v1.views import app_views, host, port, threaded

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(self):
    """Closes the storage on teardown."""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors and return a JSON response."""
    return jsonify({"error": "Not found"}), 404
