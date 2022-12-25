x = 500
v = 430
c = 360
b = 290
def setup():
    size(400,600)
def draw():
    background(0,random(0,255),random(0,255))
    global x,c,v,b
    push()
    fill(0, 128, 0)
    triangle(50,500,150,500,100,c)
    triangle(50,430,150,430,100,c)
    triangle(50,360,150,360,100,b)
    pop()
    push()
    fill(139, 69, 19)
    rect(85,500,30,10000)
    pop()
    ellipse(240,550,100,100)
    ellipse(240,480,75,75)
    ellipse(240,430,50,50)
    push()
    strokeWeight(3)
    point(225,430)
    point(240,430)
    pop()
    push()
    strokeWeight(10)
    point(random(0,600),random(0,600))
    frameRate(10)
    pop()
    x -= 5
    v -= 5
    c -= 5
    b -= 5
