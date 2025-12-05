import os

def get_files_info(working_directory, directory=""):

    try:
        file_path = os.path.join(working_directory, directory)

        abs_path = os.path.abspath(file_path)
        abs_working_dir = os.path.abspath(working_directory)

        if not abs_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside of the working directory "{working_directory}"'
        if os.path.isdir(abs_path) is False:
            return f'Error: "{directory}" is not a directory'

        file_info = []
        for files in os.listdir(abs_path): 
            name = os.path.basename(files)
            full_path = os.path.join(abs_path, name)
            file_size = os.path.getsize(full_path)
            is_dir = str(os.path.isdir(full_path))
            
            file_info.append(f'- {name}: file_size={file_size} bytes, is_dir={is_dir}')
    except Exception as e:
        return f'Error: {str(e)}'
    return "\n".join(file_info)

