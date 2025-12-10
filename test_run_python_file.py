from functions.run_python_file import run_python_file

def tester(working_directory, file_path, args=[]):
    result = run_python_file(working_directory, file_path, args)
    print(result)

def main():
    print("Test 1: Valid Python file without arguments")
    tester("calculator", "main.py")
    print("Test 2: Valid run of the calcularot but with nasty rendered result")
    tester("calculator", "main.py", ["3 + 5"])
    print("Test 3: Attempt to run a file outside the working directory -> ERROR")
    tester("calculator", "tests.py")
    print("Test 4: Attempt to run a file outside the permitted working directory -> ERROR")
    tester("calculator", "../main.py")
    print("Test 5: Attempt to run a non-existent file -> ERROR")
    tester("calculator", "nonexistent.py")
    print("Test 6: Attempt to run a non-Python file -> ERROR")
    tester("calculator", "lorem.txt")

if __name__ == "__main__":
    main()