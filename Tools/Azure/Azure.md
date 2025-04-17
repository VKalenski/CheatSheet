# **Azure**

https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli

Start PowerShell

---

### **INSTALL, UPDATE & LOGIN commands:**

|Commands                                                                                                    | Description                        |
|--                                                                                                          | --                                 |
|az aks install-cli                                                                                          | Install Azure CLI:                 |
|az                                                                                                          | Проверка за инсталация:            |
|az version                                                                                                  | Проверка на версията:              |
|az upgrade                                                                                                  | Ъпгрейд на версията:               |
|az login                                                                                                    | Log in Azure Portal:               |
|az acr login --name myNameOfAcr                                                                             | Log in to the container registry:  |
|az aks get-upgrades --name euroins-aks-staging --resource-group euroins-rg-staging                          |                                    |
|az aks upgrade --kubernetes-version 1.24.9 --name euroins-aks-staging --resource-group euroins-rg-staging   |                                    |
|az aks nodepool upgrade --cluster-name euroins-aks-staging -g euroins-rg-staging -n agentpool               |                                    |
|az aks upgrade --resource-group euroins-rg-staging --name euroins-aks-staging --kubernetes-version 1.24.9   |                                    |
|az aks get-upgrades --resource-group myResourceGroup --name myAKSCluster --output table                     |                                    |

---

### **CREATE commands:**

|Commands                                                                                                                      | Description                           |
|--                                                                                                                            | --                                    |
|az group create --name myResourceGroup --location westeurope                                                                  | Create a resource group:              |
|az acr create --resource-group myResourceGroup --name shoppingacr --sku Basic                                                 | Create an Azure Container Registry:   |
|az aks create --resource-group myResourceGroup --name myAKSCluster --node-count 1 --generate-ssh-keys --attach-acr myNameOfAcr| Create AKS cluster with ACR:          |

---

### **OTHERS commands:**

|Commands                                                                                              | Description                               |
|--                                                                                                    | :--                                       |
|az acr update -n shoppingacr --admin-enabled true                                                     | Enable Admin Account for ACR Pull:        |
|az acr list --resource-group myResourceGroup --query "[].{acrLoginServer:loginServer}" --output table | Get the login server address:             |
|az acr repository list --name shoppingacr --output table                                              | List images in registry:                  |
|az acr repository show-tags --name shoppingacr --repository shoppingclient --output table             | See tags                                  |
|az aks list                                                                                           | Проверка на клъстърите в K8s:             |
|az aks show --resource-group euroins-rg-staging --name euroins-aks-staging --output table             | --                                        |
|az aks show --resource-group euroins-rg-staging --name euroins-aks-staging                            | --                                        |
|az group delete --name myResourceGroup --yes --no-wait                                                | Clean All AKS and Azure Resources:        |
|kubectl get pdb -A                                                                                    | --                                        |
|az account set --subscription 69a94853-fcae-446b-917c-2bd00ba3e3ea                                    |                                           |
|az aks get-credentials --resource-group cloud-shell-storage-westeurope --name vk-aks-dev              |                                           |
|az aks get-credentials --admin --name MyManagedCluster --resource-group MyResourceGroup               |                                           |
|az aks show --resource-group euroins-rg-staging --name euroins-aks-staging --output table             |                                           |
|az aks show --resource-group euroins-rg-staging --name euroins-aks-staging                            |                                           |
|kubectl get pdb -A                                                                                    |                                           |


az aks upgrade --resource-group euroins-rg-staging --name euroins-aks-staging --kubernetes-version 1.24.9

az aks show --resource-group euroins-rg-staging --name euroins-aks-staging

az aks get-upgrades --resource-group myResourceGroup --name myAKSCluster --output table

az aks show --resource-group euroins-rg-staging --name euroins-aks-staging --output table

az aks upgrade --kubernetes-version 1.24.9 --name euroins-aks-staging --resource-group euroins-rg-staging

az aks install-cli
		az aks list

az aks get-credentials --admin --name MyManagedCluster --resource-group MyResourceGroup


az monitor log-analytics workspace table list --resource-group euroins-rg-staging --workspace-name euroins --output table
