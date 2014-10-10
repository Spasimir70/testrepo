def sevens_in_a_row(arr, n):
	br = 0
	for i in range(arr):
		if arr[i] == 7:
			br += 0
	return br == n

def main():
	array = list()
	num = int(input("Enter how many elements you want: "))
	print ('Enter number in array:')
	for i in range(num):
		n = input("num :")
		array.append(int(n))
	print ('ARRAY: ', array)

	num_of_sevens = int(input("Enter number of sevens"))
	print sevens_in_a_row(array, num_of_sevens)


if __name__ == '__main__':
	main()
 