"""Module to run FastAPI using Gunicorn"""

# Default/External Libraries
from gunicorn.app.base import BaseApplication


class GunicornFastAPIApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornFastAPIApplication, self).__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application