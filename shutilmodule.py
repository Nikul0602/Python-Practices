import shutil

# shutil.copy("main.py", "main1.py")        ## will create another file with same data

# shutil.copytree("Shutil Module", "Shutil")      ## will create another folder with data and files

# shutil.move("Shutil Module/file.txt", "file.txt")       ## will move file from folder to other directory

# shutil.rmtree("Shutil Module")

try:
    path = "file1.txt"
    shutil.rmtree(path)
    print("Removed Successfully")
except:
    print("path Does not exist")