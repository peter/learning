# Learning Docker

Notes in learning [Docker](https://www.docker.com/).

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

* [Learn Docker in 12 minutes (video)](https://www.youtube.com/watch?v=YFl2mCHdv24)
* [Getting started with docker, the step by step tutorial with examples (video)](https://www.youtube.com/watch?v=Vyp5_F42NGs)
* [Getting started with docker, the step by step tutorial with examples (blog post)](http://takacsmark.com/getting-started-with-docker-in-your-project-step-by-step-tutorial/)
* [Docker Hub](https://hub.docker.com)
