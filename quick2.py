import re


def sort(arr, low, high):
	if low >= high:
		return
	tempLow = low
	tempHigh = high
	while tempLow < tempHigh:
		while tempLow < tempHigh and arr[tempHigh] > arr[tempLow]:
			tempHigh -= 1
		arr[tempHigh], arr[tempLow] = arr[tempLow], arr[tempHigh]
		while tempLow < tempHigh and arr[tempLow] < arr[tempHigh]:
			tempLow += 1
		arr[tempHigh], arr[tempLow] = arr[tempLow], arr[tempHigh]
	sort(arr, low, tempLow - 1)
	sort(arr, tempHigh + 1, high)


dataString = input("input data:\n")
data = [int(x) for x in re.split(" +", dataString)]
print("sort data : {}".format(data))
sort(data, 0, len(data) - 1)
print("sort result : {}".format(data))
