import math
import os
import random
import re
import sys
sys.setrecursionlimit(1000000)
#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#
count=0
def countLuck(matrix, k):
    # Write your code here
    r=len(matrix)
    c=len(matrix[0])
    global count
    count=0
    #convert strings to individual cell
    for i in range(r):
        matrix[i]=list(matrix[i])
     
    xi=[0,0,1,-1]
    yi=[1,-1,0,0]
    #check number of adjacent passable cells
    def neighbour(i,j):
        temp=0
        for x,y in zip(xi,yi):
            if 0<=i+x<r and 0<=j+y<c and matrix[i+x][j+y]!='X':
                temp+=1
        return temp
        
        
    def dfs(i,j,matrix):
        global count
        if  matrix[i][j]=="*":
            return True
        #make the cell visited by placing 9
        matrix[i][j]='v'
        flag=False
        for x,y in zip(xi,yi):
            if 0<=i+x<r and 0<=j+y<c and matrix[i+x][j+y] in ['.','*']:
                flag=dfs(i+x,j+y,matrix)
                if flag==True:
                    matrix[i][j]="0"
                    #placing the wand
                    count+=1 if neighbour(i,j)>2 else 0
                    return flag
        #make the cell passable
        matrix[i][j]="."
        return flag
    
        
        
    flag=False
    for i in range(r):
        for j in range(c):
            if matrix[i][j]=="M":
                matrix[i][j]="."
                flag=dfs(i,j,matrix)
                #check for source cell
                count-=1 if neighbour(i,j)>2 else 0
                count+=1 if neighbour(i,j)>1 else 0
                break
    if flag and count==k:
        return "Impressed"        
    else:
        return "Oops!"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
