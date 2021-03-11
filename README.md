# downloads-sorter
## Description
Simple script that helps to organize downloads folder. I use this script executed every hour from a batch file scheduled in Windows Task Scheduler.
## How to use
1. Configure directories and folder names in **config.ini**:
```
[DEFAULT]
sortingdirectory = your\downloads\folder\path
[Extensions]
.pics = .png .jpg .jpeg .bmp
.vids = .mp4 .avi .mkv .mov
```
Folders are defined in following form:
```
folder_name = .extension1 .extension2 .extension3
```
2. Start sorting:
```
python dsorter.py
```
