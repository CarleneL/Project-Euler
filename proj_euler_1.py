'''Project euler 1
Find the sum of all of the multiples of 3 and 5 under 1000
'''

#One line solution
print "List Comprehension"
sum_of_mult = sum([ item for item in range(0,1002) if item%3==0 or item%5 == 0])
print sum_of_mult

#Iterative solution
print "Iterative"
multThrees= range(0, 1000, 3)
multFives= range(0, 1000, 5)
running_total = 0
all_mult=set(multThrees + multFives)
for x in all_mult:
	running_total += x

print running_total