# playing with *args and **kwargs

def convert_cad_to_usd(amount, rate=0.8):
    return(amount*rate)

def convert_and_sum(cad_list, rate=0.8):
    total=0
    for amount in cad_list:
        total += convert_cad_to_usd(amount, rate=rate)
    return total

print(convert_and_sum([1,3]))

def convert_and_sum_kwargs(cad_list, **kwargs):
    total=0
    for amount in cad_list:
        total+=convert_cad_to_usd(amount, **kwargs)
    return total

print(convert_and_sum_kwargs([1,3]))

def sum_of_numbers_args(*args):
    total = 0
    for numbers in args:
        total += numbers
    return total
print(sum_of_numbers_args(1,2,3,4,5,6,7,8))

def sum_of_numbers(list):
    total=0
    for num in list:
        total += num
    return total
print(sum_of_numbers([1,2,3,4,5,6,7,8,]))

def personal_details(**kwargs):
    print("Personal Details:")
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))

print(personal_details(firstName = "Jason", lastName = "Scott", country = "US"))

input_dict = {'name' : 'Vikas Singh' , 'gender' : 'Male'}
personal_details(**input_dict)

def person_details(dict):
    print("Personal Details:")
    for key, value in dict.items():
        print("{}:{}".format(key,value))

dictionary = {'name' : 'Vikas Singh' ,
             'gender' : 'Male'}

print(person_details(dictionary))
