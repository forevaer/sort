#! /bin/bash
import re
dataString = input("input data\n")
data = [ int(x) for x in re.split(" +", dataString)]
print("sore data : {}".format(data))
for index in range(1,len(data) - 1):
    insertData = data[index]
    del data[index]
    minIndex = 0
    maxIndex = index
    if insertData < data[minIndex]:
        data.inseret(minIndex, insertData)
        continue
    if insertData > data[maxIndex]:
        data.insert(maxIndex,insertData)
        continue
    while True:
        midIndex =int((minIndex + maxIndex) / 2)
        if midIndex == minIndex:
            if data[midIndex] > insertData:
                data.insert(minIndex, insertData)
            else:
                data.insert(midIndex+1,insertData)
            break
        if data[midIndex] > insertData:
            maxIndex = midIndex
            continue
        if data[midIndex] < insertData:
            minIndex = midIndex
print("sort result : {}".format(data))
