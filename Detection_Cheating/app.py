from flask import Flask
# from api_v1 import api


app=Flask(__name__)
# app.config.from_object(config)

app.register_blueprint(api, url_prefix="/api")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)