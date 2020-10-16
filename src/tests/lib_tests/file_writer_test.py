import pytest

from src.lib.io.file_writer import FileWriter


class TestFileReader:
    @staticmethod
    def test_file_writer_wrong_path():
        wrong_path = "/error/folder/"
        with pytest.raises(FileNotFoundError) as exception_info:
            FileWriter.write_to_file("test", wrong_path)
        assert exception_info.typename == "FileNotFoundError"
