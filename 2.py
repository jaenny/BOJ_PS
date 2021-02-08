#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'taxiDriver' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY pickup
#  2. LONG_INTEGER_ARRAY drop
#  3. INTEGER_ARRAY tip
#

def taxiDriver(pickup, drop, tip):
    # Write your code here
    print(pickup)
    print(drop)
    print(tip)
    dp=[0]*len(pickup)
    for i in range(len(pickup)) :
        res=[]
        for j in range(i) :
            if pickup[i] >= drop[j] :
                res.append(dp[j])
            elif drop[i] <= pickup[j] :
                res.append(dp[j])
        if len(res)!=0 :
            dp[i] = max(res) + drop[i] - pickup[i] + tip[i]
        else :
            dp[i] = drop[i] - pickup[i] + tip[i]
        print(dp)
    return max(dp)


pickup_count = int(input().strip())

pickup = []

for _ in range(pickup_count):
    pickup_item = int(input().strip())
    pickup.append(pickup_item)

drop_count = int(input().strip())

drop = []

for _ in range(drop_count):
    drop_item = int(input().strip())
    drop.append(drop_item)

tip_count = int(input().strip())

tip = []

for _ in range(tip_count):
    tip_item = int(input().strip())
    tip.append(tip_item)

result = taxiDriver(pickup, drop, tip)

print(result)
