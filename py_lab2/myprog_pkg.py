#!/usr/bin/python3
import my_pkg

while True:
	start = int(input("Select menu: 1) conversion 2) union/intersection 3) exit ? "))
	if (start == 1):
		input1 = input("input binary number : ")
		n1 = '0b' + input1
		my_pkg.conversion(n1)
	elif (start == 2):
		input2 = input("1st list: ")
		input3 = input("2nd list: ")
		my_pkg.unionintersection(input2, input3)
	elif (start == 3):
		print("exit the program...")
		break
	else:
		print("wrong menu")
