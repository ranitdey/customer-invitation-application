import pytest

from src.config import ROOT_DIR
from src.lib.io.file_reader import FileReader


class TestFileReader:
    @staticmethod
    def test_file_read_with_wrong_path():
        path = "/error/error.txt"
        with pytest.raises(FileNotFoundError) as exception_info:
            FileReader.read_file(path)
        assert exception_info.typename == "FileNotFoundError"

    @staticmethod
    def test_file_read_with_happy_scenario():
        data_one = '{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}\n'
        data_two = '{"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}'
        data = FileReader.read_file(ROOT_DIR+"/src/tests/test_data/testFileRead.txt")
        assert len(data) == 2
        assert data[0] == data_one
        assert data[1] == data_two


