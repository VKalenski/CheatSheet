### Kind Ingress (ingress.yaml)

---

Convention for naming - only CamelCase is for change:

    NAME                                            EXAMPLE
    SERVICE_NAME.NAMESPACE.svc.cluster.local    -   admin-svc-dev.dev.svc.cluster.local 
    SERVICE_NAME-svc-NAMESPACE                  -   admin-svc-dev
    LABEL_NAME-NAMESPACE                        -   admin-dev
    EXAMPLE_NAME-NAMESPACE                      -   admin-dev
    NAMESPACE                                   -   dev
    HOST                                        -   google.com
    SECRET_NAME-NAMESPACE-tls-secret            -   admin-dev-tls-secret

---

To create/apply ingress in Azure Portal

1. Open Project with VS Code
2. Open Terminal (PowerShell)
3. Set the cluster subscription:
    - ```az account set --subscription 55cbe66a-c5c7-4346-8b22-cfe33157a0b0```
4. Download cluster credentials:
    - az aks get-credentials --resource-group euroins-rg-prod --name euroins-aks-prod
5. Create ingress file in k8s":
    - kubectl create -f ingress-aks-NAMESPACE-FOLDER_NAME/NAMESPACE-ingress-FILE_NAME.yaml -n NAMESPACE
    - kubectl create -f ingress-aks-dev-admin/dev-ingress-admin.yaml -n dev
6. If file is only modified:
    - kubectl apply -f ingress-aks-NAMESPACE-FOLDER_NAME/NAMESPACE-ingress-FILE_NAME.yaml -n NAMESPACE
    - kubectl apply -f ingress-aks-dev-admin/dev-ingress-admin.yaml -n dev
7. Check if ingress is created:
    - kubectl get ingress -n dev
8. Describe for check ingress:
    - kubectl describe ingress SERVICE_NAME-svc-NAMESPACE -n dev
    - kubectl describe ingress admin-svc-dev -n dev
9. Edit ingress if is necessary:
    - kubectl edit ingress SERVICE_NAME-svc-NAMESPACE -n dev
    - kubectl edit ingress admin-svc-dev -n dev

```Good practice is the name of ingress is the same of the name of service!```