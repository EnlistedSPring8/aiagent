from functions.write_file_content import write_file
def main():
    test_one = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    test_two = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    test_three = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(test_one)
    print(test_two)
    print(test_three)

if __name__ == "__main__":
    main()