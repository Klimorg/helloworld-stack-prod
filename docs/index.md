# Helloworld stack prod : Sandbox for a pseudo production stack

The idea of this repo is to :

* try, train on new softwares,
* practice on Docker/k8s,
* apply best practices.

The final goal is to be the closest possible of what would be a **complete production stack**, meaning that you'll have :

* A REST api with an HTTP server,
* A monitored SQL database,
* A reverse proxy handling HTTPS,
* Some api monitoring,
* An authentication service.

Obviously you should have proper testing and deployment on a VPS via CI/CD.

Right now the four first points are implemented in an early stage. We have selected :

* A Python REST api made with [FastAPI](https://fastapi.tiangolo.com/) and [Gunicorn](https://gunicorn.org/) as an htttp server.
* [PostgreSQL](https://www.postgresql.org/) as a SQL database and [pgadmin](https://www.pgadmin.org/) to monitor it.
* [Traefik](https://traefik.io/) as reverse proxy,
* [Uptime Kuma](https://github.com/louislam/uptime-kuma) as simple uptime monitoring.

## Roadmap

1. Test [Caddy](https://caddyserver.com/v2) as reverse proxy.
2. Implement IAM with [Fief](https://www.fief.dev/) or [Keycloak](https://www.keycloak.org/) (try both).
3. [ELK Stack](https://www.elastic.co/fr/what-is/elk-stack) for monitoring, or [Jaeger](https://www.jaegertracing.io/).
4. Prometheus + Grafana ?

## Requirements :

Whether you work locally in "dev mode", or that this stack is deployed on a VPS, you'll need Docker and docker compose.

### Docker

* [Install Docker on the VPS](https://docs.docker.com/engine/install/ubuntu/)

* [Install using the convenience script](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)

### Docker-compose

* [Install docker-compose on the VPS](https://docs.docker.com/compose/install/)

* You might also need `haveged`, install it via `apt install haveged`. This is supposed to add more randomness to the VPS for docker-compose to start. TODO : [check this more in detail](https://wiki.archlinux.org/title/Haveged).


### Domain Name

To enable https, you'll need a domain name. You van buy one on [Name.com](https://www.name.com/).

### VPS

If you want to deploy this stack on a vps, you'll need to rent it, you can rent one for example on [DigitalOcean](https://cloud.digitalocean.com), for around 5 euros/month.


!!! info "Remark"

    If you have an old laptop, why not turn it into you own little [Ubuntu Server](https://dev.to/alejandro_du/your-old-laptop-is-your-new-database-server-4fca) and try deployement on it rtather than a vps ?



## Environement variables needed to be set

Traefik Dashboard :

  * `USERNAME`
  * `HASHED_PASSWORD`

PostgreSQl + FastaPI connection to DB :

  * `DB_USERNAME`
  * `DB_PASSWORD`

PgAdmin db monitoring :

  * `PGADMIN_DEFAULT_EMAIL`
  * `HASHED_PGADMIN_DEFAULT_EMAIL`

## Sources

Here are some sources that might be useful.


* [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
* [Deploying FastAPI Apps Over HTTPS with Traefik Proxy](https://www.youtube.com/watch?v=7N5O62FjGDc)
* [An Extremely Simple Docker, Traefik, and Python FastAPI Example](https://kleiber.me/blog/2021/03/23/simple-docker-traefik-python-fastapi-example/)
* [Dockerizing FastAPI with Postgres, Uvicorn, and Traefik](https://testdriven.io/blog/fastapi-docker-traefik/)
* [Tiangolo official fastapi docker image](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)
* [How to install Traefik 2.x on a Docker Swarm](https://blog.creekorful.org/2019/10/how-to-install-traefik-2-docker-swarm/)
* [Deploying FastAPI (and other) apps with HTTPS powered by Traefik](https://github.com/tiangolo/blog-posts/tree/master/deploying-fastapi-apps-with-https-powered-by-traefik)
* [Deploying a FastAPI app with Docker, Traefik, and Let's Encrypt](https://www.valentinog.com/blog/traefik/)


## Control startup and shutdown order in Compose

* https://docs.docker.com/compose/startup-order/
* https://github.com/jasonsychau/RelayAndContainers
* https://github.com/vishnubob/wait-for-it
* https://github.com/Eficode/wait-for
