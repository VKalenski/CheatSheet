## **Command Line Commands**

>[6. Kubernetes (K8s)](#kubernetes)
>

---
### [🔼 Back to top](#commands)
---

### **Kubernetes:**
https://kubernetes.io/docs/reference/kubectl/

Start PowerShell

Table for ```INSTALL``` and ```LOGIN``` commands:

|Description|Command|
|--|--|
|Проверка на инсталацията:                      |kubectl|
|Проверка на версията:                          |kubectl version|
|Проверка на версията:                          |kubectl version --short|
|Проверка на версията:                          |kubectl version --output=yaml|
|Проверка на версията:                          |kubectl version --output=json|
|Connect to cluster using kubectl:              |az aks get-credentials --resource-group myResourceGroup --name myAKSCluster|
|Show info for cluster:                         |kubectl cluster-info|

---

Table for ```GET``` commands:

|Description|Command|
|--|--|
|Show all namespaces:                               |kubectl get namespaces|
|Show all namespaces:                               |kubectl get ns|
|Show all service accounts:                         |kubectl get serviceAccounts|
|Show all service accounts from current namespace:  |kubectl get serviceAccounts -n dev|
|Show all nodes:                                    |kubectl get nodes|
|Show all deployments:                              |kubectl get deployment|
|Show all deployments from current namespace:       |kubectl get deployment -n dev|
|Show all replicasets:                              |kubectl get replicaset|
|Show all replicasets from current namespace:       |kubectl get replicaset -n dev|
|Show all services:                                 |kubectl get services|
|Show all services:                                 |kubectl get svc|
|Show all services from current namespace:          |kubectl get svc -n dev|
|Show all pods:                                     |kubectl get pods|
|Show all pods from current namespace:              |kubectl get pods -n dev|
|Show all pods from current namespace extend:       |kubectl get pods -n dev -o wide|
|Show all pods from all namespace:                  |kubectl get pods --all-namespaces|
|Show all pods from all namespace extend:           |kubectl get pods --all-namespaces -o wide|
|Show all pods:                                     |kubectl get pods --watch|
|Show all secrets:                                  |kubectl get secrets|
|Show all secrets in current namespace:             |kubectl get secrets -n dev|
|Show secret/token with current secret name:        |kubectl get secret default-token-htr5s -n dev|
|Show secret/token with current secret name extend: |kubectl get secret default-token-htr5s -n dev -o json|
|Show all in all namespaces:                        |kubectl get all|
|Show all in current namespace:                     |kubectl get all -n dev|

---

Table for ```DESCRIBE``` commands:

|Description|Command|
|--|--|
|Explain namespace:                             |kubectl describe namespace|
|Explain service:                               |kubectl describe service <name-service>|
|Explain pod:                                   |kubectl describe <pod-name>|
|Explain pods:                                  |kubectl describe pods --namespace kube-system|

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
||kubectl top pods -n dev|

---
### [🔼 Back to top](#commands)
---