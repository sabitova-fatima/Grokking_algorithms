def recursive_fact(x):
    if x == 0:
        return 1
    else:
        result = x * recursive_fact(x-1)
    return result

print(recursive_fact(5))
