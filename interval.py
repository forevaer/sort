#!/bin/bash
import re

dataString = input("input data:\n")
data = [int(x) for x in re.split(" +", dataString)]
print("sort data : {}".format(data))
indexInterval = [1, 3, 5, 7, 9]
maxIndex = len(data)
while indexInterval:
	interval = indexInterval.pop()
	if interval >= maxIndex:
		continue
	for index in range(interval):
		while index + interval < maxIndex:
			if data[index] > data[index + interval]:
				data[index], data[index + interval] = data[index + interval], data[index]
			index += interval
print("sort result : {}".format(data))
