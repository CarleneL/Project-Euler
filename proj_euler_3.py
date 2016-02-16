'''Project Euler 3
Find the largest prime factor of 600851475143
'''

divisors=[]
num = 600851475143
for x in range(1, num+1):
	if num % x == 0 :
		divisors.append(x)

print max(divisors)