"""
    Syntax

for val in iterator:
    #Do something
"""

env = ['EQUITY_RESEARCH','DATA_SCIENCE','RISK']

print("\n Example 1")
for v in env:
    print(f'Welcome {v}')

print("\n Example 2")
for idx,val in enumerate(env):
    print(idx, val)

print("\n Example 3")
for idx,val in enumerate(env):
    for idx2,val2 in enumerate(env):
        print(idx, idx2, val , val2)