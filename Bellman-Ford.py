#implementing shortest distance using Bellman-Ford shortest paths algorithm

import sys
import math

#R = 10000

def print_result(prev, location_list):
    index = len(location_list) - 1
    path = []
    string = ""
    try:
        path.append(location_list[index])
        while index != 0:
            path.append(location_list[prev[index]])
            index = prev[index]
        path.reverse()
        for element in path:
            string = string + ", " + element
        string = string[2:]
        print(string)
    except:
        print("Not possible")
        
def shortest_path(G, s):
    prev = [None] * len(G)
    prev[s] = 0
    dist = [float("Inf")] * len(G)
    dist[s] = 0
    for l in range(len(G)):
        for m in range(len(G)):
            for n in range(len(G[s])):
                if G[m][n] == float("Inf"):
                    continue
                elif G[m][n] != float("Inf"):
                    if dist[n] < dist[m] + G[m][n]:
                        continue
                    elif (dist[m] + G[m][n]) < dist[n]:
                        prev[n] = m
                        dist[n] = dist[m] + G[m][n]
                    else:
                        continue
                else:
                    break
    return prev
        
def input_data():
    M = []
    row_count = 0
    location_list = []
    line = sys.stdin.readline().rstrip()
    test_cases = int(line)
    while test_cases > 0 and row_count == 0:
        line = sys.stdin.readline().rstrip()
        row_count = int(line)
        for i in range(row_count):
            line = sys.stdin.readline().rstrip().split()
            line[0] = float(line[0])
            line[1] = float(line[1])
            if len(line) > 3:
                line[2] = line[2] + " " + line[3]
                line.pop()
            M.append(line)
            location_list.append(line[2])
        fuel = float(sys.stdin.readline().rstrip())
        G=[[0 for i in range(row_count)] for j in range(row_count)]
        for i in range(row_count):
            for j in range(row_count):
                lat = math.radians(M[j][0] - M[i][0])
                lng = math.radians(M[j][1] - M[i][1])
                a = (math.sin((lat/2)) ** 2) + (math.cos(math.radians(M[i][0])) * math.cos(math.radians(M[j][0])) * (math.sin((lng/2)) ** 2))
                c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
                d = R * c
                if d <= fuel:
                    G[i][j] = d
                else:
                    G[i][j] = float("Inf")
        prev = shortest_path(G, 0)
        print_result(prev, location_list)
        row_count = 0
        M = []
        G = []
        location_list = []
        test_cases -= 1
        
input_data()    

                
                    
    

                            
    
    
