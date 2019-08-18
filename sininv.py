from rad_deg import rad
def asin(x):
    b= x +((1/6)*(x**3))+((3/40)*(x**5))-((5/112)*(x**7))+((35/1152)*x**9)
    c=rad(b)
    return c
