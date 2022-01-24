import os

def file_exists(file_path):
    """
    Check if a file exists and is not a directory
    """
    return os.path.isfile(file_path)