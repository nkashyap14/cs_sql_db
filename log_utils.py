# log_utils.py

import os
from datetime import datetime

def log_timing_and_count(log_file_path, description, duration, count):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f'{timestamp} - {description} - Duration: {duration:.2f} seconds, Records Inserted: {count}\n'
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_message)

def log_failed_entries(log_file_path, failed_entries):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file_path, 'a') as log_file:
        for entry in failed_entries:
            log_message = f'{timestamp} - Failed Entry: {entry}\n'
            log_file.write(log_message)
    
    print(f"Failed entries have been logged to {log_file_path}")

