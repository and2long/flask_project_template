import os

from flask import Flask, request
from flask_migrate import Migrate

from src.models import db
from src.routes.user import user_routes

app = Flask(__name__)
app.config.from_pyfile('../instance/config.py')
db.init_app(app)
migrate = Migrate(app, db)


@app.before_request
def verify_api_key():
    """验证所有请求的 API Key
    """
    # 跳过 OPTIONS 请求的验证
    if request.method == 'OPTIONS':
        return None

    # 从请求头获取 API Key
    api_key = request.headers.get('X-API-Key')
    if not api_key:
        return {"error": "No API key provided"}, 401

    # 验证 API Key
    expected_api_key = os.getenv('API_KEY')
    if not expected_api_key:
        return {"error": "Server configuration error: API_KEY not set"}, 500

    if api_key != expected_api_key:
        return {"error": "Invalid API key"}, 401


app.register_blueprint(user_routes, url_prefix='/users')
