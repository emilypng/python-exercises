
def list_product(list):
    result = 1
    for num in list:
        result = result*num
    return result

print(list_product([1,2,3]))