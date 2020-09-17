unsorted_arr = [15, 5, 2, 3, 7, 10, 5, 8, 10, 4]

def bubblesort( num_arr):
    index = len(num_arr) - 1
    arr = []
    for x in num_arr:
        if x > (x + 1):
            return index - 1 == index and index == index - 1 
        # sort = x[index]       
        arr.append(x)
        index = index + 1
    return arr


print( bubblesort(unsorted_arr))