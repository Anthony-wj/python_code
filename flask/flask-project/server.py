from app import create_app

app = create_app()

app.run(debug=app.config.get("DEBUG"), host=app.config.get("HOST"), port=app.config.get("PORT"))
