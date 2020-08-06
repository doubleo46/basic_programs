class Node():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class Btree():
	def __init__(self, root):
		self.root = Node(root)

	def pre_order_traversal(self, node,parsed):
		if node:
			parsed += str(node.value)+ " - "
			parsed = self.pre_order_traversal(node.left, parsed) 
			parsed = self.pre_order_traversal(node.right, parsed)
		return parsed

	def in_order_traversal(self, node, traversal):
		if node:
			traversal = self.in_order_traversal(node.left, traversal)
			traversal += str(node.value) + " - "
			traversal = self.in_order_traversal(node.right, traversal)
		return traversal

	def print_tree(self, traverse_type):
		if traverse_type == "pre_order_traversal":
			return tree.pre_order_traversal(self.root,"")[:-2]
		elif traverse_type == "in_order_traversal":
			return tree.in_order_traversal(self.root,"")[:-2]			
		else:
			print(traverse_type, " not implemented.")
		return False


tree = Btree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("pre_order_traversal"))
print(tree.print_tree("in_order_traversal"))
#          
#              1
#          2       3
#         4  5    6 7
