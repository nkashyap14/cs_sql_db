# parsing.py
import os
from awpy import DemoParser

def parse_demo_files(directory_path, parse_first_only=False):
    parsed_data_list = []
    files = [os.path.join(directory_path, file_name) for file_name in os.listdir(directory_path)]

    def parse_demo_file(demo_file_path):
        demo_parser = DemoParser(demofile=demo_file_path, demo_id="demo1", parse_rate=128)
        return demo_parser.parse(return_type="df")

    if parse_first_only and files:
        print(files[0])
        parsed_data_list.append(parse_demo_file(files[0]))
    else:
        for demo_file_path in files:
            parsed_data_list.append(parse_demo_file(demo_file_path))

    return parsed_data_list