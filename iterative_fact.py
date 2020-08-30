
def it_fact(x):
    result = 1
    for i in range(1, x+1):
        result = result * i
    return result

print(it_fact(5))
