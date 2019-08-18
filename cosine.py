import factorial
def cos(p):
    
    cos=0
    y=((p)*3.14)/180
    if p==0:
        return 1
    elif p==90:
        return 0
    else:
        for i in range(21):
            sign=(-1)**i
            p=2*i
            f=factorial.factorial(p)
            cos= cos+(((y)**(p))/f)*sign
    return cos
