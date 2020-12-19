from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api_v1 import api
import config

db = SQLAlchemy()
migrate = Migrate()

app=Flask(__name__)
app.config.from_object(config)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(api, url_prefix="/api")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)