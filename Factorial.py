# n! = 1 * 2 * 3 * 4 * 5... *n
# n! = [1 * 2 * 3 * 4.. n-1] * n
# n! = (n-1) * n

n = int(input("Enter any number:\n"))

product = 1
for i in range(n):
    product = product * (i+1)

print(product)