#CIS_40 Johnny To
#Creates a graphic circle in the middle
from ezgraphics import GraphicsWindow
import math
print("Hello!")
#Constant & variable define
name = input("Name?:")
width = int(input("Width of the Window:"))
height = int(input("height of the Window:"))
radius = int(input("Radius of the Circle:"))
borderColor = input("Border Color? :")
borderThickness = int(input("Border Thickness? (by pixel):"))
textX = round(0.01*width)
textY = round(0.01*height)
Circ = "Circumference:"+str((2*math.pi*radius))
Area = "Area:"+str((math.pi*(radius**2)))
#print info
print ("TEXTX:",textX)
print ("TEXTY:",textY)
print("Circumference:",(2*math.pi*radius))
print("Area:",(math.pi*(radius**2)))
#Construct Graphic
win = GraphicsWindow (width,height)
canvas = win.canvas()
canvas.drawText(textX,textY,name+"\n"+Circ+"\n"+Area)
canvas.setOutline(borderColor)
canvas.setFill()
canvas.setLineWidth(borderThickness)
startx = (width/2)-radius
starty = (height/2)-radius
canvas.drawOval(startx,starty,2*radius,2*radius)
print("Graphic Completed")
win.wait()
