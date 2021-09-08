#FROM python:3.9-slim-buster
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app
COPY ./pyproject.toml ./poetry.lock ./
RUN pip3 install poetry
RUN poetry install
