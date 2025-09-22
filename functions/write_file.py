import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)

def write_file(working_directory, file_path, content):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not full_path.startswith(working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        # Create directory structure if it doesn't exist
        directory = os.path.dirname(full_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        # Write the file (creates it if it doesn't exist)
        with open(full_path, 'w') as file:
            file.write(content)
    except Exception as e:
        return f'Error: {str(e)}'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'