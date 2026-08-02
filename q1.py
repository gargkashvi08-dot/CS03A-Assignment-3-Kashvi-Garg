# /*****************************************************/
# /* CS03A - Summer 2026
# /* Assignment 3 - Question 1
# /* Student Name: Kashvi Garg
# /* SID: 20744788
# /*****************************************************/

import math

class Circle:
    def __init__(self, x=0,y=0,radius=1):
        self.x= x
        self.y =y
        self.radius=radius

    def getX(self):
        return self.x

    def setX(self,x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y=y

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius=radius

    def getArea(self):
        return math.pi*self.radius**2

    def getPerimeter(self):
        return 2*math.pi*self.radius

    def containPoint(self,x,y):
        dist=((x -self.x)**2+(y- self.y)**2)**0.5
        return dist<=self.radius

    def containCircle(self,circle):
        dist=((circle.x- self.x)**2+(circle.y-self.y)**2)**0.5
        return dist<=self.radius - circle.radius

    def overlaps(self,circle):
        dist=((circle.x- self.x)**2+(circle.y -self.y)**2)**0.5
        return dist<=self.radius+ circle.radius

def run():
    circles= [Circle(0,0,5), Circle(1,1,2), Circle(10,10,3),Circle(0,0,1)]

    for c in circles:
        print('Area: '+ str(c.getArea())+' Peremeter: '+ str(c.getPerimeter()))

    for c in circles:
        print('Contains (5,5): '+   str(c.containPoint(5,5)))

    for a in circles:
        for b in circles:
            if a is not b:
                print('Contains other circle: '+str(a.containCircle(b)))

    for a in circles:
        for b in circles:
            if a is not b:
                print('Overlap other circle: '+ str(a.overlaps(b)))

if __name__=='__main__':
    run()
