import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    try:
        full_path = os.path.join(working_directory, directory)
        absolute_working_directory = os.path.normpath(os.path.abspath(working_directory))
        absolute_full_path =  os.path.normpath(os.path.abspath(full_path))
        if not absolute_full_path.startswith(absolute_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'
        if not os.path.isdir(absolute_full_path):
            return f'Error: "{absolute_full_path}" is not a directory'
        contents = os.listdir(path=absolute_full_path)
        string_contents = []
        for content in contents:
            abs_content = os.path.join(absolute_full_path, content)
            if os.path.isdir(abs_content):
                d = f'- {content}: file_size={os.path.getsize(abs_content)}, is_dir=True'
                string_contents.append(d)
            else:
                f = f'- {content}: file_size={os.path.getsize(abs_content)}, is_dir=False'
                string_contents.append(f)
        return "\n".join(string_contents)

    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
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
            

