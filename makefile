.PHONY: docker-run
docker-run:
	docker run -it -p 8000:80 app

.PHONY: sync
sync:
	rsync -a ./* root@mathieuklimczak.com:/root/code/tuto_traefik/

.PHONY: traefik-up
traefik-up:
	docker compose -f docker-compose.traefik.yml up -d

.PHONY: traefik-down
traefik-down:
	docker compose -f docker-compose.traefik.yml -v down

.PHONY: network-up
network-up:
	docker network create traefik-public

.PHONY: network-down
network-down:
	docker network rm traefik-public

.PHONY: stack-up
stack-up:
	docker-compose -f docker-compose.yml up -d

.PHONY: dev-stack-up
dev-stack-up:
	docker compose -f docker-compose.yml -f docker-compose-dev.yml up --build

.PHONY: dev-stack-down
dev-stack-down:
	docker compose -f docker-compose.yml -f docker-compose-dev.yml -v down

.PHONY: install-dev
install-dev:
	python -m pip install -e ".[dev]" --no-cache-dir
	pre-commit install
	pre-commit autoupdate
