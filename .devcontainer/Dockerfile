# https://github.com/CrafterKolyan/tiny-python-docker-image/tree/main
FROM python:3.11.6-slim-bullseye

RUN apt update
RUN apt install -y --no-install-recommends git wget unzip
RUN rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/duckdb/duckdb/releases/download/v0.9.1/duckdb_cli-windows-amd64.zip && unzip duckdb_cli-linux-amd64.zip -d /usr/local/bin && rm duckdb_cli-linux-amd64.zip

ENTRYPOINT ["/bin/bash", "-c"]