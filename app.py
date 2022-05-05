from flask import Flask, abort


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def home():
        abort(404)

    @app.errorhandler(404)
    def custom404(error: Exception):
        return "Your computer has virus"

    return app


if __name__ == "__main__":
    create_app().run()