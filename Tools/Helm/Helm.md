# **Helm**

>[1. Links](#links)
>
>[2. Install](#install)
>
>[3. Helm Theory](#helm-theory)
>
>[4. Helm Commands](#helm-commands)
>

---

### **Links**

- https://helm.sh/
- https://artifacthub.io/
- https://helm.sh/docs/helm/

##### [🔼 Back to top](#helm)

---

### **Install**

>**Link installment:** https://helm.sh/docs/intro/install/

|**Commands**						| **Operation System**	| **Terminal**              |
|:--								| :--					| :--                       |
|choco install kubernetes-helm		| Windows				| Administrative PowerShell |
|scoop install helm					| Windows				| Administrative PowerShell |
|sudo snap install helm --classic	| Linux					| -                         |
|brew install helm					| MacOS					| -                         |

##### [🔼 Back to top](#helm)

---

### **Helm Theory**

Helm is a tool for managing Kubernetes packages called charts. Helm can do the following:

- Create new charts from scratch
- Package charts into chart archive (tgz) files
- Interact with chart repositories where charts are stored
- Install and uninstall charts into an existing Kubernetes cluster
- Manage the release cycle of charts that have been installed with Helm

For Helm, there are three important concepts:

- The chart is a bundle of information necessary to create an instance of a Kubernetes application
- The config contains configuration information that can be merged into a packaged chart to create a releasable object
- A release is a running instance of a chart, combined with a specific config

##### [🔼 Back to top](#helm)

---

### **Helm Commands**

|**Commands**				|**Description** |
|:-- 						|:--             |
|helm --help				|                |
|helm version				|                |
|helm list					|                |
|helm repo list			    |                |
|helm version				|                |
|helm repo update			|                |

##### [🔼 Back to top](#helm)

---