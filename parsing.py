# parsing.py os
from awpy import DemoParser
import os
from multiprocessing import Pool
import pandas as pd
import numpy as np


# def parse_demo_files(directory_path, parse_first_only=False):
#     parsed_data_list = []
#     files = [os.path.join(directory_path, file_name) for file_name in os.listdir(directory_path)]

#     def parse_demo_file(demo_file_path):
#         demo_parser = DemoParser(demofile=demo_file_path, demo_id="demo1", parse_rate=128)
#         return demo_parser.parse(return_type="df")

#     if parse_first_only and files:
#         print(files[0])
#         parsed_data_list.append(parse_demo_file(files[0]))
#     else:
#         for demo_file_path in files:
#             parsed_data_list.append(parse_demo_file(demo_file_path))

#     return parsed_data_list

def parse_demo_file(args):
    demo_file_path, demo_file_name = args
    print("Process {} Parsing file {} with path {}".format(os.getpid(),demo_file_name, demo_file_path))
    demo_parser = DemoParser(demofile=demo_file_path, demo_id=demo_file_name, parse_rate=128)
    return demo_parser.parse(return_type="df")

def parse_demo_files_in_batches(directory_path, num_processes, num_files):
    files = [os.path.join(directory_path, file_name) for file_name in os.listdir(directory_path)]
    files = files[:num_files]  # Limit the number of files to parse

    args = [(file_path, os.path.basename(file_path)) for file_path in files]

    with Pool(num_processes) as pool:
        parsed_data_list = pool.map(parse_demo_file, args)
    
    return parsed_data_list

# You can keep the single file parsing logic for reference or for other uses
def parse_demo_files(directory_path, parse_first_only=False):
    parsed_data_list = []
    files = [os.path.join(directory_path, file_name) for file_name in os.listdir(directory_path)]

    if parse_first_only and files:
        print(files[0])
        parsed_data_list.append(parse_demo_file((files[0], os.path.basename(files[0]))))
    else:
        for demo_file_path in files:
            parsed_data_list.append(parse_demo_file((demo_file_path, os.path.basename(demo_file_path))))

    return parsed_data_list
