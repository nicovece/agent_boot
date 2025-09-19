#!/usr/bin/env python3

from functions.run_python_file import run_python_file

def main():
    """Test the get_file_content function with various scenarios."""
    
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
    main()
