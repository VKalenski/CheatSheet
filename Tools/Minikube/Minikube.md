# **Minikube**

*Start administrator PowerShell*

|Commands|Description|
|:--|:--|
|choco install minikube         |Windows|
|minikube start                 |Minikube start|
|minikube status                |Minikube status|
|minikube dashboard             |Minikube Dashboard|

Linux
> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))|https://minikube.sigs.k8s.io/docs/start/
