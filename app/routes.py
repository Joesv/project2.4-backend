def register_blueprints(app):
    #from app.server import memory_api
    from app.server import user
    from app.server import device

    #app.register_blueprint(memory_api)
    app.register_blueprint(user)
    app.register_blueprint(device)

