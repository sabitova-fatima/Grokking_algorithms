
def biggest(x):
    biggest = x[0]

    for i in x:
        if i > biggest:
            biggest = i
    return biggest

my_list = [1,2,3,4,5]

print(biggest(my_list))
