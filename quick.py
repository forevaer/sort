import re
def sort(data):
	mid = len(data) // 2
	if mid < 1:
		return data
	midValue = data[mid]
	del data[mid]
	minSubData,maxSubData = [], []
	for value in data:
		if value <= midValue:
			minSubData.append(value)
		else:
			maxSubData.append(value)
	return sort(minSubData) + [midValue] + sort(maxSubData)

dataString = input("input data:\n")
data = [int(x) for x in re.split(" +", dataString)]
print("sort data : {}".format(data))
result = sort(data)
print("sort result : {}".format(result))