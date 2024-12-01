from .parser import SourceParser

import CppHeaderParser


class CppSourceParser(SourceParser):
    """
    Class for parsing C++ source files
    """

    def __init__(self, source_file):
        super().__init__(source_file)

    def parse(self):
        """
        Parse C++ source file
        """
        pass
