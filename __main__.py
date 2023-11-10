

from __init__ import create_app



APP_CONFIG = {
    "hostname": "localhost",
    "port": 5500,
    "use_reloader":True,
    "use_debugger":True,
}

if __name__ == "__main__":
    app =create_app()
    app.run(**APP_CONFIG)