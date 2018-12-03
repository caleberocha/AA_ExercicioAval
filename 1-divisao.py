import sys, subprocess
from tabulate import tabulate

cont_pow1 = 0
cont_pow2 = 0
cont_rfibo = 0
cont_mfibo = 0

class Ex1:
	def __init__(self):
		self.cont_pow1 = 0
		self.cont_pow2 = 0
		self.cont_rfibo = 0
		self.cont_mfibo = 0

	def reset(self):
		self.cont_pow1 = 0
		self.cont_pow2 = 0
		self.cont_rfibo = 0
		self.cont_mfibo = 0

	def pow1(self, a, n):
		p = 1
		self.cont_pow1 += 1

		for i in range(n):
			self.cont_pow1 += 3
			p *= a
			self.cont_pow1 += 2
		return p

	def pow2(self, a, n):
		self.cont_pow2 += 2
		if n == 0:
			self.cont_pow2 += 1
			return 1

		self.cont_pow2 += 3
		if n % 2 == 0:
			self.cont_pow2 += 2
			return self.pow2(a, n/2) * self.pow2(a, n/2)
		else:
			self.cont_pow2 += 2
			return self.pow2(a, (n-1) / 2) * self.pow2(a,(n-1) / 2) * a

	def recursive_fibonacci(self, n):
		self.cont_rfibo += 2
		if n <= 1:
			self.cont_rfibo += 1
			return n

		self.cont_rfibo += 2
		return self.recursive_fibonacci(n-1) + self.recursive_fibonacci(n-2)

	def memoized_fibonacci(self, n):
		f = [-1 for i in range(n+1)]
		return self.lookup_fibonacci(n, f)

	def lookup_fibonacci(self, n, f):
		self.cont_mfibo += 2
		if f[n] >= 0:
			self.cont_mfibo += 1
			return f[n]
		
		self.cont_mfibo += 2
		if n <= 1:
			self.cont_mfibo += 1
			f[n] = n
		else:
			self.cont_mfibo += 2
			f[n] = self.lookup_fibonacci(n - 1, f) + self.lookup_fibonacci(n - 2, f)
		
		self.cont_mfibo += 1
		return f[n]


#subprocess.call(["pip", "install", "tabulate"])
op = []
ex = Ex1()

for i in range(33):
	ex.reset()
	op.append({
		"n": i,
		"pow1_result": ex.pow1(2, i),
		"pow2_result": ex.pow2(2, i),
		"pow1_op": ex.cont_pow1,
		"pow2_op": ex.cont_pow2,
		"rec_fibo_result": ex.recursive_fibonacci(i),
		"mem_fibo_result": ex.memoized_fibonacci(i),
		"rec_fibo_op": ex.cont_rfibo,
		"mem_fibo_op": ex.cont_mfibo
		})

print(tabulate(op, "keys"))