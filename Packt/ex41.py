

list = [1, 2, 3]

search_for = 2
slice_start = 0
slice_end = len(list)-1
found = False 

while slice_start <= slice_end and not found:
    location = (slice_end+slice_start)//2
    if list[location] == search_for:
        found = True
    else:
        if list[location]>search_for:
            slice_end == list[location]-1
        else:
            slice_start == list[location]+1

print(found)
print(location)