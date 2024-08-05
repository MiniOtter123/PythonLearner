# 1. File Operations
print('===[1. File Operations]===')

# 1.1 Write Sample Text and Lines
print('===[1.1 Write Sample Text and Lines]===')

f = open('10-Data.txt', 'w', encoding="utf-8")
f.write("This is a sample text.\n")
lines = ["Line 1\n", "Line 2\n", "Line 3\n", "Line 4\n", "Line 5\n"]
f.writelines(lines)
f.close()

# 1.2 Read All Text at Once
print('===[1.2 Read All Text at Once]===')

with open('10-Data.txt', 'r') as f:
    print('Read all text: ')
    read_data = f.read()
    print(read_data)

# 1.3 Read Line by Line
print('===[1.3 Read Line by Line]===')

with open('10-Data.txt', 'r') as f:
    print('Read by line: ')
    for line in f:
        print(line, end='')
    print('')

# 1.4 Read Line 2
print('===[1.4 Read Line 2]===')

with open('10-Data.txt', 'r') as f:
    line = f.readline(-1)
    print(line)
    line = f.readline(-1)
    print(line)

# 1.5 Read-Write: Modify Existing Content
print('===[1.5 Read-Write: Modify Existing Content]===')

with open('10-Data.txt', 'r+') as f:
    existing_data = f.read()
    print(existing_data)
    f.seek(0, 0)
    f.write("New content at the beginning")
    f.seek(0, 2)
    f.write("Additional content at the end\n")

# 1.6 Append New Lines to Existing File
print('===[1.6 Append New Lines to Existing File]===')
with open('10-Data.txt', 'a') as f:
    f.write("New log entry 1\n")
    f.write("New log entry 2\n")

# 1.7 Modify a Specific Line
print('===[1.7 Modify a Specific Line]===')

with open('10-Data.txt', 'r+') as f:
    lines = f.readlines()
    lines[2] = "This is the modified line.\n"
    f.seek(0)
    f.writelines(lines)

# 1.8 Delete a Line
print('===[1.8 Delete a Line]===')

with open('10-Data.txt', 'r+') as f:
    lines = f.readlines()
    del lines[2]
    f.seek(0)
    f.writelines(lines)

# 2. Other file operations
print('===[2. Other file operations]===')

import os

source_file = 'Source.txt'
destination_file = 'Destination.txt'
source_dir = 'Source'
destination_dir = 'Destination'

# 2.1 Checking File Existence
print('===[2.1 Checking File Existence]===')

if os.path.isfile(source_file):
    print(f"File '{source_file}' exists")
else:
    print(f"File '{source_file}' does not exist")

# 2.2 Checking Directory Existence
print('===[2.2 Checking Directory Existence]===')

if os.path.isdir(source_dir):
    print(f"Directory '{source_dir}' exists")
else:
    os.makedirs(source_dir, exist_ok=True)

# 2.3 Operating Files and Directories
print('===[2.3 Operating Files and Directories]===')
import shutil

shutil.copy2(source_file, destination_file)
shutil.copytree(source_dir, destination_dir, copy_function=shutil.copy2)

# 2.4 Deleting Files and Directories
print('===[2.4 Deleting Files and Directories]===')

if os.path.exists(destination_file):
    print(f'{destination_file} file is existent')
    os.remove(destination_file)

if os.path.exists(destination_dir):
    print(f'{destination_file} directory is existent')
    shutil.rmtree(destination_dir)


# 2.5 Moving Files and Directories to Trash
print('===[2.5 Moving Files and Directories to Trash]===')

import send2trash
send2trash.send2trash('10-Data.txt')
