# **Minikube**

https://minikube.sigs.k8s.io/docs/
https://github.com/kubernetes/minikube

*Start administrator PowerShell*

|**Commands**                                    | **Description**                     |
|:--                                             | :--                                 |
|``choco install minikube``                      | Windows                             |
|``minikube start``                              | Minikube start                      |
|``minikube start --kubernetes-version=v1.23.0   | Minikube start with current version |
|``minikube status``                             | Minikube status                     |
|``minikube dashboard``                          | Minikube Dashboard                  |
|``minikube ip``                                 | xxx                  |
|``minikube stop``                               | xxx                  |
|``minikube delete``                             | xxx                  |
|``minikube ssh``                                | xxx                  |

Linux
> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))|https://minikube.sigs.k8s.io/docs/start/

---

### **Commands:**

|Commands|Description|
|:--|:--|
|eval $(minikube docker-env)         |Windows|