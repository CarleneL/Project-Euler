'''Project Euler 4
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def is_palindrome(num):
	reverse_string= ''
	index = len(str(num)) - 1
	while index>=0:
		reverse_string += str(num)[index]
		index -= 1

	if reverse_string == str(num):
		return True
	else:
		return False

val = max([x * y for x in range(100, 1000) for y in range(100, 1000) if is_palindrome(x*y)])
print val
