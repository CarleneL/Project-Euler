''' Project Euler 16
What is the sum of the digits of the number 2**1000
'''

result = reduce(lambda x,y: x + y , [int(i) for i in list(str(2**1000))])


