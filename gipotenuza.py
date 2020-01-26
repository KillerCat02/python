a=int(input ("Введите первое число ") ) #
b=int(input ("Введите второе число ") )
j=int(input ("Введите третье число ") )
D=b*b-4*a*j
if D>0:
    x1=(-b-D**0.5)/(2*a)
    x2=(-b+D**0.5)/(2*a)
    print (x1,x2)
elif D==0:
    x=-b/2*a
    print (x)
elif D<0:
    print ("Корня нету")

    
