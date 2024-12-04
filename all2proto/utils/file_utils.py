import os
from typing import List


def read_file(file_path):
    """
    Read file content
    :param file_path: path to the file
    :return: file content
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')

    with open(file_path, 'r') as f:
        return f.read()


def find_file(file_name, search_paths) -> List[str]:
    """
    Find file in search paths
    :param file_name: file name
    :param search_paths: list of paths to search
    :return: list of possible file full paths
    """
    paths = []
    for path in search_paths:
        # 获取一个路径的绝对路径
        abs_path = os.path.abspath(path)
        full_path = os.path.join(abs_path, file_name)
        if os.path.exists(full_path):
            paths.append(str(full_path))

    return paths
