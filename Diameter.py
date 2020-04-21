#calculates diameter of graph using breadth-first search

import sys
import queue

def bfs(count, adjacency_list):
    distance = []
    zero_count = 0
    is_connected = True
    for s in range(count):
        q = queue.Queue()
        d = [0] * count
        colour = ["white"] * count
        bfsvisit(s, colour, d, q, adjacency_list)
        for element in d:
            if element == 0:
                zero_count += 1
                if zero_count >= 2:
                    is_connected = False
                    break
        distance.append(d)
        zero_count = 0
    return is_connected, distance

def bfsvisit(start, colour, d, queue, adjacency_list):
    d[start] = 0
    colour[start] = "grey"
    queue.put(start)
    while not queue.empty():
        u = queue.get()
        next_node = adjacency_list[u]
        for v in next_node:
            if colour[v] == "white":
                colour[v] = "grey"
                d[v] = d[u] + 1
                queue.put(v)
        colour[u] = "black"


adjacency_list = []
count = 0
graph = 0
is_connected = True

for line in sys.stdin:
    if line.strip() != "0":
        adjacency_list = []
        count = int(line)
        graph += 1
        for i in range(count):
            adjacency_list.append(list(map(int,sys.stdin.readline().strip().split())))
        for element in adjacency_list:
            if len(element) == 0:
                is_connected = False;
        if is_connected == False and count >= 2:
            sys.stdout.write("Graph " + str(graph) + " is disconnected.\n") 
            is_connected = True
            count = 0
        elif is_connected == False and count == 1:
            sys.stdout.write("Graph " + str(graph) + " has diameter 0.\n")
            is_connected = True
            count = 0
        else:
            is_connected, order = bfs(count, adjacency_list)
            if is_connected == True:
                max_order = max(map(max, order))
                sys.stdout.write("Graph " + str(graph) + " has diameter " + str(max_order) + ".\n")
                is_connected = True
                count = 0
            else:
                sys.stdout.write("Graph " + str(graph) + " is disconnected.\n") 
                is_connected = True
                count = 0
    else:
        break
                    
    

                            
    
    
