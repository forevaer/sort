#! /bin/bash
import re
dataString = input("input data\n")
data = [ int(x) for x in re.split(" +", dataString)]
print("sore data : {}".format(data))
for index in range(1,len(data)):
    for cursor in range(index):
        if data[cursor] > data[index]:
            insertData = data[index]
            del data[index]
            data.insert(cursor, insertData)
            break
print("sort result : {}".format(data))
