from app.routes.user import user
from app.routes.lamp_device import lamp_device
from app.routes.device import device


def register_blueprints(app):
    app.register_blueprint(user)
    app.register_blueprint(lamp_device)
    app.register_blueprint(device)
