# py_import_example - ROS2 Humble example package on how to import custom python modules

## Table of contents
- [py\_import\_example - ROS2 Humble example package on how to import custom python modules](#py_import_example---ros2-humble-example-package-on-how-to-import-custom-python-modules)
  - [Table of contents](#table-of-contents)
  - [Extra info](#extra-info)
  - [Main notes](#main-notes)
    - [Package tree structure](#package-tree-structure)
    - [How to import](#how-to-import)
    - [Where are python files installed](#where-are-python-files-installed)
  - [How to create such package from scratch](#how-to-create-such-package-from-scratch)


## Extra info
https://stackoverflow.com/questions/57426715/import-modules-in-package-in-ros2

## Main notes

To test this code `git clone` as `py_import_example` package or create package from scratch [How to create such package from scratch](#how-to-create-such-package-from-scratch)

### Package tree structure
```
src/py_import_example
├── LICENSE
├── package.xml
├── py_import_example
│   ├── file1.py  <--------- import module
│   ├── __init__.py
│   ├── my_node.py  <------- main node
│   └── subfolder
│       ├── file2.py  <----- import module in a subfolder
├── README
├── resource
│   └── py_import_example
├── setup.cfg
└── setup.py  <------------- setup.py
```

### How to import

In `my_node.py` there are multiple methods to import python modules
```python
# To import module function
from .file1 import fun1  # Notice dot before module name ".file1"
from .subfolder.file2 import fun2

# To import whole module
from py_import_example import file1  # Notice "from <package_name>"
from py_import_example.subfolder import file2

# Same as previous
import py_import_example.file1 as file1
import py_import_example.subfolder.file2 as file2
```
Note the dot in `from .file1 import fun1` it is relative import it tells Python to look for the module in the same directory as the module that contains this import statement   
Meanwhile `from file1 import fun1` is absolute import which searches for python modules in Python path.

Note that such imports won't work (at least in this package)
```python
# import .file1  # NOT VALID
# import .py_import_example.file1  # NOT VALID
```

setup.py should be modified just for my_node.py. No modifications needed for file1.py and file2.py as those modules are not nodes and will only be imported.
```python
entry_points={
    'console_scripts': [
        'my_node = py_import_example.my_node:main',
```

### Where are python files installed

Python nodes installed in `install/` directory
```bash
~/ros2_ws/install/py_import_example/lib/py_import_example/my_node
```
<!-- ls -->
Python modules seems to be install in `build/` directory which is referenced in `install/` `.egg-link` file
```bash
cat ~/ros2_ws/install/py_import_example/lib/python3.10/site-packages/py-import-example.egg-link
# Out: ~/ros2_ws/build/py_import_example
~/ros2_ws/build/py_import_example/py_import_example/file1.py
```


## How to create such package from scratch

Create ROS2 workspace or cd to src of existing workspace
```bash
# cd to ROS2 workspace
```

Create ament_python package
```bash
ros2 pkg create py_import_example --license Apache-2.0 --build-type ament_python --dependencies rclpy
```

Create python modules/files
```bash
cd py_import_example/py_import_example
touch my_node.py file1.py
mkdir subfolder
cd subfolder
touch file2.py
# Write source code to .py files
```

my_node.py
```python
def main():
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

if __name__ == '__main__':
    main()
```

file1.py (node in same dir as my_node.py)
```python
def fun1():
    print("file1.py")
```

file2.py (node in sufolder)
```python
def fun2():
    print("file2.py")
```

In setup.py add `'my_node = py_import_example.my_node:main',` for ROS2 node. No modifications needed for file1.py and file2.py as those modules are not nodes and will only be imported.
```python
entry_points={
    'console_scripts': [
        'my_node = py_import_example.my_node:main',
    ],
},
```

Build
```
cd ..  # cd to src directory
colcon build --symlink-install
```

Run
```
ros2 run py_import_example my_node
```

#Expected output
```
Import method 1
file1.py
file2.py
Import method 2
file1.py
file2.py
```