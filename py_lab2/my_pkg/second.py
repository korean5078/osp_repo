#!/usr/bin/python3

def unionintersection(input2, input3):
	list1 = input2.strip('[]')
	newlist = list1.split(',')
	newlist = list(map(int,newlist))
	list2 = input3.strip('[]')
	newlist2 = list2.split(',')
	newlist2 = list(map(int,newlist2))
	union = newlist + newlist2
	union = list(set(union))
	union = sorted(union)
	intersection = list(set(newlist).intersection(newlist2))
	print("=> union",end=' ')
	print(union)
	print("=> intersection",end=' ')
	print(intersection)
	return 0
