import os
from google.genai import types
from config import MAX_CHARS
def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_working_directory = os.path.normpath(os.path.abspath(working_directory))
        absolute_full_path =  os.path.normpath(os.path.abspath(full_path))
        if not absolute_full_path.startswith(absolute_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'
        if not os.path.isfile(absolute_full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        max_chars = 10000
        with open(full_path, "r") as f:
            file_content_string = f.read(max_chars)
            if f.read(1) == "":
                return file_content_string
            else:
                truncated = file_content_string + f'[...File "{file_path}" truncated at 10000 characters]'
                return truncated
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

