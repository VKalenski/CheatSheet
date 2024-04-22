### Kind Service (service.yaml)

---

Convention for naming - only CamelCase is for change:

    NAME                            EXAMPLE
    SERVICE_NAME-svc-NAMESPACE  -   admin-svc-dev
    LABEL_NAME-NAMESPACE        -   admin-dev
    APP_NAME-NAMESPACE          -   admin-dev
    EXAMPLE_NAME-NAMESPACE      -   admin-dev
    NAMESPACE                   -   dev

---

To create/apply service in Azure Portal

1. Open Project with VS Code
2. Open Terminal (PowerShell)
3. Login to your azure account:
    - ```az login```
4. Set the cluster subscription:
    - ```az account set --subscription 55cbe66a-c5c7-4346-8b22-cfe33157a0b0```
5. Download cluster credentials:
    - ```az aks get-credentials --resource-group euroins-rg-prod --name euroins-aks-prod```
6. Create service file in k8s":
    - ```kubectl create -f Manifests/NAMESPACE/service.yaml -n NAMESPACE```
    - ```kubectl create -f Manifests/dev/service.yaml -n dev```
7. If service file is only modified:
    - ```kubectl apply -f Manifests/NAMESPACE/service.yaml -n NAMESPACE```
    - ```kubectl apply -f Manifests/dev/service.yaml -n dev```
8. Check if service is created:
    - ```kubectl get service -n dev```
9. Describe for check service:
    - ```kubectl describe service SERVICE_NAME-svc-NAMESPACE -n dev```
    - ```kubectl describe service admin-svc-dev -n dev```
10. Edit service if is necessary:
    - ```kubectl edit service SERVICE_NAME-svc-NAMESPACE -n dev```
    - ```kubectl edit service admin-svc-dev -n dev```

---
