from setuptools import find_packages, setup

package_name = 'py_import_example'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='combi',
    maintainer_email='combinacijus@gmail.com',
    description='ROS2 example package on how to import python modules',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = py_import_example.my_node:main'
        ],
    },
)
