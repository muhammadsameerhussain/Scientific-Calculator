from sine import sin
from cosine import cos
def cot(x):
    if x==0:
        return "Math Error"
    else:
        return ((cos(x))/(sin(x)))
