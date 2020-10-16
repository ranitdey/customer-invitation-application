class FileReader:
    @staticmethod
    def read_file(path: str):
        """
        Reads a file.
        :param path: Path of the input file
        :return: List of line separated content of the file
        """
        raw_data = []
        with open(path, encoding='utf-8') as file:
            for line in file:
                raw_data.append(line)
        return raw_data
