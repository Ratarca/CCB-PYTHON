"""
    __MagicMethods__

https://dbader.org/blog/python-dunder-methods
dir(object)

================
    str      :
    repr     :
    len      :
    getitem  :
    reversed :
    eq       :
    lt       :
    call     :
    add      :

"""

class forest():
    def __init__(self):
        pass

    def __str__(self):
        return "NOTHING"

amazonia = forest()
print(amazonia.__str__)