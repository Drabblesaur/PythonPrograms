#CIS_40 Johnny To
from ezgraphics import GraphicsWindow
win = GraphicsWindow (800,500)
canvas = win.canvas()
canvas.setOutline("blue")
canvas.setFill()
canvas.setLineWidth(10)
canvas.drawOval(100,100,200,200)

canvas.setOutline("black")
canvas.drawOval(310,100,200,200)

canvas.setOutline("red")
canvas.drawOval(520,100,200,200)

canvas.setOutline("yellow")
canvas.drawOval(200,200,200,200)

canvas.setOutline("green")
canvas.drawOval(410,200,200,200)