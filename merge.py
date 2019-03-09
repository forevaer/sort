#!/bin/bash
import re


def mergeSort(sortData):
	dataLength = len(sortData)
	if dataLength <= 1:
		return sortData
	mid = dataLength // 2
	leftSubData = mergeSort(sortData[:mid])
	rightSubData = mergeSort(sortData[mid:])
	return merge(leftSubData, rightSubData)


def merge(leftData, rightData):
	result = []
	leftIndex = 0
	rightIndex = 0
	leftMaxIndex = len(leftData)
	rightMaxIndex = len(rightData)
	while leftIndex < leftMaxIndex and rightIndex < rightMaxIndex:
		if leftData[leftIndex] < rightData[rightIndex]:
			result.append(leftData[leftIndex])
			leftIndex += 1
		else:
			result.append(rightData[rightIndex])
			rightIndex += 1
	result += leftData[leftIndex:]
	result += rightData[rightIndex:]
	return result


dataString = input("input data:\n")
data = [int(x) for x in re.split(" +", dataString)]
print("sort data : {}".format(data))
result = mergeSort(data)
print("sort result : {}".format(result))
