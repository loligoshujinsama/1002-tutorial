#!/usr/bin/env/python
import os
import sys
import subprocess

filename = sys.argv[1]
output = sys.argv[2]

# cwd = os.getcwd()
# if cwd != r"H:\University\Y1T1\1002_Programming\c_files":
#     os.chdir(r"H:\University\Y1T1\1002_Programming\c_files")
    
command = f"gcc.exe {filename} -o {output}"
result = subprocess.run(command, check=True)
if result.stdout == None:
    print(f"Successfully created {output}")
else:
    print(result.stdout)

# command2 = f"./{output}"
# result2 = subprocess.run(command2, text=True, capture_output=True)
# print(result2.stdout)