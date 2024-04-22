# **Kubernetes**

https://kubernetes.io/docs/reference/kubectl/

---

### **INSTALL & LOGIN commands:**

|Command|Description|
|-- |--|
|kubectl|                                                                       |Check the installation|
|kubectl version|                                                               |Check the version|
|kubectl version --short|                                                       |Check the version|
|kubectl version --output=yaml|                                                 |Check the version|
|kubectl version --output=json|                                                 |Check the version|
|az aks get-credentials --resource-group myResourceGroup --name myAKSCluster    |Connect to cluster using kubectl|
|kubectl cluster-info                                                           |Show info for cluster|

---

### **GET commands:**

|Command|Description|
|--|--|
|kubectl get namespaces --show-labels                       |Show all namespaces|
|kubectl get ns --show-labels                               |Show all namespaces|
|kubectl get serviceAccounts --show-labels                  |Show all service accounts|
|kubectl get serviceAccounts -n dev --show-labels           |Show all service accounts from current namespace|
|kubectl get nodes --show-labels                            |Show all nodes|
|kubectl get deployment --show-labels                       |Show all deployments|
|kubectl get deployment -n dev --show-labels                |Show all deployments from current namespace|
|kubectl get replicaset --show-labels                       |Show all replica sets|
|kubectl get replicaset -n dev --show-labels                |Show all replica sets from current namespace|
|kubectl get services                                       |Show all services|
|kubectl get svc                                            |Show all services in default namespace|
|kubectl get svc --all-namespaces                           |Show all services in all namespace|
|kubectl get svc -n dev                                     |Show all services from current namespace|
|kubectl get pods                                           |Show all pods|
|kubectl get pods -n dev                                    |Show all pods from current namespace|
|kubectl get pods -n dev -o wide                            |Show all pods from current namespace extend|
|kubectl get pods -n dev -o yaml                            |Show all pods from current namespace extend|
|kubectl get pods -n dev -o json                            |Show all pods from current namespace extend|
|kubectl get pods --all-namespaces                          |Show all pods from all namespace|
|kubectl get pods --all-namespaces -o wide                  |Show all pods from all namespace extend|
|kubectl get pods --watch                                   |Show all pods|
|kubectl get secrets                                        |Show all secrets|
|kubectl get secrets -n dev                                 |Show all secrets in current namespace|
|kubectl get secret default-token-htr5s -n dev              |Show secret/token with current secret name|
|kubectl get secret default-token-htr5s -n dev -o json      |Show secret/token with current secret name extend|
|kubectl get all                                            |Show all in all namespaces|
|kubectl get all -n dev                                     |Show all in current namespace|

kubectl get pods -n stg --field-selector=status.phase=Running
kubectl get pods -n stg --sort-by='.status.containerStatuses[0].restartCount'
kubectl get pv --sort-by=.spec.capacity.storage
kubectl get pdb -A

---

### **DESCRIBE commands:**

|Command|Description|
|--|--|
|kubectl describe namespace                                 |Explain namespace|
|kubectl describe service <name-service>                    |Explain service|
|kubectl describe <pod-name>                                |Explain pod|
|kubectl describe pods --namespace kube-system              |Explain pods|
|kubectl describe node <name-node>                          |Explain nodes|

---

### **LOGS commands:**

|Command|Description|
|--|--|
|kubectl logs <name-deployment>                             ||
|kubectl logs <name-service>                                ||
|kubectl logs <name-pod>                                    ||
|kubectl logs <name-pod> > app.log                          ||
|kubectl logs <name-pod> --previous > app.log               ||
|kubectl logs <name-pod> --previous | sls error > app.log   ||
|kubectl logs <pod-name> -c <container-name>                ||

---

### **DELETE commands:**

|Command|Description|
|--|--|
|kubectl delete deployment <name-deployment> -n dev        |Delete deployment|
|kubectl delete deployment <name-pod> -n dev               |Delete pod|

---

### **OTHERS commands:**

|Command|Description|
|--|--|
|kubectl rollout restart deploy <name-deploy>           |--|
|kubectl apply -f .\xxx.yml                             |Apply .yml file|
|kubectl apply -f .\aks\                                |Deploy microservices to AKS|
|kubectl config get-contexts                            |--|
|kubectl config current-context                         |--|
|kubectl config use-context gcpcluster-k8s-1            |--|
|kubectl delete deployment swn-nginx                    |--|
|kubectl create deployment mongo-depl --image=mongo     |--|
|kubectl exec mongo-depl-5fd6b7d4b4-6xzjd -it sh        |--|
|kubectl top pods -n dev                                |--|

---

kubectl api-resources
kubectl api-resources -o wide
kubectl config view

За достъпване на пода
kubectl -n dev exec --stdin --tty policy-deployment-dev-d47b9957-kmltm -- sh
ls
cat <filename.type> - без това -> cat appsettings.json

ДА се проследи сайта дали работи
tracert https://devssp.eui-api.elando.eu/

За достъпване на редис
kubectl -n dev exec --stdin --tty notifications-deployment-dev-7965cbcbfb-rn8bt -- sh
cat appsettings.json

htop
apt update
apt install htop


---
### [🔼 Back to top](#commands)
---