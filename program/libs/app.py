"""FastAPI API and Static Front-End Files"""

import openai
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .api import router as api_router

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="program/libs/static"),
    name="static",
)

@app.get("/", response_class=FileResponse)
async def index():

    return FileResponse("program/libs/static/html/index.html")

def main(
    openai_api_key: str,
    using_gunicorn: bool,
    wsgi_workers: int,
    port: int,
    ):
    """Run the main program."""

    openai.api_key  = openai_api_key

    app.include_router(api_router)
    
    if using_gunicorn:
        # Imported here due to Windows missing 'fcntl' library
        from .fast_gunicorn import GunicornFastAPIApplication

        GunicornFastAPIApplication(
            app,
            {
                "bind": f"0.0.0.0:{port}",
                "workers": 1,
                "worker_class": "uvicorn.workers.UvicornWorker",
            },
        ).run()
    else:
        print("Running uvicorn")
        import uvicorn
        uvicorn.run(
            "libs.app:app",
            host="0.0.0.0",
            port=port,
            log_level="info",
            workers=wsgi_workers,
            app_dir="/program/libs/",
        )