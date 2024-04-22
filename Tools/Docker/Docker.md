# **Docker**

|Description|Commands|
|--|--|
|docker                                        |Check the installation                           |
|docker info                                   |Show Docker info                                 |
|docker version                                |Show Docker version                              |
|docker -v (docker --version)                  |Show Docker version                              |
|docker ps                                     |Docker process status - show launched containers |
|docker ps -aq                                 |List all containers (only IDs)                   |
|docker ps -a                                  |Docker process status - show all containers      |
|docker stop $(docker ps -aq)                  |Stop all running containers                      |
|docker image ls                               |Show all images                                  |
|docker images                                 |Show all images                                  |
|docker build -t xxx .                         |Docker build in current directory                |
|docker pull ubuntu                            |Download current image                           |
|docker pull ubuntu:18.04                      |Download image with current version              |
|docker run image                              |Run current image with random name container     |
|docker run --name my-container my-image       |Run current image with current name container    |
|docker container ls                           |Show containers                                  |
|docker rmi $(docker images -q) -f             |                                                 |
|docker rm $(docker ps -aq)                    |Remove all containers                            |
|docker rmi $(docker images -q)                |Remove all images                                |
|docker system prune                           |Remove all none images                           |
|docker rmi image-name                         |Delete current image without container           |
|docker rmi -f image-name                      |Delete current image with container              |
|docker start my-container                     |Run container                                    |
|docker pause my-container                     |Pause container                                  |
|docker stop my-container                      |Stop container                                   |
|docker kill my-ubuntu                         |Stop container (hard)                            |
|docker system df                              |Show count of images, containers and ect         |



### **Docker Compose commands:**

|Description|Commands|
|--|--|
|docker-compose up                                |Run multiple container                              |
|docker-compose -f docker-compose.yaml -f docker-compose-infrastructure.yaml up --build|||
|docker-compose -f docker-compose.yml -f docker-compose.override.yml up -build|              ||
|docker-compose down                                                       |--|
|docker run -it ubuntu                                                     |--|
|docker network ls          |--|
|docker tag shoppingapi:latest shoppingacr.azurecr.io/shoppingapi:v1|Tag your images:|
|docker tag shoppingclient:latest shoppingacr.azurecr.io/shoppingclient:v1|Tag your images:|
