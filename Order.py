#calculates maximum order in graph using depth-first search

import sys
import queue

def dfs(count, adjacency_list):
    visited_nodes = []
    for start in range(count):
        colour = ["white"] * count
        dfsvisit(start, colour, adjacency_list)
        visited_nodes.append(colour.count("black"))
    return visited_nodes

def dfsvisit(start, colour, adjacency_list):
    colour[start] = "black"
    for element in adjacency_list[start]:
        if colour[element] == "white":
            dfsvisit(element, colour, adjacency_list)
    colour[start] = "black"

adjacency_list = []
count = 0
graph = 0

for line in sys.stdin:
    if line.strip() != "0":
        adjacency_list = []
        count = int(line)
        graph += 1
        for i in range(count):
            adjacency_list.append(list(map(int,sys.stdin.readline().strip().split())))
        if count != 1:
            order = dfs(count, adjacency_list)
            max_order = max(order)
            sys.stdout.write("Graph " + str(graph) + " has a component of order " + str(max_order) + ".\n")
            count = 0
        else:
            sys.stdout.write("Graph " + str(graph) + " has a component of order 1.\n") 
            count = 0
    else:
        break
                    
    

                            
    
    
