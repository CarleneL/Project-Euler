'''
Find the sum of the digits in the number 100!
'''


def recursive_factorial(num):
	if num == 1 or num == 0:
		return 1
	else:
		return num * recursive_factorial(num - 1)

solution = reduce(lambda x,y: x + y , [int(i) for i in list(str(recursive_factorial(100)))])