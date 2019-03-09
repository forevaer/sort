def sort(data):
	low = 0
	high = len(data) - 1
	while low < high:
		minIndex = low
		maxIndex = high
		for index in range(low, high + 1):
			if data[index] > data[maxIndex]:
				maxIndex = index
			if data[index] < data[minIndex]:
				minIndex = index
		data[low], data[minIndex] = data[minIndex], data[low]
		data[high], data[maxIndex] = data[maxIndex], data[high]
		low += 1
		high -= 1


a = [1, 3, 2, 5, 7, 6, 4, 9, 8]
sort(a)
print(a)
