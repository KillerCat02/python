print ("Калькулятор от Кирилла! v1.0") #Выводит сообщение
print ("\(0.0)/") #Выводит сообщение


a=int(input()) #Вводим переменную a
b=int(input()) #Вводим переменную b
c=input("Введите знак(+,- и т.д ") #Вводим знак
d=1 #Костыль, без него код не работает
if c=="+": #Если переменная c равняется +, то..
    d=a+b
elif c=="-": #Если переменная c равняется +, то..
    d=a-b
elif c=="/": #Если переменная c равняется +, то..
    if b==0:
        print ("ДЕЛИТЬ НА 0 НЕЛЬЗЯ")
    else:
        d=a/b
elif c=="*": #Если переменная c равняется +, то..
    d=a*b
elif c=="%": #Если переменная c равняется +, то..
    d=a%b
elif с=="//" #Если переменная c равняется +, то..
    c=a//b
elif c=="**" #Если переменная c равняется +, то..
    c=a**b
print (d)

    