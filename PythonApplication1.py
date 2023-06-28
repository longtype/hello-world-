import math  
x = float(input("请输入一个角度值（以度为单位）"))  
sin_x = math.sin(math.radians(x))  
def new_func(sin_x):    
    print("正弦值为：", sin_x)  
new_func(sin_x)
   
import turtle as t
import math as m 
t.screensize(800,800,"white")
t.hideturtle()
t.speed(0)
t.pendown()
t.goto(0,0)
t.forward(800)
t.left(90)
t.goto(0,0)
t.forward(800)
t.left(90)
t.goto(0,0)
t.forward(800)
t.left(90)
t.goto(0,0)
t.forward(800)
t.left(90)
t.penup()
t.goto(-10,-15)
t.write("O")
t.goto(350,-15)
t.write("x")
t.goto(-15,337)
t.write("y")

n = int(input(r"输入需要放大的倍数："))
x = int((-350)/n)
t.pensize(1)
t.speed(1)
while x <= int((350)/n):
    if x!=0:                  #定义域的反域
        y = m.sin(x)        #函数解析式
    if y>=-350 and y<=350:
        t.goto(n*x,y*n)
        t.pendown()
        t.forward(1)
        #t.penup()
    x+=1
t.down()


