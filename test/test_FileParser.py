import unittest
from FileParser import FileParser

class FileParserTest(unittest.TestCase):
    def test_something(self):
        _file: str = '../data/all_hour.csv'
        data = FileParser.Read4File(_file)
        self.assertIsNotNone(data)
        print(data)


if __name__ == '__main__':
    unittest.main()
