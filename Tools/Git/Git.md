## **Command Line Commands**

>[1. Git](#git)
>

---
### [🔼 Back to top](#commands)
---

### **Git:**

Start administrator PowerShell and Install GitHub CLI: https://github.com/cli/cli ---> Chocolatey: ```choco install gh```

---

Table for ```BASIC``` commands:

|Description|Commands|
|--|--|
|Check GitHub CLI version:                        |gh --version|
|Login in GitHub account:                         |gh auth login|

---

Table for ```CLONE```, ```STATUS```, ```ADD```, ```COMMIT``` and ```PUSH``` git files commands:

|Description|Commands|
|--|--|
|Git Initial:                                     |git init|
|Check the data:                                  |git config --list|
|Clone repo with https//:...                      |git clone https://...|
|Clone repo with https//:... current branch:      |git clone -b vk-branch https://...|
|Clone repo with git@ssh//:...                    |git clone https://...|
|Clone repo with git@ssh//:... current branch:    |git clone -b vk-branch https://...|
|Check git status:                                |git status|
|Add all modified/created files:                  |git add .|
|Add all modified/created files:                  |git add -A|
|Add current file:                                |git add file.cs|
|Create commit with one message:                  |git commit -m "Message"|
|Create commit with more than one message:        |git commit -m "Message" -m "Message"|
|Push file/s in current branch:                   |git push origin vk-branch|
|Push file/s in current branch:                   |git push -u origin vk-branch|

---

Table for ```SHOW```, ```CREATE```, ```CHECKOUT``` and ```DELETE``` branches commands:

|Description|Commands|
|--|--|
|Show current branch:                             |git branch|
|Show all origin branches:                        |git branch -av|
|Show all origin branches:                        |git branch -v -a|
|Show information for current branch:             |git show origin vk-branch|
|Create new branch:                               |git branch vk-branch-new|
|Create and checkout new branch:                  |git checkout -b 'vk-branch'|
|Create and checkout folder with branch/es:       |git checkout -b 'vk/vk-branch'|
|Checkout in branch:                              |git checkout vk-branch|
|Rename current branch:                           |git branch -M main|
|Delete branch:                                   |git branch -d vk-branch|
|Delete branch:                                   |git branch -D vk-branch|
|Delete origin branch:                            |git push origin --delete vk-branch|

---

Table for ```LOG``` commands:

|Description|Commands|
|--|--|
|Check the logs:                  |git log|
|--                               |git log -p|
|--                               |git log --stat|
|--                               |git log --pretty|
|--                               |git log --oneline|
|--                               |git shortlog|

---

|Description|Commands|
|--|--|
|--|git merge branch|
|--|git blame|


git reflog

git reset --soft HEAD~1


git show

git rebase

---
### [🔼 Back to top](#commands)
---