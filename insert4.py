#!/bin/bash
import re
dataString = input("input some data: \n")
data = [int(x) for x in re.split(" +", dataString)]
print("sort data : {}".format(data))
for index in range(1,len(data)):
    for cursor in range(index):
        if data[cursor] < data[index]:
            continue
        data[cursor],data[index] = data[index],data[cursor]
print("sort result : {}".format(data))
