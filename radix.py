def radix(data, digit=0):
	buckets = []
	result = []
	flag = False
	for index in range(0, 10):
		buckets.append([])
	step = pow(10, digit)
	for value in data:
		buckets[(value % step) // (step if step < 10 else step // 10)].append(value)
		if not flag:
		    flag = value // step
	for bucket in buckets:
		if bucket:
			result += bucket
	if flag:
		return radix(result, digit + 1)
	return result


a = [1, 3, 2, 5, 7, 9, 19, 199, 1999, 11, 57, 234]
print(radix(a))
