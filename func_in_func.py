def greater(a,b):
    if (a>b):
        return a
    else:
        return b
def greatest(a,b,c):
    if a>b and b>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
def new_greater(a,b,c):
    bigger=greater(a,b)
    return greater(bigger,c)
print(new_greater(10,20,30))