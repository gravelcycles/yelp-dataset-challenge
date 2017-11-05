from json import dumps, loads
from sys import getsizeof
from math import ceil
import os

ONE_HUNDRED_MB = 104857600

def to_file(json_data, filename):
    json_string = dumps(json_data)

    x = getsizeof(getsizeof(json_string))
    num_files = ceil(x / ONE_HUNDRED_MB)
    if num_files == 1:
        with open(filename, "wb") as f:
            f.write(json_string)
    else:
        if not os.path.exists(filename):
            os.makedirs(filename)
        chars_per_file = len(json_string) // num_files
        for i, file_no in enumerate(num_files):
            with open(str(i) + ".juicy", "wb") as f:
                if i == num_files - 1:
                    f.write(json_string[i * chars_per_file : ])
                else:
                    f.write(json_string[i*chars_per_file : (i+1)*chars_per_file])

def from_file(filename):
    if not os.path.isdir(filename):
        with open(filename, "rb") as f:
             return loads(f.read())
    else:
        files_to_join = []
        files = os.listdir(filename)
        num_juicy_files = len( list( filter( lambda x : ".juicy" in x, files) ) )
        for i in range(num_juicy_files):
            with open(str(i) + ".juicy", "rb") as f:
                files_to_join.append(f.read())

        return ''.join(files_to_join)


