from json import dumps, loads
from sys import getsizeof
from math import ceil
import os

ONE_HUNDRED_MB = 100000000 # Rounded down for smaller file sizes

def to_file(json_data, filename):
    json_string = str(dumps(json_data))

    x = getsizeof(json_string)
    num_files = ceil(x / ONE_HUNDRED_MB)


    if num_files == 1:
        with open(filename, "w") as f:
            f.write(json_string)
    else:
        if not os.path.isdir(filename):
            os.makedirs(filename)
        chars_per_file = len(json_string) // num_files
        for i in range(num_files):
            with open(os.path.join(filename, str(i) + ".juicy"), "w") as f:
                if i == num_files - 1:
                    f.write(json_string[i * chars_per_file : ])
                else:
                    f.write(json_string[i*chars_per_file : (i+1)*chars_per_file])

def from_file(filename):
    if not os.path.isdir(filename):
        with open(filename, "rb") as f:
             return loads(f.readline())
    else:
        imported_string = ""
        files = os.listdir(filename)
        num_juicy_files = len( list( filter( lambda x : ".juicy" in x, files) ) )
        for i in range(num_juicy_files):
            with open(os.path.join(filename, str(i) + ".juicy"), "r") as f:
                imported_string += f.read()
        print("done with read")
        return loads(imported_string)


