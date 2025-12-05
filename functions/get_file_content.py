import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not target_path.startswith(abs_working_dir):
            return f"Error: Cannot read {file_path} as it is outside the permitted working directory"
        if not os.path.isfile(target_path):
            return f"Error: File not found or is not a regular file: {file_path}"

        with open(target_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
    except Exception as e:
        return f'Error: {str(e)}'
    return file_content_string