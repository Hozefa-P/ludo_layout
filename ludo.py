import turtle
import math

wn=turtle.Screen()

blue=turtle.Turtle()
blue.color("blue")
blue.shape("circle")

red=turtle.Turtle()
red.color("red")
red.shape("circle")

green=turtle.Turtle()
green.color("green")
green.shape("circle")

yellow=turtle.Turtle()
yellow.color("yellow")
yellow.shape("circle")

sk=turtle.Turtle()
sk.speed(0)

#screen: 400*400 - big squares side(a), small squares side (b)
#2a+3b=400 & 6b+6b+3b=400  (using geometry)
#a=160 & b=80/3=26.66667

sk.up()                     #top right (blue)
sk.goto(199,199)
sk.fillcolor("blue")
sk.begin_fill()
sk.down()
for _ in range(4):
    sk.right(90)
    sk.forward(160)
sk.end_fill()

sk.up()                     #top right (white)
sk.goto(174,174)
sk.fillcolor("white")
sk.begin_fill()
sk.down()
for _ in range(4):
    sk.right(90)
    sk.forward(110)
sk.end_fill()

sk.up()                     #bottom left(reD)
sk.goto(-199,-199)
sk.fillcolor("red")
sk.begin_fill()
sk.down()
for _ in range(4):
    sk.right(90)
    sk.backward(160) 
sk.end_fill()

sk.up()                     #bottom left(white)
sk.goto(-174,-174)
sk.fillcolor("white")
sk.begin_fill()
sk.down()
for _ in range(4):
    sk.right(90)
    sk.backward(110) 
sk.end_fill()

sk.up()                    #top left (green)
sk.goto(-199,199)
sk.fillcolor("green")
sk.begin_fill()
sk.down()
for _ in range(4):
    sk.right(270)
    sk.backward(160) 
sk.end_fill()

sk.up()                    #top left (white)
sk.goto(-174,174)
sk.fillcolor("white")
sk.begin_fill()
sk.down()
for _ in range(4):
    sk.right(270)
    sk.backward(110) 
sk.end_fill()

sk.up()                     #bottom right (yellow)
sk.goto(199,-199)
sk.fillcolor("yellow")
sk.begin_fill()
sk.down()
for _ in range(4):
    sk.right(270)
    sk.forward(160)   
sk.end_fill()

sk.up()                     #bottom right (white)
sk.goto(174,-174)
sk.fillcolor("white")
sk.begin_fill()
sk.down()
for _ in range(4):
    sk.right(270)
    sk.forward(110)   
sk.end_fill()

#small blocks
y=199                        #blue left
for _ in range(6):
    sk.up()
    sk.goto(39,y)
    sk.down()
    y-=80/3
    for _ in range(4):
        sk.right(90)
        sk.forward(80/3)
    
x=199                       #blue bottom
for _ in range(6):
    sk.up()
    sk.goto(x,39)
    sk.down()
    x-=80/3
    for _ in range(4):
        sk.right(90)
        sk.forward(80/3)

y=-199                #yellow left
for _ in range(6):
    sk.up()
    sk.goto(39,y)
    sk.down()
    y+=80/3
    for _ in range(4):
        sk.left(90)
        sk.forward(80/3) 
        
x=199                      #yellow top
for _ in range(6):
    sk.up()
    sk.goto(x,-39)
    sk.down()
    x-=80/3
    for _ in range(4):
        sk.left(90)
        sk.forward(80/3)   
        
y=-199                      #red right
for _ in range(6):
    sk.up()
    sk.goto(-39,y)
    sk.down()
    y+=80/3
    for _ in range(4):
        sk.right(90)
        sk.forward(-80/3)                
        
x=-199                      #red top
for _ in range(6):
    sk.up()
    sk.goto(x,-39)
    sk.down()
    x+=80/3
    for _ in range(4):
        sk.right(90)
        sk.forward(-80/3)       
        
y=199                      #green right
for _ in range(6):
    sk.up()
    sk.goto(-39,y)
    sk.down()
    y-=80/3
    for _ in range(4):
        sk.left(90)
        sk.forward(-80/3)  
        
x=-199                      #green bottom
for _ in range(6):
    sk.up()
    sk.goto(x,39)
    sk.down()
    x+=80/3
    for _ in range(4):
        sk.left(90)
        sk.forward(-80/3)     
        
y=199                        #middle of green & blue
for _ in range(6):
    sk.up()
    sk.goto(80/6,y)
    sk.down()
    y-=80/3
    for _ in range(4):
        sk.right(90)
        sk.forward(80/3)  

y=199-80/3                       #middle of green & blue BLUE BLOCKS
sk.fillcolor("blue")
sk.begin_fill()
for _ in range(5):
    sk.up()
    sk.goto(80/6,y)
    sk.down()
    y-=80/3
    for _ in range(4):
        sk.right(90)
        sk.forward(80/3)          
sk.end_fill()        
        
x=199                       #middle of blue & yellow
for _ in range(6):
    sk.up()
    sk.goto(x,80/6)
    sk.down()
    x-=80/3
    for _ in range(4):
        sk.right(90)
        sk.forward(80/3) 
        
x=199-80/3                       #middle of blue & yellow YELLOW BLOCKS
sk.fillcolor("yellow")
sk.begin_fill()
for _ in range(5):
    sk.up()
    sk.goto(x,80/6)
    sk.down()
    x-=80/3
    for _ in range(4):
        sk.right(90)
        sk.forward(80/3)         
sk.end_fill()
        
y=-199                #middle of yellow and red
for _ in range(6):
    sk.up()
    sk.goto(80/6,y)
    sk.down()
    y+=80/3
    for _ in range(4):
        sk.left(90)
        sk.forward(80/3) 
        
y=-199+80/3               #middle of yellow and red RED BLOCKS
sk.fillcolor("red")
sk.begin_fill()
for _ in range(5):
    sk.up()
    sk.goto(80/6,y)
    sk.down()
    y+=80/3
    for _ in range(4):
        sk.left(90)
        sk.forward(80/3) 
sk.end_fill()        
        
x=-199                      #middle of green and red
for _ in range(6):
    sk.up()
    sk.goto(x,80/6)
    sk.down()
    x+=80/3
    for _ in range(4):
        sk.left(90)
        sk.forward(-80/3)   
        
x=-199+80/3                      #middle of green and red GREEN BLOCKS
sk.fillcolor("green")
sk.begin_fill()
for _ in range(5):
    sk.up()
    sk.goto(x,80/6)
    sk.down()
    x+=80/3
    for _ in range(4):
        sk.left(90)
        sk.forward(-80/3)           
sk.end_fill()
        
#blue triangle        
sk.up()
sk.goto(40,40)
sk.fillcolor("blue")
sk.begin_fill()
sk.down()
sk.right(135)
sk.forward(math.sqrt(80*80/2))
sk.right(90)
sk.forward(math.sqrt(80*80/2))
sk.right(135)
sk.forward(80)
sk.end_fill()

#yellow triangle
sk.up()
sk.goto(40,-40)
sk.fillcolor("yellow")
sk.begin_fill()
sk.down()
sk.left(135)
sk.forward(math.sqrt(80*80/2))
sk.right(90)
sk.forward(math.sqrt(80*80/2))
sk.right(135)
sk.forward(80)
sk.end_fill()

#green triangle        
sk.up()
sk.goto(-40,-40)
sk.fillcolor("green")
sk.begin_fill()
sk.down()
sk.left(135)
sk.forward(math.sqrt(80*80/2))
sk.left(90)
sk.forward(math.sqrt(80*80/2))
sk.right(45)
sk.forward(80)
sk.end_fill()

#red triangle        
sk.up()
sk.goto(40,-40)
sk.fillcolor("red")
sk.begin_fill()
sk.down()
sk.left(45)
sk.forward(math.sqrt(80*80/2))
sk.left(90)
sk.forward(math.sqrt(80*80/2))
sk.left(135)
sk.forward(80)
sk.end_fill()

#Marking dots in all the boxes

blue.up()
blue.goto(149,149)
blue.stamp()
blue.goto(89,149)
blue.stamp()
blue.goto(149,89)
blue.stamp()
blue.goto(89,89)
blue.stamp()

green.up()
green.goto(-149,149)
green.stamp()
green.goto(-89,149)
green.stamp()
green.goto(-149,89)
green.stamp()
green.goto(-89,89)
green.stamp()

red.up()
red.goto(-149,-149)
red.stamp()
red.goto(-89,-149)
red.stamp()
red.goto(-149,-89)
red.stamp()
red.goto(-89,-89)
red.stamp()

yellow.up()
yellow.goto(149,-149)
yellow.stamp()
yellow.goto(89,-149)
yellow.stamp()
yellow.goto(149,-89)
yellow.stamp()
yellow.goto(89,-89)
yellow.stamp()