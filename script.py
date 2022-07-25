import os
import shutil
from pathlib import Path

download_folder = str(os.path.join(Path.home(), "Downloads"))
videos_folder = str(os.path.join(Path.home(), "Videos"))
pictures_folder = str(os.path.join(Path.home(), "Pictures"))
documents_folder = str(os.path.join(Path.home(), "Documents"))
music_folder = str(os.path.join(Path.home(), "Music"))

dl_folder_files = os.listdir(download_folder)

sorter = {
    "videos":  [],
    "pictures": [],
    "documents": [],
    "music": [],
    "exicutables": [],
    "unknown":  []
}

for file in dl_folder_files:

    filename, tag = os.path.splitext(file)

    if(tag == '.png' or tag == '.svg' or tag == '.ico' or tag == '.jpeg' or tag == '.jpg'):
        sorter["pictures"].append(f'{filename}')
        shutil.move(f'{download_folder}/{file}', pictures_folder)
    elif(tag == '.mov' or tag == '.mp4'):
        sorter["videos"].append(f'{filename}')
        shutil.move(f'{download_folder}/{file}', videos_folder)
    elif(tag == '.pdf' or tag == '.doc' or tag == '.zip' or tag == '.log' or tag == '.psd' or tag == '.rar'):
        sorter["documents"].append(f'{filename}')
        shutil.move(f'{download_folder}/{file}', f'{documents_folder}/Docs')
    elif(tag == '.mp3'):
        sorter["music"].append(f'{filename}')
        shutil.move(f'{download_folder}/{file}', music_folder)
    elif(tag == '.exe' or tag == '.msi'):
        sorter["exicutables"].append(f'{filename}')
        shutil.move(f'{download_folder}/{file}', f'{documents_folder}/Apps')
    else:
        sorter['unknown'].append(f'{filename}')
        shutil.move(f'{download_folder}/{file}', f'{documents_folder}/Unknown')

print(f'script scanned your downloads folder. \n')
print(f'{sorter["documents"].__len__()} documents, {sorter["pictures"].__len__()} pictures and {sorter["music"].__len__()} music files found')
print(
    f'in total, there were {dl_folder_files.__len__()} files moved \n')
