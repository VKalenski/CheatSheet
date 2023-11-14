### Setup Computer

1. .NET 6 SDK (free)
2. GitHub Desktop (free):           https://desktop.github.com/
3. Visual Studio Community (free):  https://visualstudio.microsoft.com/downloads/
4. Visual Studio Code (free):       https://code.visualstudio.com/download/
5. Web Browser or API Client:
    - Postman  (free):              https://www.postman.com/downloads/
    - Insomnia (free):              https://insomnia.21rest/download/
6. pgAdmin (free):                  https://www.pgadmin.org/download/
7. Docker (free):                   https://www.docker.com/products/docker-desktop/\
8. Helm (free):                     https://github.com/helm/helm/releases/
9. JMeter (free):                   https://jmeter.apache.org/download_jmeter.cgi/



---

## **Chocolatey**

**Setup Packages in Administrator PowerShell:**

Install Chocolatey: https://community.chocolatey.org/

|||||
|--|--|--|--|
|x. |Base64 encoder/decoder:  |choco install base64            |https://community.chocolatey.org/packages/base64|
|x. |cURL:                    |choco install curl              |https://community.chocolatey.org/packages/curl|
|x. |acme.sh:                 |choco install acme-sh           |https://community.chocolatey.org/packages/acme-sh|
|x. |GNU grep:                |choco install grep              |https://community.chocolatey.org/packages/grep|
|x. |Kubernetes CLI:          |choco install kubernetes-cli    |https://community.chocolatey.org/packages/kubernetes-cli|
|x. |Minikube                 |choco install minikube          |https://community.chocolatey.org/packages/Minikube|
|x. |kui:                     |choco install kui               |https://community.chocolatey.org/packages/kui|
|x. |kubescape                |choco install kubescape         |https://community.chocolatey.org/packages/kubescape|
|x. |k9s                      |choco install k9s               |https://community.chocolatey.org/packages/k9s|
|x. |kubeval                  |choco install kubeval           |https://community.chocolatey.org/packages/kubeval|
|x. |kubeconform              |winget install YannHamon.kubeconform||
|x. |terraform                |choco install -y terraform      |https://community.chocolatey.org/packages/terraform|
|x. |civo                     |choco install -y civo-cli       |https://community.chocolatey.org/packages/civo-cli|


## **Scoop**

**Setup Packages in PowerShell:**

Install Scoop: iwr -useb get.scoop.sh | iex

x. civo                     scoop install civo

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

---

### Theory

---

CLI     -   Command Line Interface
CMD     -   Command Prompt
API     -   Application Programming Interface
JSON    -   JavaScript Object Notation (Текстово базиран отворен стандарт)
XML     -   Extensible Markup Language
DI      -   Dependency Injection (Внедрени зависимост)
CI/CD   -   Continuous Integration / Continuous Delivery
DTO     -   Data Transfer Objects
CSV     -   Comma-Separated Values
K8s     -   Kubernetes
SSL     -   Secure Sockets Layer
TLS     -   Transport Layer Security
IDE     -   Integrated Development Environment
IaC     -   Infrastructure as Code
SDLC    -   Software Development Life Cycle
BDD     -   Behavior-driven development
FCL     -   Framework Class Library
CLR     -   Common Language Runtime
ASDF    -   Advanced Scientific Data Format


ASP.NET - web application framework which was released as part of the .NET framework.
ASP.NET Core - cross-platform, high-performance and open-source web application framework. First version: 2016




CI is used during the build and test phase. CD is used once changes are committed.




SAST - Static Application Security Testing
DAST
SCA
OWASP
CIS
CISA
OWASP ZAP
OWASP ASVS
CVSS
SSH
SDLC - Software Development Life Cycle

DLL - Dynamic Link Library