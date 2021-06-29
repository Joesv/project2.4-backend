from app.routes.user import user
from app.routes.lamp_device import lamp_device
from app.routes.colored_lamp_device import colored_lamp_device
from app.routes.device import device
from app.routes.dummy_device import dummy_device


def register_blueprints(app):
    app.register_blueprint(user)
    app.register_blueprint(lamp_device)
    app.register_blueprint(colored_lamp_device)
    app.register_blueprint(device)
    app.register_blueprint(dummy_device)
