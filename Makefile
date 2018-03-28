SHELL ?= /bin/bash
ARGS = $(filter-out $@,$(MAKECMDGOALS))

.SILENT: ;
.ONESHELL: ;
.NOTPARALLEL: ;
.EXPORT_ALL_VARIABLES: ;
Makefile: ;

.PHONY: bash
bash:
	docker-compose exec learn-py bash

.PHONY: buildup
buildup:
	docker-compose build
	docker-compose up -d

.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down -v

%:
@: