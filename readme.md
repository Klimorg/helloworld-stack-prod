# Tutorial : FastAPI stack with Traefik reverse proxy

## Sources :

* [Deploying FastAPI Apps Over HTTPS with Traefik Proxy](https://www.youtube.com/watch?v=7N5O62FjGDc)
* [An Extremely Simple Docker, Traefik, and Python FastAPI Example](https://kleiber.me/blog/2021/03/23/simple-docker-traefik-python-fastapi-example/)
* [Dockerizing FastAPI with Postgres, Uvicorn, and Traefik](https://testdriven.io/blog/fastapi-docker-traefik/)
* [Tiangolo official fastapi docker image](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)
* [How to install Traefik 2.x on a Docker Swarm](https://blog.creekorful.org/2019/10/how-to-install-traefik-2-docker-swarm/)
* [Deploying FastAPI (and other) apps with HTTPS powered by Traefik](https://github.com/tiangolo/blog-posts/tree/master/deploying-fastapi-apps-with-https-powered-by-traefik)
* [Deploying a FastAPI app with Docker, Traefik, and Let's Encrypt](https://www.valentinog.com/blog/traefik/)

## Requirements :
To do https with Traefik, you'll need :

* a Domain Name, check [Name.com](https://www.name.com/) to buy one, the cheapest one can be around 2 euros for a year,
* and a VPS, you can but one for example on [DigitalOcean](https://cloud.digitalocean.com), for around 5 euros/month.

### Connect your domain name to your VPS
## Steps :

### Docker

* [Install Docker on the VPS](https://docs.docker.com/engine/install/ubuntu/)

* [Install using the convenience script](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)

### Docker-compose

* [Install docker-compose on the VPS](https://docs.docker.com/compose/install/)

* `apt install haveged` : add more randomness to the VPS for docker-compose to start. TODO : check this more in detail.

* On the VPS, make two directories.

```shell
root@ubuntu-s-1vcpu-2gb-ams3-01:~# mkdir code
root@ubuntu-s-1vcpu-2gb-ams3-01:~# cd code/
root@ubuntu-s-1vcpu-2gb-ams3-01:~/code# mkdir tuto_traefik
root@ubuntu-s-1vcpu-2gb-ams3-01:~/code# cd tuto_traefik/
root@ubuntu-s-1vcpu-2gb-ams3-01:~/code/tuto_traefik#
```

* Copy all the files that are in the local project on the vps.

`rsync -a ./* root@mathieuklimczak.com:/root/code/tuto_traefik/`

`rsync -a ./*` *copy everything in this directory*

`rsync -a ./* root@mathieuklimczak.com` *copy everything in this directory, on this vps*

``rsync -a ./* root@mathieuklimczak.com:/root/code/tuto_traefik/`` *copy everything in this directory, on this vps, in the following directory*.

?Question : is `rsync` really copy or synchronization ?

* Once it all has been synced, fire up docker-compose on vps side. Once it has been launched, you can access to the FastAPI doc via `http://mathieuklimczak.com/docs`. Note that right now it's still classical HTTP protocol, not HTTPS. That's what we are going to do now.

* Check the `docker-compose.traefik.yml` file to see the configuration of Traefik, and the `docker-compose.yml` file to see the configuration of the stack

* `docker-compose.override.yml` is used for local development. To check !


## Monitoring Backend with Uptime-Kuma

* [Uptime-Kuma Traefik configuration](https://github.com/louislam/uptime-kuma/wiki/Reverse-Proxy#Traefik)