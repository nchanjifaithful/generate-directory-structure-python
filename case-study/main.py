import os
import shutil
import itertools # create an iterator from a list


files = open("./data/files.txt")
new_file_list = files.readlines()
new_file_list = [file_name.strip("\n") for file_name in new_file_list]
# print(new_file_list)

# check for the duplicate introductions and add them to a list then an iterator
intro_indices = [index for (index, item) in enumerate(new_file_list) if item == "1- Introduction"]
# print(intro_indices)
intro_indices_iter = itertools.cycle(intro_indices)

# get old file list in input
old_file_list = os.listdir("./input")
# print(old_file_list)

os.chdir("./output")
# print(os.getcwd())

with open(f"../data/folders.txt", "r") as data:
    for file in old_file_list:
        idx = old_file_list.index(file)
        # create a new folder for every introduction
        if new_file_list[idx] == "1- Introduction":
            folder = data.readline()
            folder = folder.strip("\n")
            os.mkdir(folder)
            idx = next(intro_indices_iter)  # fetch each introduction statement consecutively
        new_name = new_file_list[idx] + ".mp4"
        os.rename(f"../input/{file}", new_name)
        shutil.move(f"{new_name}", f"{folder}")
