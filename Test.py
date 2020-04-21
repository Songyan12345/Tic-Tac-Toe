#program to convert adjacency list to adjacency matrix

import sys

row_count = 0
column_count = 0
for line in sys.stdin:
    if line != "0\n":
        if line != "\n":
            if row_count == 0:
                row_count = int(line)
                column_count = int(line)
                sys.stdout.write(str(row_count) + "\n")
            else:
                string = ""
                nodes_list = [int(i) for i in line.split()]
                for i in range(column_count):
                    if i in nodes_list:
                        if i != (column_count - 1): #check if end of row
                            string += "1" + " "
                        else:
                            string += "1" + "\n" 
                    else:
                        if i != (column_count - 1):
                            string += "0" + " "
                        else:
                            string += "0" + "\n" 
                row_count -= 1
                sys.stdout.write(string)
        else:
            string = ""
            for i in range(column_count):
                if i != (column_count - 1):
                    string += "0" + " "
                else:
                    string += "0" + "\n"
            row_count -= 1
            sys.stdout.write(string)
    else:
        sys.stdout.write(line)
        break
                            
    
    
