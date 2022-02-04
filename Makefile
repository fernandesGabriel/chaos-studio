.PHONY: build

.DEFAULT_GOAL := build

start: build cli

build:
	DOCKER_BUILDKIT=1 docker-compose build --pull --parallel

cli:
	docker-compose run --rm cli ash