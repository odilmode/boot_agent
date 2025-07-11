#from functions.get_files_content import get_files_content
#from functions.write_file import write_file
from functions.run_python_file import run_python_file
"""def test1_get_files_content():
    print("Result for current directory: \n", get_files_content("calculator", "lorem.txt"))

def test2_get_files_content():
    print("Result for 'main.py': \n", get_files_content("calculator", "main.py"))

def test3_get_files_content():
    print("Result for 'pkg/calculator.py': \n", get_files_content("calculator", "pkg/calculator.py"))

def test4_get_files_content():
        print("Result for '/bin/cat': \n", get_files_content("calculator", "/bin/cat"))
"""

"""def write_file1():
    print("Result for 'lorem.txt': \n", write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

def write_file2():
    print("Result for 'pkg/morelorem.txt': \n", write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

def write_file3():
    print("Result for '/tmp/temp.txt': \n", write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))"""

def run_python_file1():
    print("Result for 'main.py': \n", run_python_file("calculator", "main.py"))

def run_python_file2():
    print("Result for 'tests.py': \n", run_python_file("calculator", "tests.py"))

def run_python_file3():
    print("Result for '../main.py': \n", run_python_file("calculator", "../main.py"))

def run_python_file4():
    print("Result for 'nonexistent.py': \n", run_python_file("calculator", "nonexistent.py"))





if __name__ == '__main__':
    #test1_get_files_content()
    #test2_get_files_content()
    #test3_get_files_content()
    #test4_get_files_content()
    #write_file1()
    #write_file2()
    #write_file3()
    run_python_file1()
    run_python_file2()
    run_python_file3()
    run_python_file4()

