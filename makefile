network_name = traefik-public
prod_prefix = stack-prod
dev_prefix = stack-dev


.PHONY: network-up
network-up:
	docker network create $(network_name)

.PHONY: network-down
network-down:
	docker network rm $(network_name)

.PHONY: traefik-dev-up
traefik-dev-up:
	docker compose -f docker-compose.traefik.yml -f docker-compose.traefik-dev.yml up -d

.PHONY: traefik-dev-down
traefik-dev-down:
	docker compose -f docker-compose.traefik.yml -f docker-compose.traefik-dev.yml -v down

.PHONY: traefik-prod-up
traefik-prod-up:
	docker compose -f docker-compose.traefik.yml -f docker-compose.traefik-prod.yml up -d

.PHONY: traefik-prod-down
traefik-prod-down:
	docker compose -f docker-compose.traefik.yml -f docker-compose.traefik-prod.yml -v down

.PHONY: stack-prod-pull
stack-prod-pull:
	docker compose -f docker-compose.yml -f docker-compose-prod.yml pull

.PHONY: stack-prod-up
stack-prod-up:
	docker compose -f docker-compose.yml -f docker-compose-prod.yml -p $(prod_prefix) up -d --build --remove-orphans

.PHONY: stack-prod-down
stack-prod-down:
	docker compose -f docker-compose.yml -f docker-compose-prod.yml -p $(prod_prefix) -v down

.PHONY: pull-updated-stack
pull-updated-stack:
	docker compose -f docker-compose.yml -f docker-compose-prod.yml pull

.PHONY: stack-dev-up
stack-dev-up:
	docker compose -f docker-compose.yml -f docker-compose-dev.yml -p $(dev_prefix) up --build --remove-orphans

.PHONY: stack-dev-down
stack-dev-down:
	docker compose -f docker-compose.yml -f docker-compose-dev.yml -p $(dev_prefix) -v down

.PHONY: install-dev
install-dev:
	python -m pip install -r requirements-dev.txt
	pre-commit install
	pre-commit autoupdate
