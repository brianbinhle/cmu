app.background = 'lightBlue' #skybox background
grass = Rect(0,215,400,185, fill=rgb(52,140,49)) #grass

#Lightbulb

###   glass bulb

#top circle of glass bulb
top1 = Circle(200,100,70, fill='gray', opacity=10) #the top of the top circle of the lightbulb that will change color and opacity
Circle(200,100,70, fill=None, border='black') #the outline of the top of the top circle of the lightbulb
Polygon(141,138,150,145,159,153,164,160,149,155, fill=app.background) #hides the left portion of the circle that represents the top of the top circle of the lightbulb
Polygon(259,138,250,145,241,153,236,160,251,155, fill=app.background) #hides the right portion of the circle the represents the top of the top circle of the lightbulb
top2 = Oval(200,110,139,100, fill=None) #the bottom half of the top circle of the lightbulb that will change color and opacity
Oval(200,110,139,100, fill=None, border='black') #the outline of the bottom half of the top circle of the lightbulb
Polygon(133,94,132,104,268,104,267,94,255,62,199,32,147,62, fill=app.background) #hides the top portion of the oval that represents the bottom of the top circle of the lightbulb 
top3 = Polygon(133,94,132,104,268,104,267,94,255,62,199,32,147,62, fill='gray', opacity=10) #covers over the empty space of the lightbulb that will change color and opacity

#bottom of glass bulb
bottom = Oval(200,200,64,35, fill='gray', opacity=10) #the bottom oval of the lightbulb that will change color and opacity
Oval(200,200,64,35, fill=None, border='black') #the outline of the oval of the lightbulb
Polygon(172,183,228,183,232,198,168,198, fill=None, border='black') #the non-round part of the bottom of the glass bulb before it makes a bend

#middle of glass bulb
Line(160,150,173,183) #outline of the lightbulb on the middle left
Line(240,150,227,183) #outline of the lightbulb on the middle right

Polygon(174,183,161,150,239,150,226,183,230,198,170,198, fill=app.background) #hides the extra outlines from previous shapes
middle = Polygon(174,183,161,150,239,150,226,183,230,198,170,198, fill='gray', opacity=10) #covers over the empty space of the lightbulb that will change color and opacity

#### light source

light = Polygon(190,180,210,180,215,185,215,211,185,211,185,185, fill=app.background, border='black') #glass mount that supports any wires in the lightbulb
branch1 = Line(190,180,175,135) #left wire that will turn into branch
branch2 = Line(210,180,225,135) #right wire that will turn into branch
branch3 = Line(200,180,200,150) #middle wire that will turn into branch
branch4 = Line(200,150,190,130, fill=rgb(92,64,51), visible=False) #extra long branch that will be hidden until onMousePress
branch5 = Line(200,150,210,130, fill=rgb(92,64,51), visible=False) #extra long branch that will be hidden until onMousePress

tinyBranches = Group( #the tiny branches that stem from the main branches
Line(186,169,179,168),
Line(182,157,187,153),
Line(177,143,165,139),
Line(200,170,194,168),
Line(200,160,204,156),
Line(194,137,186,136),
Line(205,139,209,137),
Line(220,149,225,147),
Line(215,165,211,157)
)
tinyBranches.fill = rgb(92,64,51) #enables the color of all the tiny branches made
tinyBranches.visible = False #enables the initial visibility of the tiny branches until onMousePress

Line(195,190,205,190) #extra wire inside the glass mount of the lightbulb 
Line(198,190,195,211) #extra wire inside the glass mount of the lightbulb
Line(202,190,205,211) #extra wire inside the glass mount of the lightbulb

###   Spring
Oval(200,215,50,10, fill=gradient('silver','gray','silver', start='left'), border=gradient('black',app.background,'black')) #coil
Oval(200,220,50,10, fill=gradient('silver','gray','silver', start='left'), border=gradient('black',app.background,'black')) #coil
Oval(200,225,50,10, fill=gradient('silver','gray','silver', start='left'), border=gradient('black',app.background,'black')) #coil
Oval(200,230,50,10, fill=gradient('silver','gray','silver', start='left'), border=gradient('black',app.background,'black')) #coil
Oval(200,235,50,10, fill=gradient('silver','gray','silver', start='left'), border=gradient('black',app.background,'black')) #coil
Rect(188,240,24,9, fill=gradient('silver','gray','silver', start='left')) #bottom of spring
Oval(200,240,50,10, fill=gradient('silver','gray','silver', start='left'), border=gradient('black',app.background,'black')) #coil

#Roots
Roots = Group( #tree roots that will be part of the lightbulb when onMousePress
Polygon(190,249,178,272,190,260,195,268,198,263,204,270,202,258,223,274,210,249),
Line(190,249,178,272),
Line(190,249,195,268),
Line(202,258,204,270),
Line(210,249,223,274),

Line(178,272,147,278),
Line(147,278,121,275),
Line(121,275,73,284),
Line(73,284,51,291),
Line(51,291,34,306),
Line(34,306,10,319),

Line(147,278,133,298),
Line(133,298,136,309),
Line(136,309,127,328),

Line(73,284,75,303),
Line(75,303,67,316),

Line(195,268,190,285),
Line(190,285,175,300),
Line(175,300,163,321),
Line(163,321,159,351),

Line(195,268,200,285),
Line(200,285,215,300),
Line(215,300,221,315),
Line(221,315,214,337),
Line(214,337,215,349),

Line(204,270,207,283),
Line(207,283,226,291),
Line(226,291,233,297),

Line(233,297,243,316),
Line(243,316,259,332),
Line(259,332,264,347),

Line(233,297,253,296),
Line(253,296,272,302),
Line(272,302,295,322),
Line(295,322,315,330),

Line(223,274,252,271),
Line(252,271,307,269),
Line(307,269,335,280),
Line(335,280,347,294),
Line(347,294,365,302),

Line(223,274,234,280),
Line(234,280,294,284),
Line(294,284,302,300),
Line(302,300,310,305)
)

Roots.fill = rgb(92,64,51) #enables the color of the roots
Roots.visible = False #enables the visibility of the roots until onMousePress

#Birds
def drawBird(centerX,centerY): #sets up a function to draw birds at a certain point
    Line(centerX,centerY,centerX-10,centerY-5) #left wing of the bird
    Line(centerX,centerY,centerX+10,centerY-5) #right wing of the bird
    
drawBird(225,85) #draws birds at certain points
drawBird(245,120)
drawBird(160,90)
drawBird(155,130)

#onMousePress
def onMousePress(centerX,centerY):
    #adjusts the inside of the lightbulb
    light.fill = 'yellow' #turns the light on, fills the main light source
    top1.fill = 'yellow' #fills the top of the top circle
    top1.opacity = 20 #changes the opacity of the top of the top circle
    top2.fill = 'yellow' #fills the bottom of the top circle
    top2.opacity = 5 #changes the opacity of the bottom of the top circle
    top3.fill = 'yellow' #fills the empty area of the top circle
    top3.opacity = 20 #changes the opacity of the empty area of the top circle
    middle.fill = 'yellow' #fills the middle part of the lightbulb
    middle.opacity = 30 #changes the opacity of the middle part of the lightbulb
    bottom.fill = 'yellow' #fills the bottom part of the lightbulb
    bottom.opacity = 40 #changes the opacity of the bottom part of the lightbulb
    
    branch1.fill = rgb(92,64,51) #turns the left wire into a branch
    branch2.fill = rgb(92,64,51) #turns the right wire into a branch
    branch3.fill = rgb(92,64,51) #turns the middle wire into a branch
    tinyBranches.visible = True #makes the tinyBranches that stem from the main branches inside of the lightbulb visible
    branch4.visible = True #makes an extra branch inside the lightbulb visible
    branch5.visible = True #makes an extra branch inside the lightbulb visible
    
    #adjusts the outside of the lightbulb
    Roots.visible = True #makes the tree roots visible
    grass.fill = gradient(rgb(124,252,0),rgb(52,140,49)) #changes the grass to be affected by the light

#onMouseRelease
def onMouseRelease(centerX,centerY):
    #resets the inside of the lightbulb
    light.fill = app.background #turns the light off, resets the color of the main light source
    top1.fill = 'gray' #resets the color of the top of the top circle
    top1.opacity = 10 #resets the opacity of the top of the top circle
    top2.fill=None #resets the color of the bottom of the top circle
    top3.fill = 'gray' #resets the color of the empty space of the top circle of the lightbulb
    top3.opacity = 10 #resets the opacity of the empty space of the top circle of the lightbulb
    middle.fill = 'gray' #resets the color of the middle part of the lightbulb
    middle.opacity = 10 #resets the opacity of the middle part of the lightbulb
    bottom.fill = 'gray' #resets the color of the bottom of the lightbulb
    bottom.opacity = 10 #resets the opacity of the bottom of the lightbulb
    
    tinyBranches.visible = False #hides the tinyBranches that stem from the main branches
    branch1.fill = 'black' #resets the left branch into wire
    branch2.fill = 'black' #resets the right branch into wire
    branch3.fill = 'black' #resets the middle branch into wire
    branch4.visible = False #hides an extra branch inside the lightbulb
    branch5.visible = False #hides an extra branch inside the lightbulb
    
    #resets the outside of the lightbulb
    Roots.visible = False #hides the tree roots
    
    grass.fill = rgb(52,140,49) #resets the lighting that appears on the grass