from factorial import factorial
from per import nPr
def nCr(n,r):
    b= (nPr(n,r))/factorial(r)
    return b
    
