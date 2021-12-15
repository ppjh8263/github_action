FROM python:3.7.11-slim-buster

COPY . /workdir
WORKDIR /workdir
ENV PYTHONPATH=/workdir
ENV PYTHONUNBUFFERED=1

RUN /bin/bash \
    && apt-get update \
    && apt-get install curl -y\
    && apt-get install ffmpeg libsm6 libxext6 -y\
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && pwd \
    && bash docker_bash.sh

CMD ["bash", "start.sh"]