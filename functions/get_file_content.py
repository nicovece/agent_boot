import os
from google.genai import types
from .config import MAX_FILE_CONTENT_LENGTH

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)


def get_file_content(working_directory, file_path):
    try:
        working_directory = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        
        if not full_path.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            
        if not os.path.exists(full_path):
            return f'Error: "{file_path}" is not a file'
        
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(full_path, 'r') as file:
            content = file.read(MAX_FILE_CONTENT_LENGTH + 1)  # Read one extra char
            
        if len(content) > MAX_FILE_CONTENT_LENGTH:
            truncated_content = content[:MAX_FILE_CONTENT_LENGTH]
            truncation_message = f'[...File "{file_path}" truncated at {MAX_FILE_CONTENT_LENGTH} characters]'
            return truncated_content + truncation_message
            
        return content
            
    except PermissionError:
        return f'Error: Permission denied when trying to read "{file_path}"'
    except UnicodeDecodeError:
        return f'Error: Unable to decode "{file_path}" - file may contain binary data or unsupported encoding'
    except OSError as e:
        return f'Error: Operating system error when accessing "{file_path}": {str(e)}'
    except Exception as e:
        return f'Error: Unexpected error when reading "{file_path}": {str(e)}"'