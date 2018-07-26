import os
os.getcwd()
os.chdir('.')
os.getcwd()
data = open('fileToRead.txt')
print(data.readline(), end='')
print(data.readline(), end='')
print(data.readline(), end='')
print(data.readline(), end='')

data.seek(0)
print('now print ------- from for loop')
for line_item in data:
    print(line_item, end='')