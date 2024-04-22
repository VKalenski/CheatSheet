## **Command Line Commands**

>[7. PowerShell](#powershell)
>
>[8. Linux](#linux)
>

---
### [🔼 Back to top](#commands)

---

### **PowerShell:**

Start PowerShell

Table for ```CHANGE``` commands:

|Description|Command|
|--|--|
|Change kubectl to k command:                   |Set-Alias -Name k -Value kubectl|
|Change docker to d command:                    |Set-Alias -Name d -Value docker|

---
### [🔼 Back to top](#commands)
---

### **Linux:**

Table for ```CHANGE``` commands:

|Description|Command|
|--|--|
|Change kubectl to k command:                   |alias k='kubectl'|
|Change kubectl get pods to d command:          |alias kgp='kubectl get pods'|

---

|Create file from CLI:|touch text.txt|
|Create file from CLI:|echo This is sample text > MyFile.txt|
|Open file from CLI:|start .\txt.txt|
|Read file from CLI:|Get-Content .\txt.txt|
|Промяна на съдържанието на файла през конзолата:|get-Content .\txt.txt|
||node --version|
||cd xx* - само част от името|
||az acr repository list -n euroins|
||code -r ConsoleName|
az acr repository show --name euroins --repository vehicleservice
az acr repository list -n euroins
