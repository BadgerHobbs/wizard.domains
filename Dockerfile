FROM python:3.7
RUN mkdir /app 
COPY . /app
COPY pyproject.toml /app 
WORKDIR /app
ENV PYTHONPATH=.
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

ENV OPENAI_API_KEY ""
ENV WSGI_WORKERS 3
ENV PORT 5000

# run
CMD ["poetry", "run", "python", "program/main.py"]