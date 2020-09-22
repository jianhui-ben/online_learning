## find min and max in a single traversal

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    return get_clean_min_max([i for i in ints if i is not None])  ##clean the ints list

def get_clean_min_max(ints):
    if len(ints)==0:
        return (None, None)
    minimum, maximum= ints[0], ints[0]  
    for i in ints:
        if i<minimum:
            minimum= i
        if i>maximum:
            maximum= i
    return (minimum, maximum)

       


## Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

##test case 2
get_min_max([])  ##(None, None)

##test case 3
get_min_max([None])