from flasgger import Swagger

SWAGGER_CONFIG = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
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
    }
}

TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "API Gateway",
        "description": "API Gateway Documentation",
        "version": "1.0"
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