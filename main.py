import sys
import os

from core import create_file, create_folder, get_list, delete_file, copy_file, save_log, save_cd, get_cd


def get_params_list(nums, this_command=''):
    res = sys.argv[2: nums + 2]
    if res:
        return res
    else:
        print(f"not enough arguments for the command -  \"{this_command}\" ")

        exit()


command = []
try:
    command = sys.argv[1]
except IndexError:
    exit()

cd = get_cd()
if cd != "File Not found":
    os.chdir(cd)

if command == 'ls':
    get_list()
    get_cd(1)
elif command == 'cd':
    params = get_params_list(1)
    save_cd(params[0])
elif command == 'cd_reset':
    save_cd(reset_dir=True)
elif command == 'create_file':
    params_list = get_params_list(2, 'create_file')
    create_file(params_list[0])
elif command == 'create_folder':
    params_list = get_params_list(2, command)
    create_folder(params_list[0])
elif command == "delete":
    params_list = get_params_list(2, command)
    delete_file(params_list[0])
elif command == 'copy':
    params_list = get_params_list(2, command)
    copy_file(params_list[0], params_list[1])
elif command == 'help':
    print("help to print help)))")
    print("create_file - to create a file")
    print("create_folder - to create a folder")
    print("delete - to delete a file or a folder")
    print("copy - to copy a file or a folder")

else:  # ---COMMAND DOESN'T EXIST---
    exit("this command doesn't exist")

save_log("completed {} with params: {}".format(command, sys.argv))
