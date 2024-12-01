from abc import abstractmethod
from typing import List, Tuple


class SourceFile:
    """
    Class for storing parsing results of single file
    """

    class Class:
        """
        Class for storing class information
        """

        def __init__(self, name: str, package: str, methods: List[str],
                     fields: List[Tuple[str, str]]):
            """
            :param name: class name
            :param package: package name (In C++ it is namespace)
            :param methods: list of method names
            :param fields: list of tuples with field name and type
            """
            self.name = name
            self.package = package
            self.methods = methods
            self.fields = fields

    class Imports:
        """
        Class for storing imported files
        """

        def __init__(self, imports: List[str]):
            """
            :param imports: list of imported files
            """
            self.imports = imports

    def __init__(self, classes: List[Class], imports: Imports):
        """
        :param classes: list of classes
        :param imports: list of imported files
        """
        self.classes = classes
        self.imports = imports


class SourceParser:
    """
    Abstract class for parsers
    """

    def __init__(self, source_file):
        """
        :param source_file:
        """
        self.source_file = source_file

    @abstractmethod
    def parse(self):
        raise NotImplementedError("Method parse not implemented")
