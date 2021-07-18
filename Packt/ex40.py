list = [5, 8, 3, 1, 2]

searching_for = 8

result = -1

for num in range(len(list)):
    if searching_for == list[num]:
        result = num
        break
print(result)