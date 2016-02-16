''' Project Euler 13
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''

long_numbers = []
with open("proj_euler_13.txt", "r") as f:
	long_numbers=f.readlines()
print str(reduce(lambda x, y: x+y,[int(i) for i in long_numbers]))[0:10]

