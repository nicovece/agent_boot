import os

def _get_directory_size(directory_path):
    """Calculate the total size of all files in a directory recursively."""
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(file_path)
                except (OSError, FileNotFoundError):
                    # Skip files that can't be accessed
                    continue
    except (OSError, PermissionError):
        # If we can't access the directory, return 0
        return 0
    return total_size

def get_files_info(working_directory, directory="."):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    
    if not full_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: "{directory}" is not a directory'
    
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    # Get list of all items in the directory
    try:
        items = os.listdir(full_path)
    except PermissionError:
        return f'Error: Permission denied to access "{directory}"'
    
    # Sort items alphabetically for consistent output
    items.sort()
    
    # Build the result string
    result_lines = []
    for item in items:
        item_path = os.path.join(full_path, item)
        
        # Check if it's a directory
        is_directory = os.path.isdir(item_path)
        
        # Get file size
        try:
            if is_directory:
                # For directories, calculate the total size of all files within
                file_size = _get_directory_size(item_path)
            else:
                file_size = os.path.getsize(item_path)
        except (OSError, FileNotFoundError):
            file_size = 0
        
        # Format the line according to the specified format
        line = f"- {item}: file_size={file_size} bytes, is_dir={is_directory}"
        result_lines.append(line)
    
    # Join all lines with newlines and return
    return "\n".join(result_lines)