from tkinter import *
import MainFuncs as m
import equals as e
import clear as cc
import click as c
import delete as d
cal =Tk()
cal.title('CALCULATOR')
m.s =StringVar()


m.txtDisplay = Entry(cal,font=('Helevetica',20), textvariable=m.s, relief=FLAT, bd=7, insertwidth=4, bg="powderblue", justify='right').grid(row=0,columnspan=90)

# ROW 1
RAD=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="RAD", command= lambda:('deg(')).grid(row=1,column=0)

DEG=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="DEG",command=lambda:c.click('rad(')).grid(row=1,column=1)

SQROOT=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="√",command=lambda:c.click('sqroot(')).grid(row=1,column=2)

CUBEROOT=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="3√",command=lambda:c.click('cuberoot(')).grid(row=1,column=3)

ROOT=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="n√",command=lambda:c.click('root(')).grid(row=1,column=4)

FAC=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="x!",command=lambda:c.click('factorial(')).grid(row=1,column=5)

BRA1=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="(",command=lambda:c.click('(')).grid(row=1,column=6)

BRA2=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text=")",command=lambda:c.click(')')).grid(row=1,column=7)

COMMA=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text=",",command=lambda:c.click(',')).grid(row=1,column=8)

CLEAR=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="CE",command=lambda:cc.clear()).grid(row=1,column=9)


# ROW 2
INV=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="INV",command=lambda:c.click('inv(')).grid(row=2,column=0)

SIN=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="Sin",command=lambda:c.click('sin(')).grid(row=2,column=1)

SININV=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="SinInv",command=lambda:c.click('asin(')).grid(row=2,column=2)

cosec=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="Cosec",command=lambda:c.click('cosec(')).grid(row=2,column=3)

QUAD=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="Quad(a,b,c)",command=lambda:c.click('quad(')).grid(row=2,column=4)

ABS=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="|x|",command=lambda:c.click('abs(')).grid(row=2,column=5)

btn7=Button(cal,padx=15,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="7",command=lambda:c.click(7)).grid(row=2,column=6)

btn8=Button(cal,padx=15,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="8",command=lambda:c.click(8)).grid(row=2,column=7)

btn9=Button(cal,padx=15,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="9",command=lambda:c.click(9)).grid(row=2,column=8)

DIVIDE=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="÷",command=lambda:c.click('/')).grid(row=2,column=9)

# ROW 3
PI=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="π",command=lambda:c.click(3.142)).grid(row=3,column=0)

COS=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="Cos",command=lambda:c.click('cos(')).grid(row=3,column=1)

COSINV=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="CosInv",command=lambda:c.click()).grid(row=3,column=2)

SEC=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="Sec",command=lambda:c.click('sec(')).grid(row=3,column=3)

nCr=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="nCr", command=lambda:c.click('nCr(')).grid(row=3,column=4)

SIGN=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text='+/-',command=lambda:c.click('sign(')).grid(row=3,column=5)

btn4=Button(cal,padx=15,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text='4',command=lambda:c.click(4)).grid(row=3,column=6)

btn5=Button(cal,padx=15,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text='5',command=lambda:c.click(5)).grid(row=3,column=7)

btn6=Button(cal,padx=15,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text='6',command=lambda:c.click(6)).grid(row=3,column=8)

MULTIPLY=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text='×',command=lambda:c.click('*')).grid(row=3,column=9)

# ROW 4
E=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="e",command=lambda:c.click(2.718281828)).grid(row=4,column=0)

TAN=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="Tan",command=lambda:c.click('tan(')).grid(row=4,column=1)

TANINV=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="TanInv",command=lambda:c.click('atan(')).grid(row=4,column=2)

Cot=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="Cot",command=lambda:c.click('cot(')).grid(row=4,column=3)

pnr=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
        text="nPr",command=lambda:c.click('nPr(')).grid(row=4,column=4)

LN=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="ln",command=lambda:c.click('ln(')).grid(row=4,column=5)

btn1=Button(cal,padx=15,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="1",command=lambda:c.click(1)).grid(row=4,column=6)

btn2=Button(cal,padx=15,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="2",command=lambda:c.click(2)).grid(row=4,column=7)

btn3=Button(cal,padx=15,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="3",command=lambda:c.click(3)).grid(row=4,column=8)

SUBTRACTION=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="-",command=lambda:c.click('-')).grid(row=4,column=9)

# ROW 5
OFF=Button(cal,padx=6,bd=0,bg='crimson',fg='white',font=('Imprint MT Shadow',11, ),
            text="OFF",command=quit).grid(row=5,column=0)

DEL=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="Del",command=lambda:d.delete()).grid(row=5,column=1)

SQUARE=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="x^2",command=lambda:c.click('sq(')).grid(row=5,column=2)

CUBE=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="x^3",command=lambda:c.click('cube(')).grid(row=5,column=3)

POWER=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="x^n",command=lambda:c.click('power(')).grid(row=5,column=4)


LOG=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="log",command=lambda:c.click('log(')).grid(row=5,column=5)

btn0=Button(cal,padx=15,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="0",command=lambda:c.click('0')).grid(row=5,column=6)

DECIMAL=Button(cal,padx=15,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text=".",command=lambda:c.click('.')).grid(row=5,column=7)

EQUALS=Button(cal,padx=15,bd=0, bg='SKYblue',fg='black',font=('Imprint MT Shadow',11, ),
            text="=",command=lambda:e.equals()).grid(row=5,column=8)

ADDITION=Button(cal,padx=6,bd=0,fg='black',font=('Imprint MT Shadow',11, ),
            text="+",command=lambda:c.click('+')).grid(row=5,column=9)






cal.mainloop()
