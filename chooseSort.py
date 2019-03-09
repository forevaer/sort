#! /bin/bash
import re

dataString = input("input some data :\n")
data = [int(x) for x in re.split(" +", dataString)]
print("sort data : {}".format(data))
result = []
while data:
    index = 0
    minValue = data[index]
    while index < len(data):
        if data[index] < minValue:
            minValue = data[index]
        index += 1
    result.append(minValue)
    data.remove(minValue)
print("sort result : {}".format(result))

