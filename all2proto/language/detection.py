from enum import Enum
import os


class Language(Enum):
    PLAIN_TEXT = -1
    CPP = 0


class LanguageDetector:
    """
    Detects the language of a file based on its extension.
    """
    cpp_ext = ['.cpp', '.cc', '.h', '.hpp', '.hh']

    @staticmethod
    def detect(file_path):
        """
        Detect the language of the file.
        :return: Language
        """
        _, extension = os.path.splitext(file_path)
        if extension in LanguageDetector.cpp_ext:
            return Language.CPP
        else:
            return Language.PLAIN_TEXT
