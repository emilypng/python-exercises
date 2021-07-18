# example of terminating case

def print_next_number(n):
    print(n+1)
    if n >= 7:
        return "I'm bored."
    return print_next_number(n+1)

print(print_next_number(5))

# recursive countdown
def countdown(n):
    if n==0:
        print("Lift off!")
    else:
        print(n)
        return countdown(n-1)

print("Enter a number to coundown from: ")
number = int(input())

countdown(number)