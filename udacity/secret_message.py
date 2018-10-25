import os


def rename_files():
    file_list = os.listdir(r"C:\Users\juanj\Documents\PycharmProjects\python-basics\udacity\prank")
    print(file_list)

    saved_path = os.getcwd()
    print("Current working directory: " + saved_path)

    os.chdir(r"C:\Users\juanj\Documents\PycharmProjects\python-basics\udacity\prank")
    translation_table = str.maketrans("0123456789", "          ", "0123456789")
    for f_name in file_list:
        os.rename(f_name, f_name.translate(translation_table))

    os.chdir(saved_path)


rename_files()
