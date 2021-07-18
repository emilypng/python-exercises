# iterative solution uses a loop

def iterative(n):
    product = 1
    for i in range (n):
        product = product * (i+1)
    return product

print(iterative(3))
print("Enter a number to get the factorial of: ")
input = int(input())
print(iterative(input))

def recursive(n):
    if n <=1: #base case
        return 1
    else:
        return n*recursive(n-1)
    