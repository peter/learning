# Learning Docker

Notes in learning [Docker](https://www.docker.com/).

## Dockerfile Example

```Dockerfile
FROM python:latest

WORKDIR /app

# Copy/install dependencies before code - they dont' change as often
# Each step in the Dockerfile may be cached
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy source code
COPY . /app

# Start server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080]
```

## docker-compose.yml Example

For running locally with hot-reload (due to the start command and the volumes directive):

```yml
services:
    app:
        build: .
        container_name: my-app
        command: unvicorn main:app --host 0.0.0.0 --port 80 --reload
        ports:
            - 8080:80
        volumes:
             - .:/app             
```

## Running Postgres

https://hub.docker.com/_/postgres

```sh
docker pull postgres

docker run --name bs_db -p 5432:5432 -e POSGRES_USER=... -e POSGRES_PASSWORD=... -d postgres
docker ps

```

## Basic Commands to Build/Run a Dockerfile/Project

```sh
docker build -t my-app .
# This binds port 80 on local machine to 8080 in container
docker run -d 80:8080 my-app
```

## Tutorial

```
docker help pull # Pull an image or a repository from a registry
docker images
docker help run # Run a command in a new container
docker ps -as
docker help stop

docker run --name mynginx -p 80:80 nginx:10.2-alpine

docker help rm
```

Runtime parameters of a container cannot be changed even if it's stopped.

When you do `docker rm` any data in the container will be lost. For that reason
you can put data in volumes instead.

The port option in run command is a `host:container` mapping.

You can specify a tag when pulling an image, i.e. a version number or `latest`.
The tag can also specify which Linux distribution the image is based on.

You may use a private Docker registry at your company.

## Resources

* [How To Use Docker To Make Local Development A Breeze (ArjanCodes)](https://www.youtube.com/watch?v=zkMRWDQV4Tg)
* [Learn Docker in 12 minutes (video)](https://www.youtube.com/watch?v=YFl2mCHdv24)
* [Getting started with docker, the step by step tutorial with examples (video)](https://www.youtube.com/watch?v=Vyp5_F42NGs)
* [Getting started with docker, the step by step tutorial with examples (blog post)](http://takacsmark.com/getting-started-with-docker-in-your-project-step-by-step-tutorial/)
* [Docker Hub](https://hub.docker.com)
