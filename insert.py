#!/bin/bash
import re
dataString = input("input some data: \n")
data = [int(x) for x in re.split(" +", dataString)]
print("sort data : {}".format(data))
result = []
while data:
    insertData = data.pop()
    if len(result) == 0:
        result.append(insertData)
        continue
    index = 0
    while index < len(result) and result[index] < insertData:
        index += 1
    result.insert(index, insertData)
print("sort result : {}".format(result))
