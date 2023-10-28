# https://github.com/CrafterKolyan/tiny-python-docker-image/tree/main
FROM python:slim

RUN apt update
RUN apt install -y --no-install-recommends git parallel locales
RUN rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/bin/bash", "-c"]