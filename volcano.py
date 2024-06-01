#Background
Rect(0,250,400,150, fill=rgb(53,44,27)) #the table
Rect(0,0,400,250, fill='midnightBlue') #sky layer 1
Rect(0,0,400,250, fill=gradient('midnightBlue','steelBlue', start='top'), opacity=50) #sky layer 2
Rect(0,250,400,50, fill=gradient(rgb(53,44,27),'midnightBlue','steelBlue', start='bottom'), opacity=25) #reflected surface

#Stars and RegularPolygons in the Sky
RegularPolygon(65,40,6,4, fill='gold') #gold diamond
RegularPolygon(340,55,8,4, fill='white') #white diamond
Star(255,30,10,5, fill='gold', roundness=20) #gold star
Star(155,65,8,5, fill='white', roundness=20) #white star
Star(80,130,5,5, fill='gold') #gold star
Star(365,155,10,5, fill='white') #white star
Star(20,75,5,5, fill='white', roundness=20) #white star
Star(205,105,5,5, fill='white') #white star

#Smoke
Circle(300,100,25, fill=gradient('darkGray','gray', start='top'), opacity=50) #ashcloud 1
Circle(275,90,25, fill=gradient('darkGray','gray', start='top'), opacity=50) #ashcloud 2
Circle(260,110,20, fill=gradient('darkGray','gray', start='top'), opacity=50) #ashcloud 3
Circle(285,125,10, fill=gradient('darkGray','gray', start='top'), opacity=50) #ashcloud 4
Circle(320,105,20, fill=gradient('darkGray','gray', start='top'), opacity=50) #ashcloud 5
Circle(300,110,15, fill=gradient('darkGray','gray', start='top'), opacity=50) #ashcloud 6

#Volcano
Polygon(260,135,325,140,350,275,280,290,240,270, fill=rgb(44,44,44)) #volcano base layer 1
Polygon(260,135,325,140,350,275,280,290,240,270, fill=gradient(rgb(64,64,64),'dimGray', start='bottom'), opacity=50) #volcano base layer 2
Oval(292.5,137.5,65,10, fill='fireBrick') #crater with lava

Line(267.5,140.5,280,290, fill=gradient('chocolate','crimson')) #lava overflow 1
Line(290,142,345,249, fill='chocolate') #lava overflow 2
Polygon(290,142,297.5,142.5,272,215,270,285,255,260,275,160,256,166, fill=gradient('chocolate','fireBrick', start='bottom')) #lava overflow 3
Line(330,171,280,290, fill='chocolate') #lava overflow 4
Polygon(317.5,197.5,350,275,330,265, fill=gradient('chocolate','fireBrick', start='bottom')) #lava overflow 4
Line(246,231,250,275, fill='chocolate') #lava overflow 5
Line(305,143,310,155, fill='chocolate') #lava overflow 6

#Vinegar
Rect(60,320,50,50, fill='powderBlue') #clear glass
Polygon(80,305,90,305,110,320,60,320, fill='powderBlue') #clear glass
Oval(85,305,10,5, fill='white') #cap
Rect(60,335,50,20, fill='white') #Plastic label
Label('Vinegar',85,345, size=10, font='orbitron') #Text
Rect(60,360,50,10, fill='khaki') #Vinegar

#Flask
Line(55,220,55,245, fill='white', lineWidth=5, opacity=50) #outline
Line(55,245,80,275, fill='white', lineWidth=5, opacity=50) #outline
Line(35,220,35,245, fill='white', lineWidth=5, opacity=50) #outline
Line(35,245,10,275, fill='white', lineWidth=5, opacity=50) #outline

Rect(35,220,20,25, fill='powderBlue') #clear glass
Oval(45,220,25,8, fill='powderBlue') #clear glass
Oval(45,220,25,8, fill=None, border='white', opacity=50) #outline
Oval(45,275,75,25, fill=None, border='white', opacity=50) #outline
Polygon(35,245,55,245,80,275,10,275, fill=gradient('powderBlue','lightSteelBlue', start='top')) #clear glass

Polygon(25,257,65,257,80,275,10,275, fill='lawnGreen', opacity=75) #acid
Oval(45,275,70,20, fill='lawnGreen') #acid

Polygon(45,245,30,269,60,269, fill='yellow') #Plastic label
Label('!',45,260, size=15, bold=True) #Text

#Baking Soda
Rect(155,235,45,55, fill='darkOrange') #Cardboard frontSide
Polygon(190,225,200,235,155,235,155,290,145,280,145,225, fill='coral') #Cardboard Lateral Sides

Circle(177.5,262.5,15, fill='darkRed') #Baking Soda Logo, Red Circle
Circle(177.5,262.5,22, fill=None, border='yellow', dashes=True) #Baking Soda Logo, dashed circle outline
Label('Baking',177.5,257, size=10, fill='blue', font='orbitron') #Text "Baking"
Label('Soda',177.5,266, size=10, fill='blue', font='orbitron') #Text "Soda"