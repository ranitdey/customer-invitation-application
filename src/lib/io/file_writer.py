from typing import List
import time


class FileWriter:
    @staticmethod
    def write_to_file(data, output_path: str):
        with open(output_path+"/output_"+str(int(time.time()))+".txt", 'a') as out:
            if isinstance(data, List):
                for line in data:
                    out.write(line + '\n')
            else:
                out.write(data)
