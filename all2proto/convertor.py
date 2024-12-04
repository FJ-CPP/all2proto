from typing import List, Tuple

from .parsers import CppSourceParser
from .utils import find_file


class TargetSplitter:
    """
    Class for splitting target into class name and package
    """
    SCOPE_SPECIFIER = "::"

    def __init__(self, target: str):
        """
        :param target: target to split
        """
        self.target = target

    def split(self) -> Tuple[List[str], str, str]:
        """
        Split target into class and package
        :return: list of class scope; class name; package
        """
        pkg, cls = self.target.split(TargetSplitter.SCOPE_SPECIFIER, 1)
        if cls.find(TargetSplitter.SCOPE_SPECIFIER) != -1:
            cls_scope, cls_name = cls.rsplit("::", 1)
            cls_scope = cls_scope.split("::")
        else:
            cls_scope = [""]
            cls_name = cls

        print(
            f"[TargetSplitter::split] Splitting target: {self.target} into "
            f"class scope: {cls_scope}, class name: {cls_name}, package: {pkg}")
        return cls_scope, cls_name, pkg


class All2Proto:
    """
    Class for converting data structures into proto files
    """

    def __init__(self, targets: List[str], search_paths: List[str]):
        """
        :param targets: list of classes and their packages
        :param search_paths: list of paths to find dependencies
        """
        self.targets = targets
        self.search_paths = search_paths

    def convert2proto(self) -> List[Tuple[str, str]]:
        """
        Convert classes into proto files
        :return: list of tuples of class name and generated proto
        """
        for target in self.targets:
            spliter = TargetSplitter(target)
            cls_scope, cls_name, pkg = spliter.split()
            # TODO: split cls if nested

            pkg_paths = find_file(pkg, self.search_paths)
            print(
                f"[All2Proto::convert2proto] Found {pkg_paths} for package {pkg}"
            )

            for pkg_path in pkg_paths:
                parser = CppSourceParser(pkg_path, self.search_paths)
                src_graph = parser.parse()

        return []
