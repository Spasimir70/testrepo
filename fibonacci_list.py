def nth_fib_lists(listA, listB, n):
	if n == 1
	   return listA
	elif n == 2:
	   return listB
	else:
	   return nth_fib_lists(listA, listB, n-1) + nth_fib_lists(listA, listB, n-2)

print(nth_fib_lists([1, 2], [1, 3], 6))

