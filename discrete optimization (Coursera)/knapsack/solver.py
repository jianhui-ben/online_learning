#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import numpy as np
from numba import njit

Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full

    ##orginal
    #value = 0
    #weight = 0
    #taken = [0]*len(items)

    #for item in items:
    #    if weight + item.weight <= capacity:
    #        taken[item.index] = 1
    #        value += item.value
    #        weight += item.weight


    ## swapping
    #for item_1 in items:
    #    if taken[item_1.index]==0:
    #        for item_2 in items:
    #            if taken[item_2.index]==1 and item_1.value>=item_2.value and weight - item_2.weight + item_1.weight<=capacity:
    #                taken[item_1.index]=1
    #                taken[item_2.index]=0
    #                value+= (item_1.value -item_2.value)
    #                weight+= (item_1.weight -item_2.weight)


    ## dynamic programming: consider the decision variables, constraints. Start from the most simple version
    ## What about a very small constraint and only one or two options for the decision variables.

    ###The following code is using the list to fulfill the dynamic programing
    
    #value_table=[]
    #for i in range(len(items)+1):
    #    value_list=[0]*(capacity+1) 
    #    if i!=0:
    #        if i<= len(items):
    #            item = items[i-1]
            

    #        for size in range(capacity+1):
             
    #            if size<item.weight:
    #                ### have to use value_list, and then append(value_list)
    #                value_list[size]=value_table[i-1][size]
    #                #value_table[i].append(value_table[i-1][size])
    #            elif size==item.weight and value_table[i-1][size]<=item.value:
    #                #value_table[i].append(item.value)
    #                value_list[size]=item.value
    #            else:
    #                value_list[size]=max(value_table[i-1][size], 
    #                                      item.value+value_table[i-1][size-item.weight])
    #    value_table.append(value_list)
    

    #value=value_table[item_count][capacity]

    #current_value=value
    #current_capacity=capacity
    #taken = [0]*len(items)
    #for current_i in range(item_count-1,-1,-1):
    #    if value_table[current_i][current_capacity]<current_value:
    #        taken[current_i]=1
    #        current_value=value_table[current_i][current_capacity-items[current_i].weight]
    #        current_capacity-=items[current_i].weight    
    
    
    ### dynamic programming using numba
    value,taken= fast_dp(items, item_count, capacity)            

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

    ### function of dynamic programming using numba
@njit(fastmath=True)    
def fast_dp(items, item_count, capacity):
    
    value_table=np.zeros((item_count+1, capacity+1))
    
    for i in range(1,(item_count+1)):
        item = items[i-1]
        
        for size in range(capacity+1):

            if size<item.weight:
                ### have to use value_list, and then append(value_list)
                value_table[i][size]=value_table[i-1][size]
#             elif size==item.weight and value_table[i-1][size]<=item.value:
#                 value_list[size]=item.value
            else:
                value_table[i][size]=max(value_table[i-1][size], 
                                      item.value+value_table[i-1][size-item.weight])
    
#     return value_table

    value=value_table[item_count][capacity]

    current_value=value
    current_capacity=capacity
    taken = [0]* item_count
    for current_i in range(item_count-1,-1,-1):
        if value_table[current_i][current_capacity]<current_value:
            taken[current_i]=1
            current_value=value_table[current_i][current_capacity-items[current_i].weight]
            current_capacity-=items[current_i].weight
#             print('this is',current_i, current_capacity,current_value,taken[current_i])
    return int(value), taken



if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
