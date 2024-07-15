import codecs
import json


class Reader:
    def __init__(self, bin_file_path):
        self.__bin_file_path = bin_file_path

    def read(self):
        with open(self.__bin_file_path, "rb") as bin_file:
            return json.loads(codecs.decode(bin_file.read(), "zlib").decode("unicode_escape"))
