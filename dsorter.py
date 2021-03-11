import os
import shutil
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

workingdir = config['DEFAULT']['SortingDirectory']
filestofolders = {}

os.chdir(workingdir)
for extensionsfolder in config['Extensions']:
    filestofolders[extensionsfolder] = tuple(
        config['Extensions'][extensionsfolder].split())
    if not os.path.exists(extensionsfolder):
        os.mkdir(extensionsfolder)

listdir = os.listdir(workingdir)
for fileitem in listdir:
    for item in filestofolders.items():
        if fileitem.lower().endswith(item[1]):
            try:
                shutil.move(os.path.join(workingdir, fileitem),
                            item[0] + "/" + os.path.basename(fileitem))
            except:
                break
