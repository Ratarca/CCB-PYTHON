"""
    Syntax
myDict = {val1, ... , valN}


    #Methods
- add
- discard
- union
- difference
- intersection
- insersection_update
"""

assetsA = {"ITUB4","PETR4","VALE3"}
assetsB = {"BPAC11", "VALE3","MODL11"}


assetsC = assetsA.union(assetsB)
assetsD = assetsA.difference(assetsB)
assetsE = assetsA.intersection(assetsB)
assetsF = assetsA.intersection_update(assetsB)

wallet = [assetsA, assetsB, assetsC, assetsD, assetsE, assetsF]
for asset in wallet:
    print(asset,'\n')


print(assetsA.add("WEGE3"))
print(assetsB.discard("MOLD11"))

