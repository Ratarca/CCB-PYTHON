"""
    Syntax

# basic
nameFunction = lambda x : x

# Using if and else
# Nested if
# map / filter / reduce

"""
from functools import reduce

# EX 1
force_round = lambda x : round(x,2)
number = 3.14159265359

print(force_round(number))

# EX 2
check_balance = lambda balance : True if balance > 0 else False

# EX 3 
f = lambda x: 1 if x>0 else 0 if x ==0 else -1

# EX 4 : map, reduce and filter
inflationRate = [2, 3, 2, 2.5, 5, 6, 7, 8,
                 9, 10, 12, 14, 10, 12,
                 9, 8, 7, 5, 5, 5]


multi_inflation = lambda x : x*2

sum_vals = lambda x,y : x+y
get_high = lambda x,y : x if (x>y) else y

goal_inflation = lambda x : x<=5

# Map: apply function for each elements
inflationRate2 = list( map(multi_inflation, inflationRate) )

# Reduce : Apply function on all values and return only one value (agg function)
inflationRate3 = reduce(sum_vals, inflationRate)
inflationRate4 = reduce(get_high, inflationRate)

# Filter: Filter elements
inflationRate5 = list( filter(goal_inflation, inflationRate) )

print(inflationRate5) # Test for each inflation list!