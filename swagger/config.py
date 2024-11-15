from flasgger import Swagger
from .config import SWAGGER_CONFIG, TEMPLATE

SWAGGER_CONFIG = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "title": "API Gateway Documentation",
    "version": "1.0.0",
    "description": "API Gateway service with authentication and GitHub statistics",
    "termsOfService": "",
    "uiversion": 3,
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT token in format: Bearer <token>"
        }
    },
    "security": [
        {"Bearer": []}
    ]
}

TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "API Gateway",
        "description": "API Gateway service endpoints",
        "version": "1.0.0"
    },
    "consumes": [
        "application/json",
    ],
    "produces": [
        "application/json"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    }
}

def init_swagger(app):
    """Initialize Swagger with the Flask application"""
    swagger = Swagger(
        app,
        config=SWAGGER_CONFIG,
        template=TEMPLATE
    )
    return swagger