# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y

# Copying requirements of a project
COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

WORKDIR /app

COPY . /app/

RUN poetry install

CMD ["poetry", "run" , "python3", "index.py"]