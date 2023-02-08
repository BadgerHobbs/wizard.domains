# Wizard Domains
An example AI Domain Name Generator Powered by GPT-3.

> Generate the perfect domain name for your website using OpenAI's GPT-3 technology with Wizard Domains. Get instant suggestions and find the perfect name for your brand.

## About
- Uses [OpenAI's GPT-3 API](https://openai.com/api/) to generate 5 domains based on a user-provided prompt.
- Front-End written in vanilla HTML/CSS/JS, using the [Pink](https://github.com/appwrite/pink) CSS library for core UI components.
- Uses [FastAPI](https://fastapi.tiangolo.com/) as the backend webserver, optionally running Uvicorn or Gunicorn.
- Uses [Typer](https://typer.tiangolo.com/) for the command line interface when running locally.
- Uses [Poetry](https://python-poetry.org/docs/) for package management.
- Uses [ParticlesJS](https://vincentgarreau.com/particles.js/) for the animated background.
- Checks domain availability by pinging the address using a socket.

## Locally
Note: Though you can use pip, it is reccomended to use [Poetry](https://python-poetry.org/docs/) to install and manage the required Python packages.

```bash
poetry run python program/main.py --help
```
```bash
poetry run python program/main.py --uvicorn --openai-api-key="XXX"
```

## Docker
```bash
docker build -t wizard-domains .
```

```bash
docker run -d \
    --name wizard-domains \
    -p 5011:5000 \
    -e OPENAI_API_KEY="XXX" \
    --restart on-failure \
    wizard-domains
```