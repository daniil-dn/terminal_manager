import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('The folder already exists.')


def get_list(folders_only=False):
    res = os.listdir()
    if folders_only:
        res = [f for f in res if os.path.isdir(f)]

    print(res if res else 'The current directory is empty')


def delete_file(name):
    os.rmdir(name) if os.path.isdir(name) \
        else os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print("The file already exists.")
    else:
        shutil.copy(name, new_name)


def save_log(message):
    current_time = datetime.datetime.now()
    res = f"{current_time} - {message}"
    with open(f'{os.path.dirname(__file__)}/log.txt', 'a', encoding="utf-8") as f:
        f.write(res + '\n')
    print(res)


def save_cd(path='', reset_dir=False):
    if reset_dir is True:
        os.chdir(os.path.dirname(__file__))
        with open(f'{os.path.dirname(__file__)}/cur_dir.data', 'w', encoding='utf-8') as f:
            f.write(os.getcwd())
    elif reset_dir is False and path is not False:
        # just save new path
        try:
            os.chdir(path)
        except FileNotFoundError:
            exit("ERROR:\n\tThe new path is invalid!")
        with open(f'{os.path.dirname(__file__)}/cur_dir.data', 'w', encoding='utf-8') as f:
            f.write(os.getcwd())
    else:
        exit('the new path is empty')


def get_cd(printing=False):
    with open(f'{os.path.dirname(__file__)}/cur_dir.data', 'r', encoding='utf-8') as f:
        res = f.read()
        if printing:
            print("\n --The current dir is {}\n".format(res))
        return res


if __name__ == '__main__':
    pass
# TODO MAKE a function for repetitive actions - in get_cd, save_cd
