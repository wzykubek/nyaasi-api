FROM python:3.9.5-slim-buster

LABEL org.opencontainers.image.source https://github.com/samedamci/nyaasi-api

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m pip install poetry && python -m poetry config virtualenvs.create false
COPY pyproject.toml /app/
RUN apt-get update && apt-get install -y gcc make
RUN python -m poetry install -n --no-root --no-dev
RUN python -m pip uninstall -y poetry && apt-get purge -y gcc make

COPY . /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

EXPOSE 5000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:5000", "nyaasiapi:app"]
