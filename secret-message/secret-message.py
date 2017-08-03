import os

def rename_files():
    file_list = os.listdir(r"images")
    saved_path = os.getcwd()
    os.chdir(r"images")

    for file in file_list:
        new_name = file.translate(None, "0123456789")
        os.rename(file, new_name)

    os.chdir(saved_path)

rename_files()