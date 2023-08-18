## **Command Line Commands**

>[4. Docker](#docker)
>

---
### [🔼 Back to top](#commands)
---

### **Docker:**

|Description|Commands|
|--|--|
|Проверка за инсталация:|docker|
|Show Docker info:                                  |docker info|
|Show Docker version:                               |docker version|
|Show Docker version:                               |docker -v (docker --version)|
|Docker process status - show launched containers:  |docker ps|
|List all containers (only IDs):                    |docker ps -aq|
|Docker process status - show all containers:       |docker ps -a|
|Stop all running containers:                       |docker stop $(docker ps -aq)|
|Show all images:                                   |docker image ls|
|Show all images:                                   |docker images|
|Docker build in current directory:                 |docker build -t xxx .|
|Download current image:                            |docker pull ubuntu|
|Download image with current version:               |docker pull ubuntu:18.04|
|Run current image with random name container:      |docker run image|
|Run current image with current name container:     |docker run --name my-container my-image|
|Show containers:                                   |docker container ls|
|                                                   |docker rmi $(docker images -q) -f|
|Remove all containers:                             |docker rm $(docker ps -aq)|
|Remove all images:                                 |docker rmi $(docker images -q)|
|Remove all none images:                            |docker system prune|
|Delete current image without container:            |docker rmi image-name|
|Delete current image with container:               |docker rmi -f image-name|
|Run container:                                     |docker start my-container|
|Pause container:                                   |docker pause my-container|
|Stop container:                                    |docker stop my-container|
|Stop container (hard):                             |docker kill my-ubuntu|
|Show count of images, containers and ect:          |docker system df|
|Run multiple container:                            |docker-compose up|
|                                                   |docker-compose -f docker-compose.yaml -f docker-compose-infrastructure.yaml up --build|
|                                                   |docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build|
|--                                                 |docker-compose down|
|--                                                 |docker run -it ubuntu|
|--                                                 |docker network ls|
|Tag your images:                                   |docker tag shoppingapi:latest shoppingacr.azurecr.io/shoppingapi:v1|
|Tag your images:                                   |docker tag shoppingclient:latest shoppingacr.azurecr.io/shoppingclient:v1|

---
### [🔼 Back to top](#commands)
---