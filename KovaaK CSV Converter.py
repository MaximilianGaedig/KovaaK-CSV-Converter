import re
import fnmatch
import os
import ctypes
result = ctypes.windll.user32.MessageBoxW(0, "Run? All CSV files in this folder will be edited!", "KovaaK CSV Converter", 32 | 4)
if result == 6:
    cwd = os.getcwd()
    for filename in os.listdir("."):
        if fnmatch.fnmatch(filename, '*.csv'):
            print(filename)
            file = os.path.join(cwd, filename)
            with open(file, 'r+') as csv:
                content = csv.read()
                content_new = re.sub('(..:..:..)(.)(..)', r'\1:\3', content, flags=re.M)
                csv.write(content_new)
    ctypes.windll.user32.MessageBoxW(0, "Converted all CSVs to the new Format", "KovaaK CSV Converter", 64)
else:
    exit(0)
