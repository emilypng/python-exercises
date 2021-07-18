
def fib_recursive(n):
    if n<2:
        return n
    else:
        return fib_recursive(n-2)+fib_recursive(n-1)

user_input = eval(input("Enter a number to take the factorial of: "))
input_factorial = fib_recursive(user_input)
print(input_factorial)
