#!/bin/bash
import re
dataString = input("input some data : \n")
data = [ int(x) for x in re.split(" +", dataString)]
print("sort data : {}".format(data))
for index in range(len(data)):
    for cursor in range(len(data) - index - 1):
        if data[cursor] > data[cursor+1]:
            data[cursor],data[cursor+1] = data[cursor+1], data[cursor]
print("sort result : {}".format(data))
