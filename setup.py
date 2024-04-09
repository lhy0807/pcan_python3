#!/usr/bin/env python
#from distutils.core import setup
import os
import sys

from setuptools import setup, find_packages, Extension

# x_comp_args = [
#     "-I/usr/include/python3.8 -I/usr/include -I/opt/ros/noetic/include/libpcan"
# ]

# ext = Extension(
#     'pcan_python._pcan_module',
#     [
#         'src/pcan_module.c',
#         'src/pcan_module.i'
#     ],
#     # include_dirs=os.environ.get("C_INCLUDE_PATH", "").split(":") or None,
#     # library_dirs=os.environ.get("LIBRARY_PATH", "").split(":") or None,
#     swig_opts=list(x_comp_args),
#     extra_compile_args=list(x_comp_args)
# )

# print(ext)


setup(
    name='pcan_python',
    version='0.1dev',
    packages=['pcan_python',],
    license='BSD',
    long_description="This driver is a Python wrapper of the  peak-linux-driver (in C) for Linux.",
    include_package_data=True,
    package_data={"": ["_pcan_module.so"]}
    # ext_modules=[ext]
)
