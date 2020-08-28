def find_smallest(my_list):
    smallest = my_list[0]
    smallest_index = 0

    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
            smallest_index = i
        return smallest_index

def selection_sort(my_list):
    new_list = []
    for i in range(len(my_list)):
        smallest = find_smallest(my_list)
        new_list.append(my_list.pop(smallest))
    return new_list

print(selection_sort([5,3,6,2,10]))

