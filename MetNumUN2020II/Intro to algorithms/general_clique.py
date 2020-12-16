# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time

def count(n):
	# Your code here to count the units of time
	# it takes to execute clique
	return 2 + (1+n)*n/2

def clique(n):
	print "in a clique..."
	for j in range(n):
		for i in range(j):
			print i, "is friends with", j

if __name__ == '__main__':
	print count(4)