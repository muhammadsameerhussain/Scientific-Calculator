from rad_deg import rad
def atan(x):
    b= x-((1/3)*(x**3))+((1/5)*(x**5))-((1/7)*(x**7))
    c=rad(b)
    return c
