from functions.get_files_info import get_files_info
print("Expected: Result for current directory: \n \
    - main.py: file_size=\"2048\" bytes, is_dir=\"False\"\n \
    - tests.py: file_size=\"1024\" bytes, is_dir=\"False\"\n \
    - pkg: file_size=\"4096\" bytes, is_dir=\"True\"")
print("Actual: " + get_files_info("calculator", "."))

print("Expected: Result for 'pkg' directory: \n \
  - calculator.py: file_size=1721 bytes, is_dir=False \n \
  - render.py: file_size=376 bytes, is_dir=False")
print("Actual: " + get_files_info("calculator", "pkg"))

print("Expected: Result for '/bin' directory: \n \
    Error: Cannot list ""/bin"" as it is outside the permitted working directory")
print("Actual: " + get_files_info("calculator", "/bin"))

print("Expected: Result for '../' directory: \n \
    Error: Cannot list ""../"" as it is outside the permitted working directory")
print("Actual: " + get_files_info("calculator", "../"))