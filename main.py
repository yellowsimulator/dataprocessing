from fileprocessing import processFile
import os
process = processFile()
data = [2,3,4]
output_path = "test.json"
input_path = output_path
directory_path = os.getcwd()
file_type = "json"
process.create_json_file(data,output_path)

jsd = process.read_json_file(input_path)

files = process.get_all_files(directory_path, file_type=file_type)
print(files)
