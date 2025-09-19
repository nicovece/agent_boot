import os
import sys
import subprocess


def run_python_file(working_directory, file_path, args=[]):
  working_directory = os.path.abspath(working_directory)
  full_path = os.path.abspath(os.path.join(working_directory, file_path))

  # Check if the file is within the permitted working directory
  if not full_path.startswith(working_directory):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
  
  # Check if the file exists
  if not os.path.exists(full_path):
    return f'Error: File "{file_path}" not found.'
  
  # Check if the file is a regular file
  if not os.path.isfile(full_path):
    return f'Error: File not found or is not a regular file: "{file_path}"'
  
  # Check if the file has a .py extension
  if not full_path.endswith('.py'):
    return f'Error: "{file_path}" is not a Python file.'
  
  try:
    # Prepare the command to run the Python file
    cmd = [sys.executable, full_path] + args
    
    # Execute the Python file using subprocess.run
    completed_process = subprocess.run(
      cmd,
      cwd=working_directory,  # Set working directory
      capture_output=True,    # Capture both stdout and stderr
      text=True,              # Return strings instead of bytes
      timeout=30              # Set 30-second timeout
    )
    
    # Get stdout and stderr from the completed process
    stdout = completed_process.stdout.strip() if completed_process.stdout else ""
    stderr = completed_process.stderr.strip() if completed_process.stderr else ""
    
    # Format the output
    output_parts = []
    
    if stdout:
      output_parts.append(f"STDOUT: {stdout}")
    
    if stderr:
      output_parts.append(f"STDERR: {stderr}")
    
    # Handle non-zero exit codes
    if completed_process.returncode != 0:
      output_parts.append(f"Process exited with code {completed_process.returncode}")
    
    # Return formatted output or "No output produced" if nothing was captured
    if output_parts:
      return "\n".join(output_parts)
    else:
      return "No output produced."
      
  except Exception as e:
    return f"Error: executing Python file: {e}"