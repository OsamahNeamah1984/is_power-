def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


def is_power(x, y):
    """ Every number to power zero equal to 1 """
    if x == 1:
        return True
    """ Any number to power 1 equal to itself """
    if (x==y):
        return True
    """ No number other than 1 is power of 1 """
    if y ==  1:
        return False
    """" if x%y not equal to 0 then x is not power of y """
    if  not is_divisible(x,y):
        return False
    """ recurisive call to x/y,y for sequence """
    return is_power(x/y, y)  
