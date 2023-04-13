import os

folder_structure_dict = {}
sub_folders = []

files = open("F:\\Directories\\test\\data\\files.txt")
files_data = files.readlines()
files_data = [file_name.strip("\n") for file_name in files_data]
print(len(files_data))

# with open(f"F:\\Directories\\test\\data\\folders.txt", "r") as data:
#     for file_name in files_data:
#         print(len(sub_folders))
#         print(file_name)
#         print(file_name == "1- Introduction")
#         if file_name == "1- Introduction":
#             if len(sub_folders) > 0:
#                 folder_structure_dict[folder] = sub_folders
#                 sub_folders = []
#             if len(sub_folders) == 0:
#                 folder = data.readline()
#                 folder = folder.strip("\n")
#                 print(folder)
#         sub_folders.append(file_name)            

with open(f"F:\\Directories\\test\\data\\folders.txt", "r") as data:
    for file_name in files_data:
        file_name_index = files_data.index(file_name)
        if file_name_index == len(files_data) - 1 or files_data[file_name_index + 1] == "1- Introduction":
            folder_structure_dict[folder] = sub_folders
        if file_name == "1- Introduction":
            sub_folders = []
            folder = data.readline()
            folder = folder.strip("\n")
            print(folder)
        sub_folders.append(file_name)        

print(folder_structure_dict)


