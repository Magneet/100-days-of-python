import os,glob
files_obj = []
for root, dirs, files in os.walk("d:\\temp"):
    for file in files:
        
        if file.endswith(".csv"):
            files_obj.append(file)

print(files_obj)


