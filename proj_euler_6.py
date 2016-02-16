'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


difference = (sum(range(0,101)) ** 2) - sum([x ** 2 for x in range(0, 101)])
