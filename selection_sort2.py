# function, that finds the smallest number out of given list
# would be better to use min(), but no

def find_smallest(my_list):
    smallest = my_list[0]

    for i in range(len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return(smallest)


# selection sort

# for i in list - find the smallest, add it to new list, remove from the old one

def selection_sort(my_list):
    new = []
    for i in range(len(my_list)):
        smallest = find_smallest(my_list)
        new.append(smallest)
        my_list.remove(smallest)

    return new


my_list = [1,2,6,4,5]
sorted_list = selection_sort(my_list)

print(sorted_list)
