.PHONY: docker-run
docker-run:
	docker run -it -p 8000:80 app

.PHONY: sync
sync:
	rsync -a ./* root@mathieuklimczak.com:/root/code/tuto_traefik/

.PHONY: network-up
network-up:
	docker network create traefik-public

.PHONY: network-down
network-down:
	docker network rm traefik-public

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
stack-prod-up:
	docker compose -f docker-compose.yml -f docker-compose-prod.yml pull

.PHONY: stack-prod-up
stack-prod-up:
	docker compose -f docker-compose.yml -f docker-compose-prod.yml up --build

.PHONY: stack-prod-down
stack-prod-down:
	docker compose -f docker-compose.yml -f docker-compose-prod.yml -v down

.PHONY: stack-dev-up
stack-dev-up:
	docker compose -f docker-compose.yml -f docker-compose-dev.yml up --build

.PHONY: stack-dev-down
stack-dev-down:
	docker compose -f docker-compose.yml -f docker-compose-dev.yml -v down

.PHONY: install-dev
install-dev:
	python -m pip install -e ".[dev]" --no-cache-dir
	pre-commit install
	pre-commit autoupdate
