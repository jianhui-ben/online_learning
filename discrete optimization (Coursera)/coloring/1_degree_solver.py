#!/usr/bin/python
# -*- coding: utf-8 -*-


def solve_it(input_data):
    import numpy as np
    import pandas as pd
    from numba import njit 
    from collections import namedtuple

    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    # solution
    constraint_order=[]

    ##first degree constraint_order
    for i in range(node_count):
        count=0
        for k in edges:
            if i in k:
                count+=1
        constraint_order.append((i, count))


    constraint_order=sorted(constraint_order, key=lambda x: x[1])

    fixed_order=[]
    for i in constraint_order:
        fixed_order.append(i[0])

    combined_edges=[]
    for i in range(node_count):
        close_nodes=[]
        for k in edges:
            if i in k:
                close_nodes.append(k[1-k.index(i)])
        combined_edges.append(close_nodes)
    
    
    total_color=node_count-1  ### at most 
    table=np.zeros((node_count, total_color))



    ###loop and search
##0: haven't tries
##1: decision
##-1: not feasible
    while constraint_order:
        constraint_pair= constraint_order.pop()
        node=constraint_pair[0]
        current_node_constraint= table[node]
        available_color_list = np.where(table[node]==0)  ##find all available colors
    
        if 0 in table[node]:
            color=available_color_list[0][0]  ##find the first avaiable color
            table[node][color]=1   ## color this node
            ##for other attched nodes, they cannot use the same color
            for other in combined_edges[node]:
                if 1 not in table[other]:
                    table[other][color]=-1      
            
        else:
            previous_node=fixed_order[fixed_order.index(node)+1]
            previous_color=np.where(table[previous_node]==1)[0][0]
            table[previous_node][previous_color]= -1
            for other in combined_edges[previous_node]:
                if 1 not in table[other] and other!=node:
                    table[other][previous_color]=0
            table[node]=current_node_constraint
        
            constraint_order.append(constraint_pair)
            constraint_order.append((previous_node, _))


    output=[]
    for i in range(node_count):
        output.append(np.where(table[i]==1)[0][0])

    total_color=len(set(output))  


    ### local search added:
    import random
    for i in range(3):
        output= local_search(output, combined_edges, edges)
    total_color=len(set(output))   



    # prepare the solution in the specified output format
    output_data = str(total_color) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, output))

    return output_data

def check_output(output,edges):
    for (a,b) in edges:
        if output[a]==output[b]:
            return False
    return True


def local_search(output,combined_edges, edges):
    import random
    total_color=len(set(output))
    #print('total_color', total_color)
    
    
    
    color_count=[output.count(i) for i in range(total_color)]
    
    possible_deleted_colors= [color for color in range(total_color) if color_count[color]==min(color_count)]
    random.shuffle(possible_deleted_colors)
    for deleted_color in possible_deleted_colors:
        original_output=[]
        for i in output:
            original_output.append(i)
            
        bad_nodes= [i for i, x in enumerate(output) if x ==deleted_color ]
        while bad_nodes:
            #print('bad nodes are', bad_nodes)
            new_bad=[]

            for bad_node in bad_nodes:
#                 print('currently dealling with bad node', bad_node)
                losses= []
                for new_color in range(total_color-1):
                    losses.append(len([conflict_node for conflict_node in combined_edges[bad_node] if output[conflict_node]==new_color]))
                possible_new_colors= [new_color for new_color, loss in enumerate(losses) if losses[new_color]==min(losses)]
                new_color=random.choice(possible_new_colors)
#                 print('bad_node',bad_node, 'possible_new_colors', possible_new_colors, 'randomly pick', new_color)
                output[bad_node]=new_color
                new_bad+=[conflict_node for conflict_node in combined_edges[bad_node] if output[conflict_node]==new_color]
#                 print('new bad', new_bad)
            bad_nodes=list(set(new_bad))
        
        if check_output(output, edges)==False:
            output=orginal_output
        else:
            break;
            
    if len(set(output))==total_color:
        #print('''can't be better''')
        return output
    else:
        return local_search(output, combined_edges, edges)


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

