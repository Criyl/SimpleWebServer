FROM python:3.8

ENV HOST 0.0.0.0
ENV PORT 8000

# TODO( Not the recommended means of installing, replace with curling get-poetry.py noted at https://python-poetry.org/docs/ )
RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.toml poetry.lock /app/
RUN poetry install --no-interaction

COPY . .

EXPOSE $PORT
CMD ["poetry", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "server:app"]