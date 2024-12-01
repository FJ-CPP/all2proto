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

    class Import:
        """
        Class for storing imported files
        """

        def __init__(self, path, content):
            """
            :param path: path to the file
            :param content: imported content, like specific classes or functions, or `*` for all, etc
            """
            self.path = path
            self.content = content

    def __init__(self, path, classes: List[Class], imports: List[Import]):
        """
        :param path: path to the file
        :param classes: list of classes
        :param imports: list of imported files
        """
        self.path = path
        self.classes = classes
        self.imports = imports


class SourceGraph:
    """
    Class for storing parsing results of multiple files
    """

    def __init__(self, source_files: List[SourceFile]):
        """
        :param source_files: list of SourceFile objects
        """
        self.source_files = source_files

    def get_graph(self):
        """
        Get the graph of the source files.

        The graph will be like:

            {
                'A': ['B', 'C'],
                'C': ['D', 'E', 'F']
            }

        which indicates that file A imports B and C, and file C imports D, E, and F.
        The elements in the graph include path and referred content.
        """

        graph = {}
        for src in self.source_files:
            graph[src.path] = [(imp.path, imp.content) for imp in src.imports]

        return graph


class SourceParser:
    """
    Abstract class for parsers
    """

    def __init__(self, source_files: List[str], search_paths: List[str]):
        """
        :param source_files: list of source files
        :param search_paths: list of paths to search for dependencies
        """
        self.source_files = source_files
        self.search_paths = search_paths

    @abstractmethod
    def parse(self) -> SourceGraph:
        raise NotImplementedError("Method not implemented")
