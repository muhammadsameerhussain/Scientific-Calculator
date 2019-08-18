from rad_deg import rad
def acos(x):
    b=((22/7)/2)-x-((1/6)*(x**3))-((3/40)*(x**5))-((5/112)*(x**7))
    c=rad(b)
    return c
