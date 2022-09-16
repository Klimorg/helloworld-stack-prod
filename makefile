network_name = traefik-public
prod_prefix = stack-prod
dev_prefix = stack-dev

#### Networks ####

.PHONY: network-up
network-up:
	docker network create $(network_name)

.PHONY: network-down
network-down:
	docker network rm $(network_name)

#### Reverse Proxies ####
#### Traefik ####

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

#### Caddy ####

.PHONY: caddy-dev-up
caddy-dev-up:
	docker compose -f docker-compose.caddy.yml -f docker-compose.caddy-dev.yml up -d

.PHONY: caddy-dev-down
caddy-dev-down:
	docker compose -f docker-compose.caddy.yml f docker-compose.caddy-dev.yml -v down

.PHONY: caddy-prod-up
caddy-prod-up:
	docker compose -f docker-compose.caddy.yml -f docker-compose.caddy-prod.yml up -d

.PHONY: caddy-prod-down
caddy-prod-down:
	docker compose -f docker-compose.caddy.yml f docker-compose.caddy-prod.yml -v down


#### Stack ####
#### V1 ####

.PHONY: stack-prod-up
stack-prod-up:
	docker compose -f docker-compose-v1.yml -f docker-compose-prod-v1.yml -p $(prod_prefix) up -d --build --remove-orphans

.PHONY: stack-prod-down
stack-prod-down:
	docker compose -f docker-compose-v1.yml -f docker-compose-prod-v1.yml -p $(prod_prefix) -v down

.PHONY: pull-updated-stack
pull-updated-stack:
	docker compose -f docker-compose-v1.yml -f docker-compose-prod-v1.yml pull

.PHONY: stack-dev-up
stack-dev-up:
	docker compose -f docker-compose-v1.yml -f docker-compose-dev-v1.yml -p $(dev_prefix) up --build --remove-orphans

.PHONY: stack-dev-down
stack-dev-down:
	docker compose -f docker-compose-v1.yml -f docker-compose-dev-v1.yml -p $(dev_prefix) -v down

#### V2 ####

.PHONY: stack-dev-v2-up
stack-dev-v2-up:
	docker compose -f docker-compose-v2.yml -f docker-compose-dev-v2.yml -p $(dev_prefix) up --build --remove-orphans

.PHONY: stack-dev-v2-down
stack-dev-v2-down:
	docker compose -f docker-compose-v2.yml -f docker-compose-dev-v2.yml -p $(dev_prefix) -v down

.PHONY: pull-updated-stack-v2
pull-updated-stack-v2:
	docker compose -f docker-compose-v2.yml -f docker-compose-prod-v2.yml pull

.PHONY: stack-prod-v2-up
stack-prod-v2-up:
	docker compose -f docker-compose-v2.yml -f docker-compose-prod-v2.yml -p $(dev_prefix) up --build --remove-orphans

.PHONY: stack-prod-v2-down
stack-prod-v2-down:
	docker compose -f docker-compose-v2.yml -f docker-compose-prod-v2.yml -p $(dev_prefix) -v down

.PHONY: install-dev
install-dev:
	python -m pip install -r requirements-dev.txt
	pre-commit install
	pre-commit autoupdate
