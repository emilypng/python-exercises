list = [5, 8, 1, 3, 2]
still_going = True
while still_going:
    for num in range(len(list)-1):
        if list[num] > list[num+1]:
            list[num], list[num+1] = list[num+1],list[num]
            still_going = True
    still_going = False
print(list)