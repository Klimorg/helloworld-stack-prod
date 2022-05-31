.PHONY: docker-run
docker-run:
	docker run -it -p 8000:80 app

.PHONY: sync
sync:
	rsync -a ./* root@mathieuklimczak.com:/root/code/tuto_traefik/

.PHONY: traefik-up
traefik-up:
	docker-compose -f docker-compose.traefik.yml up -d

.PHONY: network
network:
	docker network create traefik-public

.PHONY: stack-up
stack-up:
	docker-compose -f docker-compose.yml up -d

.PHONY: install-dev
install-dev:
	python -m pip install -e ".[dev]" --no-cache-dir
	pre-commit install
	pre-commit autoupdate
