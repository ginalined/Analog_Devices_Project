"""
unit test module
author: Hao Ding
"""
import unittest
from parser import Parser


class ParserTest(unittest.TestCase):
    """
    test the parser class
    """

    def test_directory(self):
        """_summary_
        test different directory input
        """
        parser = Parser("tests", ".txt")
        assert parser.get_all_files()
        parser = Parser("tests/a1", ".txt")
        assert parser.get_all_files()
        parser = Parser(1, ".txt")
        assert parser.get_all_files() is False
        parser = Parser("", ".txt")
        assert parser.get_all_files() is False
        # test non exist dir name
        parser = Parser("tests/fa2", ".txt")
        assert parser.get_all_files() is False

        # test file name
        parser = Parser("tests/fa1.txt", ".txt")
        assert parser.get_all_files() is False

        # test long name
        parser = Parser("tests/../tests", ".txt")
        assert parser.get_all_files()

    def test_result(self):
        """_summary_
        test output correctness
        """
        parser = Parser("tests", ".txt")
        assert parser.get_all_files()
        assert len(parser.files) == 4
        assert len(parser.files) == len(parser.lines)
        assert sum(parser.lines) == 25

        parser = Parser("tests", ".docx")
        assert parser.get_all_files()
        assert len(parser.files) == 1
        assert len(parser.files) == len(parser.lines)
        assert sum(parser.lines) == 4

        parser = Parser("tests", ".png")
        assert parser.get_all_files()
        assert len(parser.files) == 0
        assert len(parser.files) == len(parser.lines)
        assert sum(parser.lines) == 0


if __name__ == "__main__":
    unittest.main()
