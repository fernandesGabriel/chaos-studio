ARG PYTHON_VERSION=3.8


# -------------------- py-base -------------------- #

FROM python:${PYTHON_VERSION}-alpine3.11 AS py-base

RUN set -x \
 && apk add --no-cache \
    jpeg-dev \
    zlib-dev \
    libjpeg

WORKDIR /chaos-studio


# -------------------- py-dependencies ------------ #

FROM py-base AS py-dependencies

COPY ./requirements.txt ./

RUN set -x \
 && apk add --no-cache \
    git \
    unzip \
    gcc \
    g++ \
    musl-dev \
    linux-headers \
    libffi-dev \
    \
 && mkdir /requirements \
    \
 && pip install --prefix=/requirements -Ur requirements.txt


# -------------------- py-cli -------------------- #

FROM py-base AS py-cli

COPY --from=py-dependencies /requirements /usr/local

COPY . .

RUN set -x \
 && pip install -e .
