from typing import List


class FileWriter:
    @staticmethod
    def write_to_file(serialized_array: List[str], output_path: str):
        with open(output_path+"/output.txt", 'a') as out:
            for line in serialized_array:
                out.write(line + '\n')
