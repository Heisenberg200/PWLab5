import os

cur_dir = os.getcwd()
# print(cur_dir)
path = os.getcwd() + '/rename_folder'
list_files = os.listdir(path)
# print(list_files)
for file in list_files:
    # print(file)
    file_name = file.split('] ')
    print(file_name[0], '\n', file_name[1])
    os.rename(os.path.join(path,file), os.path.join(path,file_name[1]))
    # print(file)