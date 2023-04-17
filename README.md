# Commands Documentation 

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

### Git:

|--|--|
|--|--|
|```Проверка на данните:```|**git config --list**|
|```Clone repo:```|**git clone https://...**|
|```Clone repo with current branch:```|**git clone -b branch https://...**|
|```Git Initial:```|**git init**|
|```Create file from CLI:```|**touch text.txt**|
|```Create file from CLI:```|**echo This is sample text > MyFile.txt**|
|```Open file from CLI:```|**start .\txt.txt**|
|```Read file from CLI:```|**Get-Content .\txt.txt**|
|```Промяна на съдържанието на файла през конзолата:```|**get-Content .\txt.txt**|
|```Проверка на статуса```|**git status**|
|```Добавяне на всички променени/създадени файлове:```|**git add -A**|
|```Добавяне на всички променени/създадени файлове:```|**git add .**|
|```Добавяне на конкретен файл:```|**git add file.cs**|
|```Създаване на коментар към commit-а:```|**git commit -m "Text" -m "Text"**|
|```Качване на промяната в съответния бранч:```|**git push origin vk-branch**|
|```Check the logs```|**git log**|
|--|**git log -p**|
|--|**git log --stat**|
|--|**git log --pretty**|
|--|**git log --oneline**|
|--|**git shortlog**|
|```Създаване на нов бранч:```|**git branch vk-branch-new**|
|```Създаване на нов бранч и преминаване в него:```|**git checkout -b 'vk-branch-new'**|
|```Преминаване в друг бранч:```|**git checkout vk-branch-new**|
|```Показване на всички бранчове:```|**git branch**|
|```Remove branch:```|**git branch -d vk-branch**|
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

### Minikube:

Start administrator PowerShell  

|--|--|
|--|--|
|First|choco install minikube|--|
|Second|Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))|https://minikube.sigs.k8s.io/docs/start/|
|Start|minikube start|--|
|Status|minikube status|--|
|Dashboard|minikube dashboard|--|

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

### Docker:  

|--|--|
|--|--|
|Проверка за инсталация:|docker|
|Show Docker info:|docker info|
|Show Docker version:|docker version|
|Show Docker version:|docker -v (docker --version)|
|Docker process status - show launched containers:|docker ps|
|Docker process status - show all containers:|docker ps -a|
|Show all images:|docker image ls|
|Show all images:|docker images|
|Docker build in current directory:|docker build -t xxx .|
|Download current image:|docker pull ubuntu|
|Download image with current version:|docker pull ubuntu:18.04|
|Run current image with random name container:|docker run image|
|Run current image with current name container:|docker run --name my-container my-image|
|Show containers:|docker container ls|
|Delete current image without container:|docker rmi image-name|
|Delete current image with container:|docker rmi -f image-name|
|Run container:|docker start my-container|
|Pause container:|docker pause my-container|
|Stop container:|docker stop my-container|
|Stop container (hard):|docker kill my-ubuntu|
|Show count of images, containers and ect:|docker system df|
|Others:|docker-compose up|
|--|docker-compose down|
|--|docker run -it ubuntu|
|--|docker network ls|
|Tag your images:|docker tag shoppingapi:latest shoppingacr.azurecr.io/shoppingapi:v1|
|Tag your images:|docker tag shoppingclient:latest shoppingacr.azurecr.io/shoppingclient:v1|

---

### Azure Portal: 
https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-latest

|--|--|
|--|--|
|Инсталиране на Azure CLI:|az aks install-cli|
|Проверка за инсталация:|az|
|Проверка на версията:|az version|
|Ъпгрейд на версията:|az upgrade|
|Вход в Azure Portal:|az login|
|Create a resource group:|az group create --name myResourceGroup --location westeurope|
|Create an Azure Container Registry:|az acr create --resource-group myResourceGroup --name shoppingacr --sku Basic|
|Enable Admin Account for ACR Pull:|az acr update -n shoppingacr --admin-enabled true|
|Log in to the container registry:|az acr login --name shoppingacr|
|Get the login server address:|az acr list --resource-group myResourceGroup --query "[].{acrLoginServer:loginServer}" --output table|
|Проверка на клъстърите в K8s:|az aks list|
|--|az aks show --resource-group euroins-rg-staging --name euroins-aks-staging --output table|  
|--|az aks show --resource-group euroins-rg-staging --name euroins-aks-staging|
|--|kubectl get pdb -A|

---

### Kubernetes: 
https://kubernetes.io/docs/reference/kubectl/

Start PowerShell

Install kubectl: ...

|--|--|
|--|--|
|Проверка на инсталацията:|kubectl|
|Проверка на версията:|kubectl version|
|Проверка на версията:|kubectl version --short|
|Проверка на версията:|kubectl version --output=yaml|
|Проверка на версията:|kubectl version --output=json|
|Show info for cluster:|kubectl cluster-info|
|Explain namespace:|kubectl describe namespace|
|Show all namespaces:|kubectl get namespaces|
|Show all namespaces:|kubectl get ns|
|Show all services:|kubectl get services|
|--|kubectl describe service <name-service>|
|Explain pods:|kubectl describe pods --namespace kube-system|
|--|kubectl logs <name-pod>|
|Show deployments:|kubectl get deployment|
|--|kubectl rollout restart deploy <name-deploy>|
|Apply .yml file:|kubectl apply -f .\xxx.yml|  
|--|--|
|--|--|
|--|--|
|--|--|  
|--|--|
|--|--|
|--|--|
|--|--|  
|--|--|
|--|--|
|--|--|
|--|--|  
|--|--|
|--|--|
|--|--|
|--|--|  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
