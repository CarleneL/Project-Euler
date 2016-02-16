''' Project Euler 2:
Find the sum of the even Fibonacci numbers under 4mil
'''
running_sum= 0 

a = 1
b = 1
while a <= 4000000:
	if a % 2 == 0:
		running_sum += a
	a, b =b, a + b
	#print a, b
print running_sum