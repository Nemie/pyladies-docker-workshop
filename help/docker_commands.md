Docker cheatsheet
=================

`docker ps` _list running containers_

`docker ps -a` _list all containers, running and stopped_

`docker run <image name>` _run a container based on the given image_

`docker stop <container id/name>` _stop container_

`docker rm <container id/name>` _delete container_

`docker build <Dockerfile path>` _builds an image based on the given dockerfile_

`docker images` _list images_

`docker rmi <image name>` _delete image_

`docker-compose up` _start containers defined in docker-compose.yml_

`docker-compose stop` _stop containers defined in docker-compose.yml_

`docker-compose build` _build defined in docker-compose.yml_

`docker-compose rm` _destroy stopped containers_
