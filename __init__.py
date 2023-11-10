import os

from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.utils import redirect
from wsgi_app import  render_template, request, wsgi
from werkzeug.wrappers import Response
import conexion
def create_app(with_static=True):
    new_app = wsgi()

    if with_static:
        new_app.app = SharedDataMiddleware(
            new_app.app,
            {"/static": os.path.join(os.path.dirname(__file__), "static")},
        )

    @new_app.route(["/", "/home"])
    def home_page():
        return Response(**render_template("home.html", msg="bruno se la come"))

    new_app.register_blueprint(conexion.bp)

    return new_app
