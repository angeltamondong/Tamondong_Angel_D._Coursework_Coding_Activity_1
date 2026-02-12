def collatz(n):
    if n % 2 == 0:
        even = n // 2
        print("Even:", even)
        return even
    else:
        odd = 3 * n + 1
        print("Odd:", odd)
        return odd

# Main program
n = int(input("Enter a number: "))
while n != 1:
    n = collatz(n)