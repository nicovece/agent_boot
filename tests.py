#!/usr/bin/env python3

from functions.run_python_file import run_python_file
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.get_files_info import get_files_info

def test_function_calls():
    """Test all function calls as described in the lesson."""
    
    print("=== Testing Function Calls ===")
    print()
    
    # Test 1: get_file_content
    print("1. Testing get_file_content:")
    print("get_file_content({'file_path': 'main.py'})")
    result1 = get_file_content('.', 'main.py')
    print(f"Result: {result1}")
    print()
    
    # Test 2: write_file
    print("2. Testing write_file:")
    print("write_file({'file_path': 'main.txt', 'content': 'hello'})")
    result2 = write_file('.', 'main.txt', 'hello')
    print(f"Result: {result2}")
    print()
    
    # Test 3: run_python_file
    print("3. Testing run_python_file:")
    print("run_python_file({'file_path': 'main.py'})")
    result3 = run_python_file('.', 'main.py')
    print(f"Result: {result3}")
    print()
    
    # Test 4: get_files_info
    print("4. Testing get_files_info:")
    print("get_files_info({'directory': 'calculator/pkg'})")
    result4 = get_files_info('.', 'calculator/pkg')
    print(f"Result: {result4}")
    print()

def main():
    """Test the run_python_file function with various scenarios."""
    
    # Test 1
    print('run_python_file("calculator", "main.py")')
    print("Result for running main.py:")
    result1 = run_python_file("calculator", "main.py")
    print(result1)
    print()

    # Test 2
    print('run_python_file("calculator", "main.py", ["3 + 5"])')
    print("Result for running main.py:")
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result2)
    print()
    
    # Test 3
    print('run_python_file("calculator", "tests.py")')
    print("Result for running tests.py:")
    result3 = run_python_file("calculator", "tests.py")
    print(result3)
    print()
    
    # Test 4
    print('run_python_file("calculator", "../main.py")')
    print("Result for running ../main.py:")
    result4 = run_python_file("calculator", "../main.py")
    print(result4)
    print()
    
    # Test 5
    print('run_python_file("calculator", "nonexistent.py")')
    print("Result for running nonexistent.py:")
    result5 = run_python_file("calculator", "nonexistent.py")
    print(result5)
    print()

if __name__ == "__main__":
    # Run the lesson function call tests
    test_function_calls()
    
    print("\n" + "="*50)
    print("Original run_python_file tests:")
    print("="*50)
    
    # Run the original tests
    main()
