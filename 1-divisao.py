import sys, subprocess
from tabulate import tabulate

cont_pow1 = 0
cont_pow2 = 0
cont_rfibo = 0
cont_mfibo = 0

def pow1(a, n):
	global cont_pow1

	p = 1
	cont_pow1 += 1

	for i in range(n):
		cont_pow1 += 3
		p *= a
		cont_pow1 += 2
	return p

def pow2(a, n):
	global cont_pow2

	if n == 0:
		cont_pow2 += 3
		return  1

	if n % 2 == 0:
		cont_pow2 += 3
		return pow2(a, n/2) * pow2(a, n/2)
	else:
		cont_pow2 += 3
		return pow2(a, (n-1) / 2) * pow2(a,(n-1) / 2) * a

def recursive_fibonacci(n):
	global cont_rfibo

	if n <= 1:
		cont_rfibo += 3
		return n

	return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def memoized_fibonacci(n):
	f = [-1 for i in range(n+1)]
	return lookup_fibonacci(n, f)

def lookup_fibonacci(n, f):
	global cont_mfibo

	cont_mfibo += 3
	if f[n] >= 0:
		return f[n]
	
	if n <= 1:
		f[n] = n
	else:
		f[n] = lookup_fibonacci(n - 1, f) + lookup_fibonacci(n - 2, f)
	
	cont_mfibo += 1
	return f[n]


#subprocess.call(["pip", "install", "tabulate"])
op = []

for i in range(33):
	cont_pow1 = 0
	cont_pow2 = 0
	op.append({
		"n": i,
		"pow1_result": pow1(2, i),
		"pow2_result": pow2(2, i),
		"pow1_op": cont_pow1,
		"pow2_op": cont_pow2,
		"rec_fibo_result": recursive_fibonacci(i),
		"mem_fibo_result": memoized_fibonacci(i),
		"rec_fibo_op": cont_rfibo,
		"mem_fibo_op": cont_mfibo
		})

print(tabulate(op, "keys"))