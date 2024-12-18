# remote_db.py

import paramiko
from config import SSH_HOST, SSH_PORT, SSH_USER, SSH_KEY_PATH, REMOTE_DB_PATH
import uuid
from datetime import datetime
from log_utils import log_failed_entries
import time

def log_failed_entry(log_file_path, failed_command, sql_file_name):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f'{timestamp} - Failed Entry in {sql_file_name}: {failed_command}\n'
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_message)

def execute_remote_sql(commands, log_file_path, retries=10, backoff=1):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(SSH_HOST, SSH_PORT, SSH_USER, key_filename=SSH_KEY_PATH)
    
    # Generate a unique file name
    unique_id = uuid.uuid4()
    remote_file_path = f'/tmp/sql_commands_{unique_id}.sql'
    
    # Join all commands into a single script
    full_command = "\n".join(commands)
    
    # Save the commands to a temporary file on the remote server
    sftp_client = ssh_client.open_sftp()
    with sftp_client.file(remote_file_path, 'w') as remote_file:
        remote_file.write(full_command)
    sftp_client.close()
    
    attempt = 0
    while attempt < retries:
        # Execute the script using sqlite3
        stdin, stdout, stderr = ssh_client.exec_command(f"sqlite3 {REMOTE_DB_PATH} < {remote_file_path}")
        stdout_output = stdout.read().decode()
        stderr_output = stderr.read().decode()
        
        if stderr_output:
            if "database is locked" in stderr_output:
                print(f"Database is locked. Attempt {attempt + 1} failed.")
                attempt += 1
                if attempt < retries:
                    time.sleep(backoff)
                    backoff *= 2  # Exponential backoff
                else:
                    print("All retry attempts failed due to database locking.")
                    raise Exception(f"Database locked error: {stderr_output}")
            else:
                print(f"Error: {stderr_output}")
                # Log the error with the remote file path
                for command in commands:
                    log_failed_entry(log_file_path, command, remote_file_path)
                raise Exception(f"Database error: {stderr_output}")
        else:
            print(f"Output: {stdout_output}")
            break  # If successful, exit the loop
    
    ssh_client.close()