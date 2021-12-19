import sys

from core import create_file, create_folder, get_list, delete_file, copy_file, save_log


command = sys.argv[1]

save_log("completed {} with params: {}".format(command, sys.argv))
if command == 'ls':
    get_list()
elif command == 'create_file':
    name = sys.argv[2]
    create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except:
        print('You have forgotten the second parameter')
    else:
        create_folder(name)
elif command == "delete":
    name = sys.argv[2]
    delete_file(name)
elif command == 'copy':
    name = sys.argv[2]
    new_name = sys.argv[3]
    copy_file(name, new_name)
elif command == 'help':
    print("help to print help)))")
    print("create_file - to create a file")
    print("create_folder - to create a folder")
    print("delete - to delete a file or a folder")
    print("copy - to copy a file or a folder")


save_log('end')