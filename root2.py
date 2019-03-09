def up(data, end):
	last = (end + 1) // 2 - 1
	while not last < 0:
		left = 2 * last + 1
		if data[last] < data[left]:
			data[last], data[left] = data[left], data[last]
		right = 2 * last + 2
		if right <= end and data[last] < data[right]:
			data[last], data[right] = data[right], data[last]
		last = (last + 1) // 2 - 1


def down(data, end):
	data[0], data[end] = data[end], data[0]
	return data


a = [1, 3, 2, 4, 5]
for tail in range(len(a) - 1, -1, -1):
	up(a, tail)
	down(a, tail)
print(a)
