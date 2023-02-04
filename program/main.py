
from typing import Optional
import typer

from libs.app import main as app_main

def main(
        openai_api_key: str = typer.Option(
            ...,
            envvar="OPENAI_API_KEY",
            help="OpenAI API key.",
        ),
        using_gunicorn: Optional[bool] = typer.Option(
            True,
            "--gunicorn/--uvicorn",
            envvar="USING_GUNICORN",
            help="Enable use of Gunicorn or Uvicorn for FastAPI WSGI server.",
        ),
        wsgi_workers: Optional[int] = typer.Option(
            1,
            envvar="WSGI_WORKERS",
            help="Number of Gunicorn/Uvicorn WSGI worker processes.",
        ),
        port: Optional[int] = typer.Option(
            5000,
            envvar="PORT",
            help="Port for FastAPI.",
        ),
    ):
    """Run the main program."""

    app_main(
        openai_api_key,
        using_gunicorn,
        wsgi_workers,
        port,
    )
    
typer_app = typer.Typer()
typer_app.command()(main)


if __name__ == "__main__":
    typer_app()