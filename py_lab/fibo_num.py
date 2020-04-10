#!/usr/bin/python3

count =  1
n = int(input("fibonacci number? "))
a = 1
b = 1
c = 1
print(1,end=',')
while count < n:
	if n != count+1:
		print(c,end=',')
	else:
		print(c)
	final = c
	a = b
	b = c
	c = a+b
	count = count+1
print("F%d = %d" %(n, final))
