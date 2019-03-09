def parse(data, index=0, end=None):
	if not end:
		end = len(data) - 1
	if end <= 2:
		return
	if index > end:
		return
	left = 2 * index + 1
	right = left + 1
	parse(data, left, end)
	parse(data, right, end)
	if left <= end and data[left] > data[index]:
		data[index], data[left] = data[left], data[index]
	if right <= end and data[index] < data[right]:
		data[index], data[right] = data[right], data[index]


def save(data, tail):
	if data[0] > data[tail]:
		data[0], data[tail] = data[tail], data[0]
		return False
	return True


def heap(data):
	cursor = len(data) - 1
	while True:
		parse(data, end=cursor)
		if save(data, cursor):
			break
		cursor -= 1
	return data


data = [1, 4, 2, 5, 7, 6, 9, 8, 3]
heap(data)
print(data)
