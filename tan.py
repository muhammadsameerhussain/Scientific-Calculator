import sine
import cosine
def tan(x):
    if x==90:
        print("Math Error")
    else:
        return ((sine.sin(x))/(cosine.cos(x)))
