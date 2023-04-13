import os
import shutil


files = open("./input/files.txt")
new_file_list = files.readlines()
new_file_list = [file_name.strip("\n") for file_name in new_file_list]
# print(new_file_list)

os.chdir("input/files")
# print(os.getcwd())

old_file_list = os.listdir()

os.chdir("../../output")
print(os.getcwd())

with open(f"../input/folders.txt", "r") as data:
    for file in old_file_list:
        idx = old_file_list.index(file)
        new_name = new_file_list[idx] + ".mp4"
        if new_name == "1- Introduction.mp4":
            sub_folders = []
            folder = data.readline()
            folder = folder.strip("\n")
            os.mkdir(folder)
        os.rename(f"../input/files/{file}", new_name)
        shutil.move(f"{new_name}", f"{folder}")    