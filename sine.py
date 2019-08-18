import factorial
def sin(p):# SINE
    sin=0
    if p==180 and p==360:
        return 0
    elif p==90:
        return 1
    else:
        y=((p)*3.14)/180
        for i in range(21):
            sign=(-1)**i
            p=2*i+1
            f=factorial.factorial(p)
            sin=sin+(((y)**(p))/f)*sign
    return sin
