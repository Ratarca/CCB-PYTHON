"""
    Syntax

def external_func(*param):
    def internal_fun(*param)
        #pass
    
    # Can use internal_func
    # Can return internal_func

"""
# EX
def welcome(name)->str:

    def upper_txt(text:str)->str:
        return str.upper(text)

    return (f'Welcome {upper_txt(name)}')