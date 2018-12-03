from tabulate import tabulate

class Item:
	def __init__(self, weight, value):
		self.weight = weight
		self.value = value

	def __str__(self):
		return "(" + str(self.weight) + "," + str(self.value) + ")"

	def __repr__(self):
		return self.__str__()

class Mochila:
	def __init__(self, capacity, items):
		self.capacity = capacity
		self.items = items
		self.n = len(self.items)
		self.aux_matrix = [[-1 for j in range(self.capacity + 1)] for i in range(self.n + 1)]
		self.cont_mr = 0
		self.cont_md = 0

	def reset(self):
		self.aux_matrix = [[-1 for j in range(self.capacity + 1)] for i in range(self.n + 1)]
		self.cont_mr = 0
		self.cont_md = 0

	def mochila_rec(self, n = None, capacity = None):
		if n is None:
			n = self.n
		if capacity is None:
			capacity = self.capacity
		
		if n == 0 or capacity == 0:
			self.cont_mr += 3
			return 0
		
		if self.items[n-1].weight > capacity:
			self.cont_mr += 3
			return self.mochila_rec(n-1, capacity)
		
		self.cont_mr += 3
		return max(self.items[n-1].value + self.mochila_rec(n-1, capacity-self.items[n-1].weight), self.mochila_rec(n-1, capacity))

	def mochila_pd(self):
		for i in range(self.n + 1):
			self.cont_md += 3
			for j in range(self.capacity + 1):
				self.cont_md += 3
				if i == 0 or j == 0:
					self.cont_md += 3
					self.aux_matrix[i][j] = 0
					self.cont_md += 1
				elif self.items[i-1].weight <= j:
					self.cont_md += 5
					self.aux_matrix[i][j] = max(self.items[i-1].value + self.aux_matrix[i-1][j-self.items[i-1].weight], self.aux_matrix[i-1][j])
				else:
					self.cont_md += 1
					self.aux_matrix[i][j] = self.aux_matrix[i-1][j]

		self.cont_md += 1
		return self.aux_matrix[self.n][self.capacity]
		


op = []
for n in range(2, 30):
	items = [Item(i, j) for i,j in zip(range(10, 10*n+10, 10), range(50, 50*n+50, 50))]
	c = items[-1].weight + items[-2].weight

	m = Mochila(c, items)
	op.append({
		"capacity": c,
		"ultimo_item": items[-1],
		"mochila_rec": m.mochila_rec(),
		"mochila_pd": m.mochila_pd(),
		"mochila_rec_op": m.cont_mr,
		"mochila_pd_op": m.cont_md
	})
	m.reset()

print(tabulate(op, "keys"))