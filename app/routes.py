def register_blueprints(app):
    from app.server import user
    from app.server import lamp_device
    from app.server import device

    app.register_blueprint(user)
    app.register_blueprint(lamp_device)
    app.register_blueprint(device)

