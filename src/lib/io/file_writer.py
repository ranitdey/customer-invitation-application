from typing import List
import time


class FileWriter:
    @staticmethod
    def write_to_file(data, output_path: str):
        """
        Writes data in a output file.
        :param data: Data to write.
        :param output_path: Path where the output file will be placed
        :return:
        """
        with open(output_path+"/output_"+str(int(time.time()))+".txt", 'a') as out:
            if isinstance(data, List):
                for line in data:
                    out.write(line + '\n')
            else:
                out.write(data)
