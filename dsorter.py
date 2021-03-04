import os
import shutil

filestofolders = {
    '.pics': ('.png', '.jpg', '.jpeg', '.bmp'),
    '.vids': ('.mkv', '.mp4', '.avi', '.mov'),
    '.trash': ('.torrent'),
    '.archives': ('.7z', '.rar', '.zip'),
    '.apps': ('.exe'),
    '.docs': ('.doc', '.docx', '.pdf'),
    '.audio': ('.mp3', '.m4a', '.wav')
    }
workingdir = r'D:\_Downloads'

os.chdir(workingdir)
for key in filestofolders.keys():
    if not os.path.exists(key):
        os.mkdir(key)

listdir = os.listdir(workingdir)
for fileitem in listdir:
    for item in filestofolders.items():
        if fileitem.lower().endswith(item[1]):
            try:
                shutil.move(os.path.join(workingdir, fileitem), item[0] + "/" + os.path.basename(fileitem))
            except:
                break

                