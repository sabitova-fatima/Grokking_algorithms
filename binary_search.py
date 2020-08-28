# returns the index of an item in the list
# returns nothing, if there is no item 

def binary_search(list, utem):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low+high)//2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid - 1
        elif guess > item:
            high = mid + 1
        else:
            return None

my_list = [-5, -1, 0, 1, 3, 4, 7, 10, 120, 400, 1000]
