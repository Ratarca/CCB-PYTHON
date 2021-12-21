"""
    Syntax

# Optional
# Args
# Kwargs
"""

# Default param
def minus_vals(val_1:int, val_2 = 0) ->int:
    return  val_1 - val_2


# Optional param
def sum_vals(val_1:int, *val_2:int)->int:
    """
        Sum two integer vals.
        
        ex:
            sum_vals(1,2) -> 3
    """
    return val_1 + val_2

# "Args" you need only *some_tuple
def show_args(name:str = "Ratarca", *args):
    print(args, type(args), len(args))
    return name

show_args('Nothing1',[1,2,3,5,6,8])
show_args('Nothing2',[1,2,3,5,6,8],777)
show_args('Nothing3',[1,2,3,5,6,8],777,999)

# "Kwargs" you need only **some_dict
def show_kwargs(name:str = "Ratarca", **kwargs):
    print("\n")
    print(type(kwargs))
    print(kwargs)
    print(kwargs.items())
    return name

show_kwargs()
show_kwargs('rafa',middle='targino',another = 10)