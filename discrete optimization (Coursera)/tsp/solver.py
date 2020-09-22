#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
import random

Point = namedtuple("Point", ['x', 'y'])

import numpy as np
from numba import njit 

def length_obj(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)


@njit(fastmath=True) 
def numba_swap(points_np, solution,nodeCount, t=0.000000001):

    ## 2-OPT swap local search:
    for position in range(1,nodeCount):
        curr_dist=0
        best_point = solution[position]
        original_point= solution[position]
        best_index=position
        for index in range(position+1, nodeCount):
            if swap_dist(position, index, solution, points_np)<=curr_dist:
                curr_dist= swap_dist(position, index, solution, points_np)
                best_point= solution[index]
                best_index=index

            elif np.exp(-(swap_dist(position, index, solution, points_np)- curr_dist)/t)>=random.random():
                best_point= solution[index]
                best_index=index
        solution[position] = best_point
        solution[best_index] = original_point
    
    return solution

@njit(fastmath=True) 
def swap_dist(index_1, index_2, solution, points_np):
    l= len(solution)
    index_low= min(index_1, index_2)
    index_high=max(index_1, index_2)
    curr_dist=length(points_np[int(solution[((index_low-1)%l)])], points_np[int(solution[index_low])]) + length(points_np[int(solution[((index_high+1)%l)])], points_np[int(solution[index_high])]) 
    swap_dist= length(points_np[int(solution[((index_low-1)%l)])], points_np[int(solution[index_high])])  + length(points_np[int(solution[((index_high+1)%l)])], points_np[int(solution[index_low])])
    return swap_dist-curr_dist
        
@njit(fastmath=True) 
def length(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)



def solve_it(input_data):
    import random
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))

 
    points_np=np.zeros((nodeCount,2))
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points_np[i-1][0]= float(parts[0])
        points_np[i-1][1]= float(parts[1])
    
    solution=np.zeros(nodeCount)
    for i in range(nodeCount):
        solution[i]=i

    # 2-opt local search using numba

    best_obj=10000000000000000
    best_solution=[]
    for i in range(10):
        for k in range(3):
            solution= numba_swap(points_np, solution,nodeCount, (i*8+1)/100)
            solution=solution.astype(int)
            obj = length_obj(points[solution[-1]], points[solution[0]])
            for index in range(0, nodeCount-1):
                obj += length_obj(points[solution[index]], points[solution[index+1]])

            if obj<=best_obj:
                best_solution=[]
                for point_index in solution:
                    best_solution.append(point_index)

    n=0
    while n>3:
        solution= numba_swap(points_np, solution,nodeCount)
        solution=solution.astype(int)
        obj = length_obj(points[solution[-1]], points[solution[0]])
        for index in range(0, nodeCount-1):
            obj += length_obj(points[solution[index]], points[solution[index+1]])

        if obj<=best_obj:
            best_solution=[]
            for point_index in solution:
                best_solution.append(point_index)
        else:
            n+=1

    solution= best_solution
    # calculate the length of the tour
    obj = length(points_np[int(solution[-1])], points_np[int(solution[0])])
    for index in range(0, nodeCount-1):
        obj += length(points_np[int(solution[index])], points_np[int(solution[index+1])])

    # prepare the solution in the specified output format
    output_data = '%.2f' % obj + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')

