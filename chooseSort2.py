#! /bin/bash
import re

dataString = input("input some data :\n")
data = [int(x) for x in re.split(" +", dataString)]
print("sort data : {}".format(data))
for index in range(len(data)):
    minValue = data[index]
    targetIndex = index
    for cursorIndex in range(index, len(data)):
        if data[cursorIndex] < minValue:
            minValue = data[cursorIndex]
            targetIndex = cursorIndex
    data[index],data[targetIndex] = data[targetIndex], data[index]
print("sort result : {}".format(data))
