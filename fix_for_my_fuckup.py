import os
import fnmatch

cwd = os.getcwd()
for filename in os.listdir("."):
    if fnmatch.fnmatch(filename, '*.csv'):
        print(filename)
        file = os.path.join(cwd, filename)
        with open(file, 'r+') as csv:
            content = csv.read()
            content = content.replace("\n", "  ")
            pos = content.find("Kill #,Timestamp,Bot,Weapon,TTK,Shots,Hits,Accuracy,Damage Done,Damage Possible,Efficiency,Cheated", 1)
            print(pos)
            csv.seek(pos)
            csv.truncate()

