#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alicePoints = 0
    bobPoints = 0

for alice in a:
  for bob in b:
    print(x, y)    
    compare(alice, bob)   
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

