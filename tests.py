#!/usr/bin/env python3

from functions.write_file import write_file

def main():
    """Test the get_file_content function with various scenarios."""
    
    # Test 1
    print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"):\n')
    print("Result for writing lorem.txt:")
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result1)
    print()

    # Test 2
    print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"):\n')
    print("Result for writing morelorem.txt:")
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result2)
    print()

    # Test 3
    print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed"):\n')
    print("Result for writing temp.txt:")
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result3)
    print()

if __name__ == "__main__":
    main()
