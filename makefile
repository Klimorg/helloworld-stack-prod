.PHONY: run_docker
run_docker:
	docker run -it -p 8000:80 app

.PHONY: sync
sync:
	rsync -a ./* root@mathieuklimczak.com:/root/code/tuto_traefik/

.PHONY: traefik_up
traefik_up:
	docker-compose -f docker-compose.traefik.yml up -d

.PHONY: network
network:
	docker network create traefik-public

.PHONY: stack_up
stack_up:
	docker-compose -f docker-compose.yml up -d