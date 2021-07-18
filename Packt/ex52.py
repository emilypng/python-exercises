stored_results = {}
def sum_to_n(n):
    result = 0
    for i in reversed(range(n)):
        result += i + 1
    stored_results[n] = result # storing result in dictionary
    return result 


def sum_to_n_dynamic(n):
    result = 0
    for i in reversed(range(n)):
        if i+1 in stored_results:
            print("stopping because we previously printed {}".format(str(i+1)))
            result += stored_results[i+1]
            break
        else:
            result += i + 1
    stored_results[n] = result
    return result

print(sum_to_n(3))
print(sum_to_n_dynamic(4))