## **Command Line Commands**

>[2. Minikube](#minikube)
>

---
### [🔼 Back to top](#commands)
---

### **Minikube:**

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