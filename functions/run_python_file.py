import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not target_path.startswith(abs_working_dir):
            return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"
        
        if not os.path.exists(target_path):
            return f'Error: File "{file_path}" not found.'
        root, ext = os.path.splitext(target_path)
        if ext.lower() != '.py':
            return f'Error: File \"{file_path}\" is not a Python file.'

        result = subprocess.run(
            ['python', target_path] + args,
            cwd=abs_working_dir,
            timeout=30,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            return f'Process exited with code "{result.returncode}"'
        if not result.stdout and not result.stderr:
            return 'No output produced'
        return f'STDOUT: "{result.stdout}"\nSTDERR: "{result.stderr}"'

    except Exception as e:
        return f'Error: executing Python file: {str(e)}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified python file, constrained to the working directory.",
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