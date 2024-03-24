FROM python:3.12-slim-bookworm

WORKDIR /workarea

RUN apt-get update && apt-get install -y git make

# Needed to downlod private modules 
ARG GITHUB_USER
ARG GITHUB_TOKEN 
RUN git config --global url."https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com".insteadOf "https://github.com"

COPY requirements.txt requirements-dev.txt ./
RUN pip install -r requirements-dev.txt
