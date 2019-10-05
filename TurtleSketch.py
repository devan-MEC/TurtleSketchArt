import turtle



f=open("turtlemovements.txt","w+")
f.write('''import turtle
wn=turtle.Screen()
wn.title("DrawingApp @forFOSS")
wn.bgcolor("black")
wn.setup(width=800,height=800)
wn.tracer(0)


#brushtool
brush=turtle.Turtle()
brush.speed(0)
brush.shape("circle")
brush.color("white")
brush.goto(0,0)
#end of inits\n''')
wn=turtle.Screen()
wn.title("DrawingApp @forFOSS")
wn.bgcolor("black")
wn.setup(width=800,height=800)
wn.tracer(0)


#brushtool
brush=turtle.Turtle()
brush.speed(0)
brush.shape("circle")
brush.color("white")
brush.goto(0,0)

#brushfunctions
def brush_right():
    x=brush.xcor()
    x+=10
    brush.setx(x)
    f.write('''x=brush.xcor()
x+=10
brush.setx(x)\n''')
def brush_left():
    x=brush.xcor()
    x-=10
    brush.setx(x)
    f.write('''x=brush.xcor()
x-=10
brush.setx(x)\n''')
def brush_up():
    y=brush.ycor()
    y+=10
    brush.sety(y)
    f.write('''y=brush.ycor()
y+=10
brush.sety(y)\n''')
def brush_down():
    y=brush.ycor()
    y-=10
    brush.sety(y)
    f.write('''y=brush.ycor()
y-=10
brush.sety(y)\n''')
def brush_rightup():
    brush.left(45)
    brush.forward(10)
    brush.right(45)
    f.write('''brush.left(45)
brush.forward(10)
brush.right(45)\n''')
def brush_leftup():
    brush.left(135)
    brush.forward(10)
    brush.right(135)
    f.write('''brush.left(135)
brush.forward(10)
brush.right(135)\n''')
def brush_rightdown():
    brush.right(45)
    brush.forward(10)
    brush.left(45)
    f.write('''brush.right(45)
brush.forward(10)
brush.left(45)\n''')
def brush_leftdown():
    brush.left(225)
    brush.forward(10)
    brush.right(225)
    f.write('''brush.left(225)
brush.forward(10)
brush.right(225)\n''')

def brushoff():
    brush.penup()
    f.write('''brush.penup()\n''')

def brushon():
    brush.pendown()
    f.write('''brush.pendown()\n''')
def closeapp():
    f.write('''while True:
    wn.update()''')
    f.close()
    exit() #does this function work okay? seems glitchy to me




#keybindings
wn.listen()
wn.onkeypress(brush_right,"d")
wn.onkeypress(brush_left,"a")
wn.onkeypress(brush_up,"w")
wn.onkeypress(brush_down,"s")
wn.onkeypress(brush_rightup,"e")
wn.onkeypress(brush_leftup,"q")
wn.onkeypress(brush_rightdown,"c")
wn.onkeypress(brush_leftdown,"z")
wn.onkeypress(brushoff,"o")
wn.onkeypress(brushon,"i")
wn.onkeypress(closeapp,"p")
#game loop
while True:
    wn.update()
