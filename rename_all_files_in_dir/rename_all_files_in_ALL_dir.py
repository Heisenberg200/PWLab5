# переименовать файлы отбросив в именах всех фалов всех папок
# [......] вначале имени файла
#
import os

path = os.getcwd() + '/rename_folder'
list_files = os.listdir(path)

for x in list_files:
    sub_dir = os.path.join(path, x)
    if os.path.isdir(sub_dir):
        list_files_in_subdir = os.listdir(sub_dir)

        for file in list_files_in_subdir:
            file_name = file.split('] ')
            os.rename(os.path.join(sub_dir,file), os.path.join(sub_dir,file_name[1]))
