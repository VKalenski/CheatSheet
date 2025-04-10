### Setup Computer

|N  | **Commands**                    | **Links**                                               |
|:--|                                 | :--                                                     |
|x. | .NET 6.0 SDK (free)             | https://dotnet.microsoft.com/en-us/download/dotnet/6.0  |
|x. | .NET 8.0 SDK (free)             | https://dotnet.microsoft.com/en-us/download/dotnet/8.0  |
|x. | .NET 9.0 SDK (free)             | https://dotnet.microsoft.com/en-us/download/dotnet/9.0  |
|x. | GitHub Desktop (free)           | https://desktop.github.com/                             |
|x. | Visual Studio Community (free)  | https://visualstudio.microsoft.com/downloads/           |
|x. | Visual Studio Code (free)       | https://code.visualstudio.com/download/                 |
|x  | Api Client Postman (free)       | https://www.postman.com/downloads/                      |
|x  | Api Client Insomnia (free)      | https://insomnia.21rest/download/                       |
|x. | pgAdmin (free)                  | https://www.pgadmin.org/download/                       |
|x. | Docker (free)                   | https://www.docker.com/products/docker-desktop/         |
|x. | Helm (free)                     | https://github.com/helm/helm/releases/                  |
|x. | Headlamp (free)                 | https://headlamp.dev/                                   |
|x. | JMeter (free)                   | https://jmeter.apache.org/download_jmeter.cgi/          |
|x. | WinMerge (free)                 | https://winmerge.org/                                   |

---

## **Chocolatey**

**Setup Packages in Administrator PowerShell:**

Open **Administator** Terminal
**Install Chocolatey:** https://community.chocolatey.org/

|N  | **Commands**                 | **Command**                        | **Links**                                                 |
|-- | :--                          | :--                                | :--                                                       |
|x. | **acme.sh**                  | choco install -y acme-sh           | https://community.chocolatey.org/packages/acme-sh         |
|x. | **Base64 encoder/decoder**   | choco install -y base64            | https://community.chocolatey.org/packages/base64          |
|x. | **civo**                     | choco install -y civo-cli          | https://community.chocolatey.org/packages/civo-cli        |
|x. | **GitHub CLI**               | choco install -y gh                | https://community.chocolatey.org/packages/gh              |
|x. | **GNU grep**                 | choco install -y grep              | https://community.chocolatey.org/packages/grep            |
|x. | **Kubernetes CLI**           | choco install -y kubernetes-cli    | https://community.chocolatey.org/packages/kubernetes-cli  |
|x. | **Kubernetes HELM CLI**      | choco install -y kubernetes-helm   | https://community.chocolatey.org/packages/kubernetes-helm |
|x. | **kubescape**                | choco install -y kubescape         | https://community.chocolatey.org/packages/kubescape       |
|x. | **k9s**                      | choco install -y k9s               | https://community.chocolatey.org/packages/k9s             |
|x. | **kubeval**                  | choco install -y kubeval           | https://community.chocolatey.org/packages/kubeval         |
|x. | **Minikube**                 | choco install -y minikube          | https://community.chocolatey.org/packages/Minikube        |
|x. | **terraform**                | choco install -y terraform         | https://community.chocolatey.org/packages/terraform       |
|x. | **kui**                      | choco install -y kui               | https://community.chocolatey.org/packages/kui             |
|x. | **cURL**                     | choco install -y curl              | https://community.chocolatey.org/packages/curl            |

---

## **Scoop**

**Setup Packages in PowerShell:**

**Install Scoop:** iwr -useb get.scoop.sh | iex

x. civo                     scoop install civo
|x. |kubeconform              |winget install -y YannHamon.kubeconform||

---

### **Setup Packages in Ubuntu 22:**

x. Kubernetes CLI:
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

https://pwittrock.github.io/docs/tasks/tools/install-kubectl/

x. Krew

(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)

https://krew.sigs.k8s.io/docs/user-guide/setup/install/#bash
