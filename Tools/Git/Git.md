# **Git:**

Start administrator PowerShell and Install GitHub CLI: https://github.com/cli/cli ---> Chocolatey: ```choco install gh```

---

**BASIC commands:**

|**Commands**                           | **Description**            |
|--                                     | --                         |
|gh --version                           | Check GitHub CLI version   |
|gh auth login                          | Login in GitHub account    |
|gh auth status                         | Check the GitHub account   |

---

**CLONE, STATUS, ADD, COMMIT & PUSH commands:**

|**Commands**                           | **Description**                                |
|--                                     | --                                             |
|git init                               | Git Initial                                    |
|git config --list                      | Check the data                                 |
|git clone https://...                  | Clone repo with https//:...                    |
|git clone -b vk-branch https://...     | Clone repo with https//:... current branch     |
|git clone https://...                  | Clone repo with git@ssh//:...                  |
|git clone -b vk-branch https://...     | Clone repo with git@ssh//:... current branch   |
|git status                             | Check git status                               |
|git add .                              | Add all modified/created files                 |
|git add -A                             | Add all modified/created files                 |
|git add file.cs                        | Add current file                               |
|git commit -m "Message"                | Create commit with one message                 |
|git commit -m "Message" -m "Message"   | Create commit with more than one message       |
|git push origin vk-branch              | Push file/s in current branch                  |
|git push -u origin vk-branch           | Push file/s in current branch                  |

---

**SHOW, CREATE, CHECKOUT & DELETE commands:**

|**Commands**                           | **Description**                            |
|--                                     | --                                         |
|git branch                             | Show current branch                        |
|git branch -av                         | Show all origin branches                   |
|git branch -v -a                       | Show all origin branches                   |
|git show origin vk-branch              | Show information for current branch        |
|git branch vk-branch-new               | Create new branch                          |
|git checkout -b 'vk-branch'            | Create and checkout new branch             |
|git checkout -b 'vk/vk-branch'         | Create and checkout folder with branch/es  |
|git checkout vk-branch                 | Checkout in branch                         |
|git branch -M main                     | Rename current branch                      |
|git branch -d vk-branch                | Delete branch                              |
|git branch -D vk-branch                | Delete branch                              |
|git push origin --delete vk-branch     | Delete origin branch                       |

---

**LOGS commands:**

|**Commands**                           | **Description**    |
|--                                     | --                 |
|git log                                | Check the logs     |
|git log -p                             | --                 |
|git log --stat                         | --                 |
|git log --pretty                       | --                 |
|git log --oneline                      | --                 |
|git shortlog                           | --                 |

---

**OTHERS commands:**

|**Commands**                           | **Description**|
|--                                     | --             |
|git merge branch                       | --             |
|git blame                              | --             |
|git reflog                             | --             |
|git reset --soft HEAD~1                | --             |
|git show                               | --             |
|git rebase                             | --             |
