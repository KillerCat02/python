from tkinter import *
import time
import datetime

root = Tk()
c = Canvas(root,
           width = 800,
           height=600,
           bg='#0000FF')
c.pack()
c.create_rectangle(100/2,100/2,250/2,150/2, #1
                   fill='red')

c.create_rectangle(300/2,300/2,250/2,150/2, #2
                   fill='red')

c.create_rectangle(50/2,150/2,100/2,300/2, #3
                   fill='red')

c.create_rectangle(100/2,300/2,250/2,350/2, #4
                   fill='red')

c.create_rectangle(300/2,500/2,250/2,350/2, #5
                   fill='red')

c.create_rectangle(50/2,350/2,100/2,500/2, #6
                   fill='red')

c.create_rectangle(100/2,500/2,250/2,550/2, #7
                   fill='red')

c.create_text(350//22,250/2/2,text = '1')
c.create_text(550/2/2,450/2/2,text = '2')
c.create_text(150/2/2,450/2/2,text = '3')
c.create_text(350/2/2,650/2/2,text = '4')
c.create_text(550/2/2,850/2/2,text = '5')
c.create_text(150/2/2,850/2/2,text = '6')
c.create_text(350/2/2,1050/2/2,text = '7')

c.create_rectangle(100/2+150,100/2,250/2+150,150/2, #1
                   fill='red')

c.create_rectangle(300/2+150,300/2,250/2+150,150/2, #2
                   fill='red')

c.create_rectangle(50/2+150,150/2,100/2+150,300/2, #3
                   fill='red')

c.create_rectangle(100/2+150,300/2,250/2+150,350/2, #4
                   fill='red')

c.create_rectangle(300/2+150,500/2,250/2+150,350/2, #5
                   fill='red')

c.create_rectangle(50/2+150,350/2,100/2+150,500/2, #6
                   fill='red')

c.create_rectangle(100/2+150,500/2,250/2+150,550/2, #7
                   fill='red')

c.create_text(350/2/2+150,250/2/2,text = '1')
c.create_text(550/2/2+150,450/2/2,text = '2')
c.create_text(150/2/2+150,450/2/2,text = '3')
c.create_text(350/2/2+150,650/2/2,text = '4')
c.create_text(550/2/2+150,850/2/2,text = '5')
c.create_text(150/2/2+150,850/2/2,text = '6')
c.create_text(350/2/2+150,1050/2/2,text = '7')


c.create_rectangle(100/2+350,100/2,250/2+350,150/2, #1
                   fill='red')

c.create_rectangle(300/2+350,300/2,250/2+350,150/2, #2
                   fill='red')

c.create_rectangle(50/2+350,150/2,100/2+350,300/2, #3
                   fill='red')

c.create_rectangle(100/2+350,300/2,250/2+350,350/2, #4
                   fill='red')

c.create_rectangle(300/2+350,500/2,250/2+350,350/2, #5
                   fill='red')

c.create_rectangle(50/2+350,350/2,100/2+350,500/2, #6
                   fill='red')

c.create_rectangle(100/2+350,500/2,250/2+350,550/2, #7
                   fill='red')

c.create_text(350/2/2+350,250/2/2,text = '1')
c.create_text(550/2/2+350,450/2/2,text = '2')
c.create_text(150/2/2+350,450/2/2,text = '3')
c.create_text(350/2/2+350,650/2/2,text = '4')
c.create_text(550/2/2+350,850/2/2,text = '5')
c.create_text(150/2/2+350,850/2/2,text = '6')
c.create_text(350/2/2+350,1050/2/2,text = '7')



c.create_rectangle(100/2+500,100/2,250/2+500,150/2, #1
                   fill='red')

c.create_rectangle(300/2+500,300/2,250/2+500,150/2, #2
                   fill='red')

c.create_rectangle(50/2+500,150/2,100/2+500,300/2, #3
                   fill='red')

c.create_rectangle(100/2+500,300/2,250/2+500,350/2, #4
                   fill='red')

c.create_rectangle(300/2+500,500/2,250/2+500,350/2, #5
                   fill='red')

c.create_rectangle(50/2+500,350/2,100/2+500,500/2, #6
                   fill='red')

c.create_rectangle(100/2+500,500/2,250/2+500,550/2, #7
                   fill='red')

c.create_text(350/2/2+500,250/2/2,text = '1')
c.create_text(550/2/2+500,450/2/2,text = '2')
c.create_text(150/2/2+500,450/2/2,text = '3')
c.create_text(350/2/2+500,650/2/2,text = '4')
c.create_text(550/2/2+500,850/2/2,text = '5')
c.create_text(150/2/2+500,850/2/2,text = '6')
c.create_text(350/2/2+500,1050/2/2,text = '7')
print(datetime.datetime.now().time())

c.create_rectangle(300/2+200,300/4+75,250/2+200,150/4+75,fill = 'red')#57
c.create_rectangle(300/2+200,500/4+75,250/2+200,350/4+75,fill = 'red')#57

while True:
    t=[0,0,0,0]
    t[0]= int( str(datetime.datetime.now().time())[3])
    t[1]= int( str(datetime.datetime.now().time())[4])
    t[2]= int( str(datetime.datetime.now().time())[6])
    t[3]= int( str(datetime.datetime.now().time())[7])
    print (t)
    for target in range(4):
        if t[3]%2==0:
            c.itemconfig(57,fill='red')
            c.itemconfig(58,fill='red')
        else:
            c.itemconfig(57,fill='white')
            c.itemconfig(58,fill='white')
            
        number=t[target]
        for i in [i+(target*14) for i in range(1,8)]:
            c.itemconfig(i,fill='red')
        if number == 0:
            c.itemconfig(4+(target*14),fill='white')
        if number == 1:
            for i in (1+(target*14),3+(target*14),4+(target*14),6+(target*14),7+(target*14),8+(target*14)):
                c.itemconfig(i,fill='white')
        if number == 2:
            for i in (3+(target*14),5+(target*14),8+(target*14)):
                c.itemconfig(i,fill='white')
        if number == 3:
            for i in (3+(target*14),6+(target*14)):
                c.itemconfig(i,fill='white')
        if number == 4:
            for i in (1+(target*14),6+(target*14),7+(target*14)):
                c.itemconfig(i,fill='white')
        if number == 5:
            for i in (2+(target*14),6+(target*14)):
                c.itemconfig(i,fill='white')
        if number == 6:
            for i in (2+(target*14),):
                c.itemconfig(i,fill='white')
        if number == 7:
            for i in (3+(target*14),4+(target*14),6+(target*14),7+(target*14)):
                c.itemconfig(i,fill='white')
        if number == 8:
            pass
        if number == 9:
            for i in (6+(target*14),):
                c.itemconfig(i,fill='white')
        root.update()
    time.sleep(1)
root.mainloop()
