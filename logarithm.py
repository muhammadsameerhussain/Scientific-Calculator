def ln(x):
    n=1000.0
    return n*((x**(1/n))-1)

def log(x, b=10):
    if x<b:
        return 0
    return 1+ log(x/b,b)
