#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER rows
#  2. INTEGER cols
#  3. INTEGER initR
#  4. INTEGER initC
#  5. INTEGER finalR
#  6. INTEGER finalC
#  7. INTEGER_ARRAY costRows
#  8. INTEGER_ARRAY costCols
#


def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    global visit
    queue=[[initC,initR]]
    visit[initC][initR]=1
    direct=[[1,0],[0,1],[-1,0],[0,-1]]
    while queue :
        c = queue[0][0]
        r = queue[0][1]
        queue.pop(0)
        for d in direct :
            dr = r + d[0]
            dc = c + d[1]
            if 0<=dr<rows and 0<=dc<cols and visit[dc][dr]==0 :
                if dr == r and r<rows:
                    visit[dc][dr] = visit[c][r] + costRows[c]
                elif dc == c and c<cols:
                    visit[dc][dr] = visit[c][r] + costCols[r]
                queue.append([dc,dr])
    return visit[finalR][finalC]-1


rows = int(input().strip())

cols = int(input().strip())

initR = int(input().strip())

initC = int(input().strip())

finalR = int(input().strip())

finalC = int(input().strip())

costRows_count = int(input().strip())

costRows = []

for _ in range(costRows_count):
    costRows_item = int(input().strip())
    costRows.append(costRows_item)

costCols_count = int(input().strip())

costCols = []

visit=[[0]*cols for _ in range(rows)]

for _ in range(costCols_count):
    costCols_item = int(input().strip())
    costCols.append(costCols_item)

result = minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols)

print(result)
