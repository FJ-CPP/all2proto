from typing import List, Tuple

from .parsers import CppSourceParser


class All2Proto:
    """
    Class for converting data structures into proto files
    """

    def __init__(self, targets: List[Tuple[str, str]], search_paths: List[str]):
        """
        :param targets: list of classes and their packages
        :param search_paths: list of paths to find dependencies
        """
        self.targets = targets
        self.search_paths = search_paths

    def convert2proto(self, output_path: str):
        """
        Convert classes into proto files
        """
        for class_name, package in self.targets:
            pass

        raise NotImplementedError