I have a small stack that use for training on best practices and new softwares (I plan to use it as a production stack template, but I'm far from it for now). The stack is comprised of :

* A small basic UI made with streamlit (I'm more of a backend guy, so I don't bother with UI for now),
* A python backend done with FastAPI+gunicorn,
* The DB used is postgre, monitored by pgadmin,
* Uptime-kuma is used for a "really simple" uptime monitoring of the api,
* Traefik as a reverse proxy with https,
* Mkdocs for the documentation.

The whole CI/CD is powered by github actions. But lately, the pipeline doesn't end. I have to cancel it to end the pipeline.

More precisely the part named `Update stack` is the job `deploy-stack` doesn't end and stay idle. I'm even able to connect to my VPS, dot a `GET` or `POST` request and see the result in the github runner terminal, so the last command `exit` doesn't pass it seems.

Apart from some rewriting in the github action, I haven't touch in the rest of the project for a long time.

Do any of you have had this problem lately ?

For the record, here's github action pipeline, the rest of the project can be found at this [public repo](https://github.com/Klimorg/stack_prod).


```yaml
---
name: Build & Deploy
on: [push, pull_request]

env:
    API_NAME: api-prod
    UI_NAME: ui-prod

jobs:
    tests:
        runs-on: ${{ matrix.os }}
        strategy:
            fail-fast: false
            matrix:
                os: [ubuntu-latest, macos-latest]
                python-version: ['3.8', '3.9', '3.10']
                exclude:
                    - os: macos-latest
                      python-version: '3.8'

        steps:
            - uses: actions/checkout@v3
            - name: Set up Python
              uses: actions/setup-python@v3
              with:
                  python-version: ${{ matrix.python-version }}

            - name: Display Python version
              run: python --version

            - name: Install Python dependencies
              run: |
                  python -m pip install --upgrade pip
                  python -m pip install -r app/requirements.txt
                  python -m pip install -r frontend/requirements.txt
                  python -m pip install -r requirements-test.txt

            - name: Run test suite
              run: |
                  python -m pytest -v

    build-image:
        needs: tests
        runs-on: ubuntu-latest
        steps:
            - name: Set up QEMU
              uses: docker/setup-qemu-action@v2

            - name: Set up Docker Buildx
              uses: docker/setup-buildx-action@v2

            - name: Login to DockerHub
              uses: docker/login-action@v2
              with:
                  username: ${{ secrets.DOCKERHUB_USERNAME }}
                  password: ${{ secrets.DOCKERHUB_ACCESS_TOKEN }}

            - name: Build and push
              id: docker_build_api
              uses: docker/build-push-action@v3
              with:
                  file: Dockerfile.backend
                  # push new image only if on main branch
                  push: ${{ github.ref == 'refs/heads/main' }}
                  tags: |
                      vorphus/${{ env.API_NAME }}:latest
                      vorphus/${{ env.API_NAME }}:${{ github.sha }}

            - name: Image digest
              run: echo ${{ steps.docker_build_api.outputs.digest }}

            - name: Build and push
              id: docker_build_ui
              uses: docker/build-push-action@v3
              with:
                  file: Dockerfile.frontend
                  # push new image only if on main branch
                  push: ${{ github.ref == 'refs/heads/main' }}
                  tags: |
                      vorphus/${{ env.UI_NAME }}:latest
                      vorphus/${{ env.UI_NAME }}:${{ github.sha }}

            - name: Image digest
              run: echo ${{ steps.docker_build_ui.outputs.digest }}

    deploy-stack:
        needs: build-image
        # update stack only if on main branch, not on dev or any other
        if: ${{ github.ref == 'refs/heads/main' }}
        runs-on: ubuntu-latest
        steps:
            - name: Configure SSH
              run: |
                  mkdir -p ~/.ssh/
                  echo "$SSH_KEY" > ~/.ssh/deploy
                  chmod 600 ~/.ssh/deploy
                  cat >>~/.ssh/config <<END
                  Host staging
                    HostName $SSH_HOST
                    User $SSH_USER
                    IdentityFile ~/.ssh/deploy
                    StrictHostKeyChecking no
                  END
              env:
                  SSH_USER: ${{ secrets.SSH_USERNAME }}
                  SSH_KEY: ${{ secrets.SSH_KEY }}
                  SSH_HOST: ${{ secrets.SSH_HOST }}

            - name: Add deploy key to ssh-agent
              run: ssh staging 'eval "$(ssh-agent -s)" && ssh-add ~/.ssh/deploy && ssh-add -l -E md5 && cd /opt/stack_prod && git checkout main && git pull
                  origin main && exit'

            - name: Update stack
              run: |
                  ssh staging <<EOF
                  export DEPLOYMENT_COMMIT=${{ github.sha }}
                  export DEPLOYMENT_DATE=${{ github.event.repository.pushed_at }}
                  export DB_USERNAME=${{ secrets.DB_USERNAME }}
                  export DB_PASSWORD=${{ secrets.DB_PASSWORD }}
                  export PGADMIN_DEFAULT_EMAIL=${{ secrets.PGADMIN_DEFAULT_EMAIL }}
                  export HASHED_PGADMIN_DEFAULT_PASSWORD=${{ secrets.HASHED_PGADMIN_DEFAULT_PASSWORD }}
                  cd /opt/stack_prod
                  make pull-updated-stack
                  make stack-prod-up
                  exit
                  EOF

            - name: Disconnect
              run: echo "ssh connection terminated"

    build-docs:
        needs: tests
        runs-on: ubuntu-latest
        steps:
            - name: Checkout repo
              uses: actions/checkout@v3
            - name: Set up Python
              uses: actions/setup-python@v3
              with:
                  python-version: '3.9'
            - name: Install dependencies
              run: |
                  python -m pip install -e ".[docs]" --no-cache-dir
            - name: Deploy documentation
              run: mkdocs gh-deploy --force
```
