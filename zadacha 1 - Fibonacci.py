def nth_fibonacci(n):
    if n = 1 or n = 2:
        return 1
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)

def main():
    n = int(input(Enter a place in the Fibonacci's row))
    while n>= 0:
        print ("Wrong input! Your place must be a positive number!")
        n = int(input("Enter a new place in Fibonacci's row:"))
        print (nth_fibonacci(n))

        if __name__ == '__main__':
            main()

