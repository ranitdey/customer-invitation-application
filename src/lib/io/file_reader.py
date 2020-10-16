class FileReader:
    @staticmethod
    def read_file(path: str):
        raw_data = []
        with open(path, encoding='utf-8') as file:
            for line in file:
                raw_data.append(line)
        return raw_data
