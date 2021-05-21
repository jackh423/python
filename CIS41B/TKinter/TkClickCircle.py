from tkinter import *
import tkinter as tk
from random import randint,uniform
import math

root = tk.Tk()

canvas = tk.Canvas(root, width=500,height=500)

colors = ['red','orange','yellow','green','blue','purple','black','cyan','magenta']
c = len(colors) - 1

lastPoint = [0,0]
noClicks = True

def mouseClick(event):
    global noClicks

    if randint(0,5) == 0:
        canvas.create_circle(event.x, event.y, randint(25,50))
    else:
        DrawPolygon(event.x,event.y,randint(25,50),randint(3,7))
            
    if noClicks :
        noClicks = False
    else :
        drawLine(event)
       
    lastPoint[0] = event.x
    lastPoint[1] = event.y
    

def mouseDragged(event) :
    if randint(0,1) : #only draw a shape 50% of the time to thin it out a little bit
        mouseClick(event)
    
    
def DrawCircle(self, x, y, r) :
    color = colors[randint(0,c)]
    return self.create_oval(x-r, y-r, x+r, y+r,outline=color,fill=color)

def DrawPolygon(x,y,r,n):
    rads = (2*math.pi)/n
    offset= uniform(0,math.pi)

    points = []

    for i in range(n) :
        px = r*math.cos(i*rads + offset) + x
        py = r*math.sin(i*rads + offset) + y
        point = [px,py]
        points.append(point)

    color = colors[randint(0,c)]
    canvas.create_polygon(points,outline=color,fill=color)
    
def drawLine(event):
    canvas.create_line(lastPoint[0],lastPoint[1],event.x,event.y,fill="black")

    
    
canvas.create_text(250,10,text="click to draw a shape, click again for a line")    
    

tk.Canvas.create_circle = DrawCircle
frame = Frame(root, width=500, height=500)
canvas.bind("<Button-1>", mouseClick)
canvas.bind("<B1-Motion>",mouseDragged)
canvas.focus_set()
canvas.pack()
root.wm_title("Draw some shapes")
root.mainloop() 
