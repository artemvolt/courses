from tokenize import String
import os


def find_files_in_folders(dir_path: String):
    """Получение всех файлов из папки"""
    abs_path = os.path.abspath(dir_path)
    if not os.path.isdir(
            os.path.abspath(dir_path)
    ):
        raise NotADirectoryError("this isn't directory path")

    files = []
    for item in os.listdir(dir_path):
        abs_path_with_item = abs_path + "/" + item

        if os.path.isfile(abs_path_with_item):
            files.append(abs_path_with_item)

        if os.path.isdir(abs_path_with_item):
            files = files + find_files_in_folders(abs_path_with_item)

    return files
