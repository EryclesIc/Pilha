class Node:
	def __init__(self, data):
		self.adjacents = []
		self.set_data(data)
		self.set_visited(False)

	def add_adjacent(self, node):
		self.adjacents.append(node)

	def set_visited(self, state):
		self.visited = state

	def is_visited(self):
		return self.visited

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data