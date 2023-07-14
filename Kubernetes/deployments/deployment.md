### Kind Deployment (deployment.yaml)

Convention for naming - only CamelCase is for change:

    NAME                                        EXAMPLE
    DEPLOYMENT_NAME-deployment-NAMESPACE    -   admin-deployment-dev
    APP_NAME-NAMESPACE                      -   admin-dev
    LABEL_NAME-NAMESPACE                    -   admin-dev
    CONTAINER_NAME-NAMESPACE                -   admin-dev
    IMAGE_NAME-NAMESPACE                    -   admin-dev
    NAMESPACE                               -   dev
    CONTAINER_REGISTRY_NAME.azurecr.io      -   euroins.azurecr.io

---

To create/apply deployment in Azure Portal

1. Open Project with VS Code
2. Open Terminal (PowerShell)
3. Login to your azure account:
    - ```az login```
5. Set the cluster subscription:
    - ```az account set --subscription 55cbe66a-c5c7-4346-8b22-cfe33157a0b0```
6. Download cluster credentials:
    - ```az aks get-credentials --resource-group euroins-rg-prod --name euroins-aks-prod```
7. Create deployment file in k8s":
    - ```kubectl create -f Manifests/NAMESPACE/deployment.yaml -n NAMESPACE```
    - ```kubectl create -f Manifests/dev/deployment.yaml -n dev```
8. If deployment file is only modified:
    - ```kubectl apply -f Manifests/NAMESPACE/deployment.yaml -n NAMESPACE```
    - ```kubectl apply -f Manifests/dev/deployment.yaml -n dev```
9. Check if deployment is created:
    - ```kubectl get deployment -n dev```
10. Describe for check deployment:
    - ```kubectl describe deployment SERVICE_NAME-deployment-NAMESPACE -n dev```
    - ```kubectl describe deployment admin-deployment-dev -n dev```
11. Edit deployment if is necessary:
    - ```kubectl edit deployment SERVICE_NAME-deployment-NAMESPACE -n dev```
    - ```kubectl edit deployment admin-deployment-dev -n dev```

---
