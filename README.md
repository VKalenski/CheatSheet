# Commands

>[1. Git](#git)
>
>[2. Minikube](#minikube)
>
>[3. .NET](#net)
>
>[4. Docker](#docker)
>
>[5. Azure](#azure)
>
>[6. Kubernetes (K8s)](#kubernetes)
>
---

### ${\color{green}Git}$

|Description|Commands|
|--|--|
|Проверка на данните:|**git config --list**|
|Clone repo:|**git clone https://...**|
|Clone repo with current branch:|**git clone -b branch https://...**|
|Git Initial:|**git init**|
|Create file from CLI:|**touch text.txt**|
|Create file from CLI:|**echo This is sample text > MyFile.txt**|
|Open file from CLI:|**start .\txt.txt**|
|Read file from CLI:|**Get-Content .\txt.txt**|
|Промяна на съдържанието на файла през конзолата:|**get-Content .\txt.txt**|
|Проверка на статуса|**git status**|
|Добавяне на всички променени/създадени файлове:|**git add -A**|
|Добавяне на всички променени/създадени файлове:|**git add .**|
|Добавяне на конкретен файл:|**git add file.cs**|
|Създаване на коментар към commit-а:|**git commit -m "Text" -m "Text"**|
|Качване на промяната в съответния бранч:|**git push origin vk-branch**|
|Check the logs|**git log**|
|--|**git log -p**|
|--|**git log --stat**|
|--|**git log --pretty**|
|--|**git log --oneline**|
|--|**git shortlog**|
|Създаване на нов бранч:|**git branch vk-branch-new**|
|Създаване на нов бранч и преминаване в него:|**git checkout -b 'vk-branch-new'**|
|Преминаване в друг бранч:|**git checkout vk-branch-new**|
|Показване на всички бранчове:|**git branch**|
|Remove branch:|**git branch -d vk-branch**|
|--|**git branch -D vk-branch**|
|--|**git push -u origin <vk-branch-new>**|
|--|**git branch -d localBranchName**|
|--|**git branch -D localBranchName**|
|--|**git push origin --delete remoteBranchName**|
|```Show info for current branch:```|**git show origin vk-branch**|
|```Показва всички бранчове, които има в repo-то```|**git branch -av**|
|--|**git branch -v -a**|
|```Create folder with branches```|**git checkout -b 'vk/vk-user-example'**|
|--|**git merge branch**|
|--|**git blame**|
|--|--|
|--|--|
|--|--|
|--|--|
|--|--|

---
### [🔼 Back to top](#commands)
---

### Minikube:

Start administrator PowerShell  

|Description|Commands|
|--|--|
|First|choco install minikube|--|
|Second|Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))|https://minikube.sigs.k8s.io/docs/start/|
|Start|minikube start|--|
|Status|minikube status|--|
|Dashboard|minikube dashboard|--|

---
### [🔼 Back to top](#commands)
---

### .NET:

|--|--|
|--|--|
|View list with projects:|dotnet new --list|
|Create .NET MVC from the PowerShell:|dotnet new mvc|
|Create .NET Web Api from the PowerShell:|dotnet new webapi|
|Create .NET MVC with name from the PowerShell:|dotnet new mvc -n ProjectName|
|Create .NET Web Api with name from the PowerShell:|dotnet new webapi -n ProjectName|
|Create new .gitignore file:|dotnet new gitignore|
|Create migration:|dotnet-ef migrations add 'New migrations'|
|Update the database:|dotnet-ef database update|
|За вкарване на няколко проекта в общ solution:|dotnet new sln|
|За вкарване на няколко проекта в общ solution:|dotnet new sln --name MySolution|
|--|--|

---
### [🔼 Back to top](#commands)
---

### Docker:  

|--|--|
|--|--|
|Проверка за инсталация:|docker|
|Show Docker info:|docker info|
|Show Docker version:|docker version|
|Show Docker version:|docker -v (docker --version)|
|Docker process status - show launched containers:|docker ps|
|List all containers (only IDs):|docker ps -aq|
|Docker process status - show all containers:|docker ps -a|
|Stop all running containers:|docker stop $(docker ps -aq)|
|Show all images:|docker image ls|
|Show all images:|docker images|
|Docker build in current directory:|docker build -t xxx .|
|Download current image:|docker pull ubuntu|
|Download image with current version:|docker pull ubuntu:18.04|
|Run current image with random name container:|docker run image|
|Run current image with current name container:|docker run --name my-container my-image|
|Show containers:|docker container ls|
||docker rmi $(docker images -q) -f|
|Remove all containers:|docker rm $(docker ps -aq)|
|Remove all images:|docker rmi $(docker images -q)|
|Remove all none images:|docker system prune|
|Delete current image without container:|docker rmi image-name|
|Delete current image with container:|docker rmi -f image-name|
|Run container:|docker start my-container|
|Pause container:|docker pause my-container|
|Stop container:|docker stop my-container|
|Stop container (hard):|docker kill my-ubuntu|
|Show count of images, containers and ect:|docker system df|
|Run multiple container:|docker-compose up|
||docker-compose -f docker-compose.yaml -f docker-compose-infrastructure.yaml up --build|
||docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build|
|--|docker-compose down|
|--|docker run -it ubuntu|
|--|docker network ls|
|Tag your images:|docker tag shoppingapi:latest shoppingacr.azurecr.io/shoppingapi:v1|
|Tag your images:|docker tag shoppingclient:latest shoppingacr.azurecr.io/shoppingclient:v1|

---
### [🔼 Back to top](#commands)
---

### Azure:

https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
  
https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli

Start PowerShell

---

Table for ```INSTALL```, ```UPDATE``` and ```LOGIN``` commands:

|Description|Commands|
|--|--|
|Инсталиране на Azure CLI:|az aks install-cli|
|Проверка за инсталация:|az|
|Проверка на версията:|az version|
|Ъпгрейд на версията:|az upgrade|
|Log in Azure Portal:|az login|
|Log in to the container registry:|az acr login --name myNameOfAcr|
||az aks get-upgrades --name euroins-aks-staging --resource-group euroins-rg-staging|
||az aks upgrade --kubernetes-version 1.24.9 --name euroins-aks-staging --resource-group euroins-rg-staging|
||az aks nodepool upgrade --cluster-name euroins-aks-staging -g euroins-rg-staging -n agentpool|
||az aks upgrade --resource-group euroins-rg-staging --name euroins-aks-staging --kubernetes-version 1.24.9|
||az aks get-upgrades --resource-group myResourceGroup --name myAKSCluster --output table|

---

Table for ```CREATE``` commands:

|Description|Commands|
|--|--|
|Create a resource group:|az group create --name myResourceGroup --location westeurope|
|Create an Azure Container Registry:|az acr create --resource-group myResourceGroup --name shoppingacr --sku Basic|
|Create AKS cluster with attaching ACR:|az aks create --resource-group myResourceGroup --name myAKSCluster --node-count 1 --generate-ssh-keys --attach-acr myNameOfAcr|

---

Table for ```OTHER``` commands:

|Description|Commands|
|--|--|
|Enable Admin Account for ACR Pull:|az acr update -n shoppingacr --admin-enabled true|
|Get the login server address:|az acr list --resource-group myResourceGroup --query "[].{acrLoginServer:loginServer}" --output table|
|List images in registry:|az acr repository list --name shoppingacr --output table|
|See tags|az acr repository show-tags --name shoppingacr --repository shoppingclient --output table|
|Проверка на клъстърите в K8s:|az aks list|
|--|az aks show --resource-group euroins-rg-staging --name euroins-aks-staging --output table|
|--|az aks show --resource-group euroins-rg-staging --name euroins-aks-staging|
|Clean All AKS and Azure Resources:|az group delete --name myResourceGroup --yes --no-wait|
|--|kubectl get pdb -A|
||az account set --subscription 69a94853-fcae-446b-917c-2bd00ba3e3ea|
||az aks get-credentials --resource-group cloud-shell-storage-westeurope --name vk-aks-dev|
||az aks get-credentials --admin --name MyManagedCluster --resource-group MyResourceGroup|
||az aks show --resource-group euroins-rg-staging --name euroins-aks-staging --output table|
||az aks show --resource-group euroins-rg-staging --name euroins-aks-staging|
||kubectl get pdb -A|

---
### [🔼 Back to top](#commands)
---

### Kubernetes:
https://kubernetes.io/docs/reference/kubectl/

Start PowerShell

Table for ```INSTALL``` and ```LOGIN``` commands:

|Description|Command|
|--|--|
|Install the Kubernetes CLI:|az aks install-cli|
|Проверка на инсталацията:|kubectl|
|Проверка на версията:|kubectl version|
|Проверка на версията:|kubectl version --short|
|Проверка на версията:|kubectl version --output=yaml|
|Проверка на версията:|kubectl version --output=json|
|Connect to cluster using kubectl:|az aks get-credentials --resource-group myResourceGroup --name myAKSCluster|
|Show info for cluster:|kubectl cluster-info|

---

Table for ```GET``` commands:

|Description|Command|
|--|--|
|Show all namespaces:|kubectl get namespaces|
|Show all namespaces:|kubectl get ns|
|Show all nodes:|kubectl get nodes|
|Show all deployments:|kubectl get deployment|
|Show all deployments from current namespace:|kubectl get deployment -n dev|
|Show all replicasets:|kubectl get replicaset|
|Show all replicasets from current namespace:|kubectl get replicaset -n dev|
|Show all services:|kubectl get services|
|Show all services:|kubectl get svc|
|Show all services from current namespace:|kubectl get svc -n dev|
|Show all pods:|kubectl get pods|
|Show all pods from current namespace:|kubectl get pods -n dev|
|Show all pods:|kubectl get pods --watch|
|Show all:|kubectl get all|

---

Table for ```DESCRIBE``` commands:

|Description|Command|
|--|--|
|Explain namespace:|kubectl describe namespace|
|Explain service:|kubectl describe service <name-service>|
|Explain pod:|kubectl describe <pod-name>|
|Explain pods:|kubectl describe pods --namespace kube-system|

---

Table for ```LOGS``` commands:

|Description|Command|
|--|--|
|--|kubectl logs <name-deployment>|
|--|kubectl logs <name-service>|
|--|kubectl logs <name-pod>|

---

Table for ```OTHERS``` commands

|Description|Command|
|--|--|
|--|kubectl rollout restart deploy <name-deploy>|
|Apply .yml file:|kubectl apply -f .\xxx.yml|  
|Deploy microservices to AKS:|kubectl apply -f .\aks\|
|--|kubectl config get-contexts|
|--|kubectl config current-context|  
|--|kubectl config use-context gcpcluster-k8s-1|
|--|kubectl delete deployment swn-nginx|
|--|kubectl create deployment mongo-depl --image=mongo|
|--|kubectl exec mongo-depl-5fd6b7d4b4-6xzjd -it sh|

---
### [🔼 Back to top](#commands)
---
