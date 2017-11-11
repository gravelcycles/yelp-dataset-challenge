from json import dumps, loads
from sys import getsizeof
from math import ceil
import os
import sys

ONE_HUNDRED_MB = 100000000 # Rounded down for smaller file sizes

# TODO: Write short documentation and use case for juicy
# TODO: Process json as we read from file. Ideally, asynchronously, but we can just read it one at a time
#           need to deal with case when last line isn't complete


def to_file(json_data, filename):
    """

    :param json_data: json object to save to file
    :param filename: filename (directories included)
    :return: None
    """
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
    """

    :param filename:
    :return:
    """
    if not os.path.isdir(filename):
        with open(filename, "rb") as f:
             return f.read()
    else:
        imported_string = ""
        files = os.listdir(filename)
        num_juicy_files = len( list( filter( lambda x : ".juicy" in x, files) ) )
        for i in range(num_juicy_files):
            with open(os.path.join(filename, str(i) + ".juicy"), "r") as f:
                imported_string += f.read()
        print("done with read")
        return imported_string


def from_json_file(filename):
    """
    Assuming there is a list of json entries, each of which is separated by a new line
    :param filename:
    :return:
    """
    if not os.path.isdir(filename):
        with open(filename, "r") as f:
            jsons = []
            for line in f:
                if (line != '') and (line[-2] == '}'):
                    print('ha')
                    jsons.append(loads(line))
            print("json_list size:", sys.getsizeof(jsons))
    else:
        files = os.listdir(filename)
        num_juicy_files = len( list( filter( lambda x : ".juicy" in x, files) ) )

        from_file_string = ""
        for i in range(num_juicy_files):
            with open(os.path.join(filename, str(i) + ".juicy"), "r") as f:
                from_file_string += f.read()
        print("from_file_string size:", sys.getsizeof(from_file_string))
        string_list = from_file_string.split("\n")
        print("string_list size:", sys.getsizeof(string_list))
        del from_file_string
        jsons = [loads(j_string) for j_string in string_list]
        print('jsons list size:', sys.getsizeof(jsons))
    return jsons

def to_json_file(list_of_objects, filename):
    """

        :param filename: A list of jsonifiable objects
        :return:
        """
    json_string = "\n".join([dumps(x) for x in list_of_objects])
    x = getsizeof(json_string)

    num_files = ceil(x / ONE_HUNDRED_MB)

    if num_files == 1:
        with open(filename, "w") as f:
            f.write(json_string)
    else:
        if not os.path.isdir(filename):
            os.makedirs(filename)
        objects_per_file = len(json_string) // num_files

        for i in range(num_files):
            with open(os.path.join(filename, str(i) + ".juicy"), "w") as f:
                if i == num_files - 1:
                    f.write(json_string[i* objects_per_file : ])
                else:
                    f.write(json_string[i * objects_per_file: (i + 1) * objects_per_file])
