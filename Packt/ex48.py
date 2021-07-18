def sum_first_n(n):
    total = 0
    for num in range(n):
        total += num+1
    return total

print(sum_first_n(100))
