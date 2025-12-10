import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not target_path.startswith(absolute_working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory.'
        
        dir_name = os.path.dirname(target_path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            return f'Error: Cannot write to "{file_path}" as the file does not exist. Created necessary directories.'
          
        with open(target_path, 'w') as file:
            file.write(content)

    except Exception as e:
        return f'Error: An unexpected error occurred: {str(e)}'
    
    return f'Succesfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes specified content to a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)