from flask import Flask
from flask import render_template
from flask_migrate import Migrate
from models import db
from api_v1 import api
import config


migrate = Migrate()

app=Flask(import_name=__name__,
static_url_path="/",
static_folder="/",
template_folder="static/"
)
app.config.from_object(config)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(api, url_prefix="/api")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/manager")
def manager():
    return render_template("manager.html")

if __name__ == "__main__":
    # app.run(host="127.0.0.1" , port=5000 , debug=True)
    app.run(host="0.0.0.0" , port=5000 , debug=True)