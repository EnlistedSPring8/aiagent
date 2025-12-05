from functions.get_file_content import get_file_content

def main():
    print("Works as expected:")
    print(get_file_content("calculator", "main.py"))
    print("Works as expected:")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("Expected: Error for outside working directory:")
    print(get_file_content("calculator", "/bin/cat"))
    print("Expected: Error for non-existent file:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print("Expected: First 3 words of lorem.txt:")
    print(get_file_content("calculator", "lorem.txt").split()[:3])



if __name__ == "__main__":
    main()