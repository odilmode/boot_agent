import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_working_directory = os.path.normpath(os.path.abspath(working_directory))
        absolute_full_path = os.path.normpath(os.path.abspath(full_path))
        if not absolute_full_path.startswith(absolute_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(absolute_full_path):
            return f'Error: File "{file_path}" not found.'
        if os.path.splitext(absolute_full_path)[1] != ".py":
            return f'Error: "{file_path}" is not a Python file.'

        try:
            proc = subprocess.run(["python", file_path], capture_output=True, text=True, timeout=30, cwd=absolute_working_directory)
            outs = "STDOUT:" + proc.stdout
            errs = "STDERR:" + proc.stderr
            formatted = outs + "\n" + errs
            status_code = proc.returncode
            if proc.stdout == "" and proc.stderr == "":
                return "No output produced."
            if status_code != 0:
                formatted += f'\nProcess exited with code {status_code}'
            return formatted

        except subprocess.CalledProcessError as e:
            return f"Error: executing Python file: {e}"
        except subprocess.TimeoutExpired as e:
            return f"Error: executing Python file: {e}"
    except Exception as e:
            return f"Error: {type(e).__name__}: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
