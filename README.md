# Commands Documentation 

>[1. Git](#git)
>

### Git:


|--|--|
|--|--|
|```Проверка на данните:```|**git config --list**|
|```Clone repo:```|**git clone https://...**|
|```Clone repo with current branch:```|**git clone -b branch https://...**|
|```Git Initial:```|**git init**|
|```Create file from CLI:```|**touch text.txt**|
|```Create file from CLI:```|**echo This is sample text > MyFile.txt**|
|```Open file from CLI:```|**start .\txt.txt**|
|```Read file from CLI:```|**Get-Content .\txt.txt**|
|```Промяна на съдържанието на файла през конзолата:```|**get-Content .\txt.txt**|
|```Проверка на статуса```|**git status**|
|```Добавяне на всички променени/създадени файлове:```|**git add -A**|
|```Добавяне на всички променени/създадени файлове:```|**git add .**|
|```Добавяне на конкретен файл:```|**git add file.cs**|
|```Създаване на коментар към commit-а:```|**git commit -m "Text" -m "Text"**|
|```Качване на промяната в съответния бранч:```|**git push origin vk-branch**|
|```Check the logs```|**git log**|
|--|**git log -p**|
|--|**git log --stat**|
|--|**git log --pretty**|
|--|**git log --oneline**|
|--|**git shortlog**|
|```Създаване на нов бранч:```|**git branch vk-branch-new**|
|```Създаване на нов бранч и преминаване в него:```|**git checkout -b 'vk-branch-new'**|
|```Преминаване в друг бранч:```|**git checkout vk-branch-new**|
|```Показване на всички бранчове:```|**git branch**|
|```Remove branch:```|**git branch -d vk-branch**|
|--|**git branch -D vk-branch**|
|--|**git push -u origin <vk-branch-new>**|
|--|**git branch -d localBranchName**|
|--|**git branch -D localBranchName**|
|--|**git push origin --delete remoteBranchName**|
|```Show info for current branch:```|**git show origin vk-branch**|
|```Показва всички бранчове, които има в repo-то```|**git branch -av**|
|--|**git branch -v -a**|
|```Create folder with branches```|**git checkout -b 'vk/vk-user-example'**|
|--|**git merge branch**|
|--|**git blame**|
|--|--|
|--|--|
|--|--|
|--|--|
|--|--|
