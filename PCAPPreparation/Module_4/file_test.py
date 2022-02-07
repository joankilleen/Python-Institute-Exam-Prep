"""Reading and writing a normal file
import os
import sys
try:
    dir_path = os.getcwd()
    new_file_path = str(os.path.join(dir_path, 'newtext.txt'))
    fo = open(new_file_path, 'wt')
    for i in range(10):
        s = "Joans line #" + str(i+1) + "\n"
        fo.write(s)
    fo.close()
except IOError as e:
	print("I/O error occurred: ", os.strerror(e.errno))

Reading and writing a binary file
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))"""


try:
    brf = open('newtext.txt', 'rb')
    data_read = bytearray(brf.read())
    brf.close()
    for b in data_read:
        print(b, end='')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
#print(data)

	