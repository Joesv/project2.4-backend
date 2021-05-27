def register_blueprints(app):
    #from app.server import memory_api
    from app.server import user

    #app.register_blueprint(memory_api)
    app.register_blueprint(user)