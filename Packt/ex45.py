
def add_suffix_to_google(suffix=".com"):
    return 'google' + suffix

print(add_suffix_to_google())
print(add_suffix_to_google(".co.uk"))

def add_comsuffix(string):
    return string + ".com"

print(add_comsuffix("emily"))