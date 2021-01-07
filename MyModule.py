import os
from pathlib import Path
import shortuuid


class ManagePath():
    def __init__(self):
        try:
            module_path = os.path.abspath(__file__)
            print(module_path)
        except Exception as ex:
            print(ex)

    def create_tmp_folder(self, filePath):
        try:
            Path(str(filePath)).mkdir(parents=True, exist_ok=True)
            print(filePath)
        except Exception as ex:
            print("Create Tmp", ex)

    def create_file(self, file_path_with_name):
        try:
            print(file_path_with_name)
            Path(file_path_with_name).touch()
        except Exception as ex:
            print(f'{file_path_with_name}Create file', ex)

    def write_text(self, file_path, text):

        if Path(file_path).exists():
            file = Path(file_path)
            file.write_text(text)

    def append_text(self, file_path, text):

        if Path(file_path).exists():
            try:
                f = Path(file_path).open('a')
                f.write(text)
                f.close()
            except Exception as ex:
                print(ex)

    def read_text(self, file_path):
        file = Path(file_path)
        return file.read_text()


def generate_user_info():

    user_id = shortuuid.ShortUUID().random(length=6)
    user_link = shortuuid.ShortUUID().random(length=18)
    return user_id, user_link


def note_exist(file_path):
    file = Path(file_path)
    return file.is_dir()
