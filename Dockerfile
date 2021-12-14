FROM python:3.7.11-slim-buster

COPY . /workdir
WORKDIR /workdir
ENV PYTHONPATH=/workdir
ENV PYTHONUNBUFFERED=1

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && source $HOME/.poetry/env \
    && poetry install \
    && poetry shell \
    && poe force-cuda11

CMD ["nohup", "python", "api.py", ">>", "server/logs/docker.txt"]