"""
this file contains functions for basic file
processing, such as reading, writing to file.

Author: Yapi Donatien Achou
"""

import json
from glob import glob


class processFile():


    def __init__(self):
        pass
        #self.data = data
        #self.output_path = output_path
        #self.input_path = input_path


    def create_json_file(self, data, output_path):
        """
        Create a json file containing data.
        Arguments:
        ----------
        data: (type: list or dict),
        the data to be saved in the json file.

        path: (type: string),
        the output json file name.

        Returns:
        -------
        None.
        """
        with open(output_path, 'w') as outfile:
            json.dump(data, outfile)


    def read_json_file(self, input_path):
        """
        read json file and return the data.
        Arguments:
        ---------
        input_path: (type: string),
        path to the json file.

        Returns:
        -------
        json_data: (type: type of the python object saved),
        the data contains in the json file
        """
        with open(input_path) as json_data:
            json_data = json.load(json_data)
            return json_data


    def get_all_files(self,directory_path, file_type="all"):
        """
        Get all files from a directory.
        If type is not none return only the files
        type. Example type=csv
        Arguments:
        ---------
        directory_path: (type: sting),
        the path to the directory.

        file_type: (type: string),
        the type of files contains in the directory
        """
        if file_type == "csv":
            try:
                files = glob("{}/**.csv".format(directory_path))
            except:
                files = None
        elif file_type == "h5":
            try:
                files = glob("{}/**.h5".format(directory_path))
            except:
                files = None
        elif file_type == "json":
            try:
                files = glob("{}/**.json".format(directory_path))
            except:
                files = None
        elif file_type == "all":
            try:
                files = glob("{}/*".format(directory_path))
            except:
                files = None
        return files


if __name__ == '__main__':
    process = processFile()
