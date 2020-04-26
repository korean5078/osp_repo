#!/usr/bin/python3

def conversion(n):
	num = int(n, 2)
	print("=> OCT>",end=' ')
	print(format(num, 'o'))
	print("=> DEC>",end=' ')
	print(num)
	print("=> HEX>",end=' ')
	print(format(num, 'X'))
	return 0
