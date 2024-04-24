def main():
    print_tree() # For debugging install path
    
    print("Import method 1")
    from .file1 import fun1
    from .subfolder.file2 import fun2
    fun1()
    fun2()
    
    
    print("Import method 2")
    from py_import_example import file1
    from py_import_example.subfolder import file2
    file1.fun1()
    file2.fun2()
    
    
    print("Import method 3")
    import py_import_example.file1 as file1
    import py_import_example.subfolder.file2 as file2
    file1.fun1()
    file2.fun2()
    
    # import .file1  # NOT VALID
    # import .py_import_example.file1  # NOT VALID
        

def print_tree():
    # Print tree of install and build folders and omit some unimportant files to make it more readable
    import os
    import sys
    print()
    print("my_node.py:", os.path.abspath(__file__))
    print()

    for path in sys.path[:1]:
        if os.path.exists(path) and os.path.isdir(path):
            print(f"{path}")
            for file in os.listdir(path):
                print(f"  {file}")
            
    def list_py_files(directory, prefix='  '):
        for entry in os.listdir(directory):
            path = os.path.join(directory, entry)
            if os.path.isdir(path):
                if entry in ['__pycache__', 'resource', 'hook', 'prefix_override']:
                    continue  # Skip __pycache__ directories
                print(f"{prefix}{entry}/")
                list_py_files(path, prefix + '  ')
            elif entry.endswith('.py'):
                print(f"{prefix}{entry}")

    # Loop through all entries in sys.path
    for path in sys.path[1:2]:
        if os.path.exists(path) and os.path.isdir(path):
            print(f"{path}")
            list_py_files(path)
            
    print()


if __name__ == '__main__':
    main()
