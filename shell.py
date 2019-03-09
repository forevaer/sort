#!/bin/bash
import re

dataString = input("input data:\n")
data = [int(x) for x in re.split(" +", dataString)]
print("sort data : {}".format(data))
totalLength = len(data)
indexInterval = 1
while indexInterval < totalLength / 3:
    indexInterval = 3 * indexInterval + 1
while indexInterval >= 1:
    for index in range(indexInterval, totalLength):
        while index > indexInterval and data[index] < data[index - indexInterval]:
            data[index], data[index - indexInterval] = data[index - indexInterval], data[index]
            index -= indexInterval
    indexInterval //= 3
print("sort result : {}".format(data))
