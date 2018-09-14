import os

current_dir = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(current_dir, 'Migrations')

files = os.listdir(directory)
sql_files = list()
for file in files:
    if 'sql' in file:
        sql_files.append(file)

while True:
    word = input("введите строку ")
    for file in sql_files:
        with open(os.path.join(directory,sql_files[1])) as f:
            if word not in f.read().split(" "):
                sql_files.remove(file)
    for file in sql_files:
        print(file)
    print(len(sql_files))
            