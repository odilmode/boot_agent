import os
from google.genai import types
def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_working_directory = os.path.normpath(os.path.abspath(working_directory))
        absolute_full_path =  os.path.normpath(os.path.abspath(full_path))
        if not absolute_full_path.startswith(absolute_working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory.'
        if not os.path.exists(absolute_full_path):
            os.makedirs(os.path.dirname(absolute_full_path), exist_ok=True)
        with open(absolute_full_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
            return f"Error: {type(e).__name__}: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
