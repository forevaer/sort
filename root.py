class Node(object):
	def __init__(self, value):
		self.left = None
		self.right = None
		self.able = True
		self.value = value
		self.parent = None


def create(data, parent=None, nodes=[]):
	if not data:
		return parent
	if not nodes:
		parent = Node(data.pop(0))
		create(data, parent, [parent])
	more = []
	for node in nodes:
		if data:
			node.left = Node(data.pop(0))
			more.append(node.left)
		if data:
			node.right = Node(data.pop(0))
			more.append(node.right)
	create(data, parent, more)
	return parent


def show(*nodes):
	if not nodes:
		return
	follow = []
	for node in nodes:
		print(node.value, end="\t")
		if node.left:
			follow.append(node.left)
		if node.right:
			follow.append(node.right)
	print()
	show(*follow)


def check(node):
	if node.left and node.left.left:
		check(node.left)
	if node.right and node.right.right:
		check(node.right)
	if node.left.able and node.left.value > node.value:
		node.value, node.left.value = node.left.value, node.value
	if node.right and node.right.able and node.right.value > node.value:
		node.value, node.right.value = node.right.value, node.value


def exchange(node):
	nodes = [node]
	last = None
	while nodes:
		last = nodes.pop(0)
		if not last.able:
			break
		if last.left and last.left.able:
			nodes.append(last.left)
		if last.right and last.right.able:
			nodes.append(last.right)

	if last.left and last.left.able:
		last = last.left
	node.value, last.value = last.value, node.value
	last.able = False


def result(node):
	nodes = [node]
	result = []
	while nodes:
		node = nodes.pop(0)
		result.append(node.value)
		if node.left:
			nodes.append(node.left)
		if node.right:
			nodes.append(node.right)
	return result


def main():
	node = create([1, 2, 3, 4, 5, 6, 7])
	step = 0
	while node.left.able:
		print("====step : {}====".format(step))
		show(node)
		check(node)
		exchange(node)
	print("=====final=====")
	show(node)
	print("sort result : {}".format(result(node)))


if __name__ == '__main__':
    main()
