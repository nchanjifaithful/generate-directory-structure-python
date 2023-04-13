import os

for i in range(1, 104):
    new_file = open(f"input/files/Lesson{i}.txt", mode="w")
    new_file.write(f"{i}")