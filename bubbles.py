#sets the background to recolor remaining parts
app.background = 'lightSalmon'

def drawLeaf(x,y): #function that draws a leaf and starfish parts from a center point
    
    #draws a dark leafy area that represents the source of the leafy bubbles
    Polygon(x+29,y+59,x+57,y,x+85,y+59,x+57,y+64,x+85,y+69,x+57,y+128,x+29,y+69,x+57,y+64,fill='darkOliveGreen')
    
    #creates a new color for a different set of "starfish"
    Polygon(x-50,y+8,x+50,y+8,x+50,y-8,x,y,x-50,y,fill='burlyWood')
    Polygon(x+50,y-8,x+64,y-8,x+64,y+8,x+50,y+8,fill='burlyWood')
    
    #variables to create each part of the leaf
    angleBetweenLeaves = 360/4
    leafX = -1
    leafY = 1
    
    #for loop function to make 4 leafs that stem from a single point; also creates shape for the starfish
    for i in range(4):
        if i != 2:
            leafX *= -1
        if i == 2:
            leafY *= -1

        if i == 0 or i == 2:
            Arc(x-(8*leafX),y,16,102,angleBetweenLeaves*-i,90, fill=gradient('mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen', start='top')),
            Arc(x-(50*leafX),y-29.5*leafY,16,43,180+90*i,180, fill=gradient('mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen', start='top')),
            Arc(x-(29*leafX),y-51*leafY,42,16,270+90*i,180, fill=gradient('mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen', start='top')),
            Polygon(x-50*leafX,y-8*leafY,x-8*leafX,y,x,y,x-8*leafX,y-51*leafY,x-29*leafX,y-59*leafY,x-50*leafX,y-51*leafY,x-58*leafX,y-29.5*leafY, fill=gradient('mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen', start='top')),
            Arc(x-(50*leafX),y,100,16,angleBetweenLeaves*-i,90, fill='burlyWood')
        if i == 1 or i == 3:
            Arc(x-(50*leafX),y-29.5*leafY,16,43,90*i-90,180, fill=gradient('mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen', start='top')),
            Arc(x-(29*leafX),y-51*leafY,42,16,270+90*(i-1),180, fill=gradient('mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen', start='top')),
            Arc(x,y-8*leafY,100,16,90*i,90, fill=gradient('mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen', start='top')),
            Polygon(x-50*leafX,y-8*leafY,x-8*leafX,y,x,y,x-8*leafX,y-51*leafY,x-29*leafX,y-59*leafY,x-50*leafX,y-51*leafY,x-58*leafX,y-29.5*leafY, fill=gradient('mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen','mediumSeaGreen','limeGreen', start='top')),
            Arc(x,y-51*leafY,16,102,90*i,90, fill='lightSalmon')
    
    #creates extra parts for other starfish; also creates shape for the leaves
    Arc(x-50,y-8,28,88,270,90,rotateAngle=-5,fill='burlyWood')
    Arc(x-64,y+7,28,88,90,90, fill='burlyWood', rotateAngle=-5)
    
    #creates a tiny starfish at the center of the leaf
    Star(x,y,5,4, fill='brown')
    
    #suctions on each of the starfish
    Circle(x-58,y-16,4, fill=None,border='sienna')
    Circle(x-58,y-30,3.5, fill=None,border='sienna')
    Circle(x-57.5,y-43,3, fill=None,border='sienna')
    Circle(x-57,y+11,4, fill=None,border='sienna')
    Circle(x-57,y+23,3.5, fill=None,border='sienna')
    Circle(x-57,y+37,3, fill=None,border='sienna')
    
    Circle(x-1,y+50,4, fill=None,border='sienna')
    Circle(x-2.5,y+36,3.5, fill=None,border='sienna')
    Circle(x-3,y+23,3, fill=None,border='sienna')
    Circle(x+10,y+62.5,4, fill=None,border='sienna')
    Circle(x+20,y+63,3.5, fill=None,border='sienna')
    Circle(x+31,y+63.5,3, fill=None,border='sienna')
    Circle(x-12,y+63,4, fill=None,border='sienna')
    Circle(x-24,y+63.5,3.5, fill=None,border='sienna')
    Circle(x-36,y+64,3, fill=None,border='sienna')
    
    Circle(x+18,y+2.5,3, fill=None,border='sienna')
    Circle(x+27,y+2,3.5, fill=None,border='sienna')
    Circle(x+38,y+2,4, fill=None,border='sienna')
    
    Circle(x-16,y-3,3, fill=None,border='sienna')
    Circle(x-29,y-3,3.5, fill=None,border='sienna')
    Circle(x-44,y-2,4, fill=None,border='sienna')
    Circle(x+2,y-12,3, fill=None,border='sienna')
    Circle(x+2,y-25,3.5, fill=None,border='sienna')
    Circle(x+2,y-39,4, fill=None,border='sienna')
    Circle(x,y-52,4.5, fill=None,border='sienna')

#calls the drawLeaf function to draw multiple leaves and starfish from certain points on the canvas
drawLeaf(-14,2)
drawLeaf(100,2)
drawLeaf(214,2)
drawLeaf(328,2)
drawLeaf(442,2)

drawLeaf(-14,130)
drawLeaf(100,130)
drawLeaf(214,130)
drawLeaf(328,130)
drawLeaf(442,130)

drawLeaf(-14,258)
drawLeaf(100,258)
drawLeaf(214,258)
drawLeaf(328,258)
drawLeaf(442,258)

drawLeaf(-14,386)
drawLeaf(100,386)
drawLeaf(214,386)
drawLeaf(328,386)
drawLeaf(442,386)

leafBubbles = Group() #represents all the leaf bubbles

def onMouseMove(mouseX,mouseY): #automatic function that lights up the leaf bubbles when your moving mouse is close to a leaf bubble
    for leafBubble in leafBubbles:
        if distance(mouseX,mouseY,leafBubble.centerX,leafBubble.centerY) <= 50:
            leafBubble.fill = 'lightGreen'
        else:
            leafBubble.fill = 'green'
    
def onStep(): #automatic function moves the leaf bubbles every onStep

    #makes the leaf bubbles "evaporate" from their origin
    for leafBubble in leafBubbles:
        leafBubble.centerX += randrange(-10,11)
        leafBubble.centerY -= 5
        leafBubble.opacity -= 5
        if leafBubble.opacity <= 1:
            leafBubbles.remove(leafBubble)

    #creates an array of leaf bubbles that represent their origin
    for x in range(4):
        for y in range(4):
            leafBubbles.add(
                Circle(43+114*x,66+128*y,5,fill='green')
                )