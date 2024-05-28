import sys
import pandas as pd
import numpy as np

# Utility function to calculate the deep size of an object
def get_deep_size(obj, seen=None):
    """Recursively finds the size of objects, including nested elements."""
    
    if seen is None:
        seen = set()
    
    obj_id = id(obj)
    
    if obj_id in seen:
        return 0
    
    seen.add(obj_id)
    
    size = sys.getsizeof(obj)
    
    if isinstance(obj, dict):
        size += sum(get_deep_size(v, seen) for v in obj.values())
        size += sum(get_deep_size(k, seen) for k in obj.keys())
    
    elif hasattr(obj, '__dict__'):
        size += get_deep_size(vars(obj), seen)
    
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum(get_deep_size(i, seen) for i in obj)
    
    return size

# Batch insert function
def batch_insert(objects_list, insert_function):
    batch_size = 100
    commands = []
    for i in range(0, len(objects_list), batch_size):
        batch = objects_list[i:i + batch_size]
        batch_commands = [insert_function(obj) for obj in batch]
        commands.extend(batch_commands)
    return commands

def clean_dataframe(df):
    # Replace string '<NA>' with None
    df.replace('<NA>', None, inplace=True)
    # Replace pd.NA and np.nan with None
    df.replace({pd.NA: None, np.nan: None}, inplace=True)
    # Replace None with the string 'NULL'
    df = df.applymap(lambda x: 'NULL' if x is None else x)
    return df

def clean_parsed_data(parsed_data):
    for key, value in parsed_data.items():
        if isinstance(value, pd.DataFrame):
            parsed_data[key] = clean_dataframe(value)
    return parsed_data


# def clean_dataframe(df):
#     # Replace string '<NA>' with None (which will be converted to SQL NULL)
#     df.replace('<NA>', None, inplace=True)
#     # Replace pd.NA and np.nan with None for SQL compatibility
#     df.replace({pd.NA: None, np.nan: None}, inplace=True)
#     return df

# def clean_parsed_data(parsed_data):
#     for key, value in parsed_data.items():
#         if isinstance(value, pd.DataFrame):
#             parsed_data[key] = clean_dataframe(value)
#     return parsed_data