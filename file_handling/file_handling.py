import json, os


def file_exist(path, file_name):
    if file_name in os.listdir(path): return True
    else:
        return False

def create_file(path, file_name):
    with open(path + os.sep + file_name, "w") as fp:
        pass

def delete_file(path, file_name):
    path = path + os.sep + file_name
    if os.path.exists(path):
        os.remove(path + os.sep + file_name)
        return True
    else:
        return False