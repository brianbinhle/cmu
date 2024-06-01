#Background
Rect(0,0,400,400, fill=gradient('lightBlue',rgb(35,96,157),'midnightBlue')) #gradient background

#Body and Clothes
Polygon(142,269,142,281,110,302,105,310,105,349,123,400,132,400,225,400,250,369,250,369,245,336,235,310,230,302,215,280, fill=rgb(252,190,107)) #torso and arm skin
Polygon(130,289,110,302,105,310,125,315,127,349,150,400,225,400,225,315,235,310,215,280,173,296, fill='yellowGreen') #shirt
Star(190,319,20,5, fill=None, border='aqua', borderWidth=2, roundness=30) #shirt design
Star(200,375,20,5, fill=None, border='white', borderWidth=1, roundness=30) #shirt design
Star(155,350,20,5, fill=None, border='white', borderWidth=1, roundness=30) #shirt design
RegularPolygon(154,312,4,4, fill=None, border='white') #shirt design
RegularPolygon(207,345,4,4, fill=None, border='white') #shirt design
RegularPolygon(166,385,4,4, fill=None, border='white') #shirt design

#Hair, Skin, Nose
Oval(191,180,182,215, fill=rgb(252,190,107)) #face
Oval(192,230,22,10, fill=gradient(rgb(252,190,107),rgb(225,180,113), start='left-top')) #lower nose
Polygon(181,230,203,230,199,216,194,207,192,195,190,207,185,216, fill=gradient(rgb(252,190,107),rgb(225,180,113),rgb(225,225,180), start='left'), opacity=75) #upper nose
Oval(191,180,182,215, fill=gradient('black',rgb(252,190,107),rgb(252,190,107), start='left'), opacity=20) #lighting of face

Polygon(90,70,155,75,125,115,87,121,87,110, fill=gradient(rgb(13,60,138),rgb(13,60,138),rgb(13,60,138),rgb(13,60,138),rgb(36,100,200), start='top-right')) #hair
Oval(155,75,106,50, fill=gradient(rgb(13,60,138),rgb(13,60,138),rgb(42,118,205),rgb(42,118,205),rgb(89,155,231), start='left')) #hair
Polygon(189,56,226,74,206,71, fill=gradient(rgb(42,118,205),rgb(164,234,246), start='left')) #hair
Oval(266,129,24,60, fill=rgb(164,234,246)) #hair
Polygon(175,134,188,142,202,170,220,135, fill=gradient(rgb(164,234,246),rgb(42,118,205), start='bottom')) #hair
Polygon(214,71,266,99,278,134,272,151,211,150,175,134,149,125,125,115,125,95,206,71, fill=gradient(rgb(164,234,246),rgb(164,234,246),rgb(89,155,231),rgb(42,118,205),rgb(42,118,205),rgb(13,60,138), start='right')) #hair
Polygon(102,70,96,50,114,59, fill=rgb(13,60,138)) #hair
Polygon(100,153,110,173,125,115, fill=gradient(rgb(36,100,200),rgb(36,100,200),rgb(13,60,138), start='bottom')) #hair
Polygon(121,125,142,133,168,153,181,164,190,158,202,170,188,142,175,134,125,115, fill=gradient('white','black','black', start='bottom'), opacity=20) #shadow of hair
Polygon(100,156,100,180,80,159,81,136,87,121,105,95, fill=gradient(rgb(164,234,246),rgb(36,100,200),rgb(36,100,200), start='bottom-left')) #hair
Polygon(105,95,87,121,100,156,125,115, fill=gradient(rgb(13,60,138),rgb(13,60,138),rgb(36,100,200),rgb(36,100,200), start='right-top')) #hair
Polygon(125,115,147,125,162,136,181,156,175,134, fill=gradient(rgb(164,234,246),rgb(36,100,200),rgb(36,100,200), start='bottom')) #hair
Polygon(207,157,222,164,220,153,211,150, opacity=20) #shadow of hair
Polygon(272,149,282,174,282,200,290,174,278,129, fill=rgb(164,234,246)) #hair
Polygon(211,150,231,160,229,149,236,151,262,174,272,149, fill=gradient(rgb(164,234,246),rgb(164,234,246),rgb(164,234,246),rgb(133,213,225),rgb(133,213,225),rgb(89,155,231),rgb(89,155,231), start='right')) #hair
Polygon(273,152,282,174,276,168, opacity=50) #shadow of hair

#Eyes
Polygon(180,176,180.5,164,138,169,139,188,144,203,158,209,180,212, fill='white') #white part of eye
Polygon(210,218,210,180,250,174,250,192,243,205,237,212,222,216, fill='white') #white part of eye
Oval(160.5,169,43,25, fill='white') #white part of eye
Oval(180,188,10,48, fill='white') #white part of eye
Oval(211.5,193,10,48, fill='white') #white part of eye
Oval(229,174,40,24, fill='white') #white part of eye

Oval(171,195,25,28, fill=gradient(rgb(28,37,96),rgb(85,181,255), start='right'), border='black', borderWidth=1) #iris
Circle(173,200,7) #pupil
Circle(176,189,1, fill='white') #extra white dot

Oval(223,200,25,28, fill=gradient(rgb(28,37,96),rgb(85,181,255), start='right'), border='black', borderWidth=1) #iris
Circle(223,204.5,7) #pupil
Circle(229,195,1, fill='white') #extra white dot

#Eyebrow
Polygon(162,136,138,139,129,148,147,142,170,143, fill=rgb(28,37,96))

#Mouth
Polygon(170,250,180,253,190,254,206,256,206,259,190,261,175,256) #open mouth
Polygon(165,247,164,244,190,252,198,253,212,254,200,256,190,255,170,250, fill='lightSalmon') #upper lip
Polygon(165,247,170,256,183,264,196,264,208,260,212,254,206,256,202,259,190,261,175,256,170,250, fill='salmon') #bottom lip

#Lighting
Rect(0,0,400,400, fill=gradient('white','black', start='bottom-right'), opacity=20) #background lighting
Polygon(142,269,167,285,220,282,190,300,125,315,105,310,110,302,130,289,142,281, fill=gradient('black','yellowGreen', start='top'),  opacity=20) #shadow of neck

Line(125,315,127,349, opacity=50, lineWidth=1) #shadow of arm
Line(127,349,150,400, opacity=50, lineWidth=1) #shadow of arm
Line(225,315,225,400, opacity=50, lineWidth=1) #shadow of arm
Line(105,310,125,315, opacity=25, lineWidth=1) #shadow of shirt sleeve
Line(225,315,235,310, opacity=25, lineWidth=1) #shadow of  shirt sleeve
Line(130,289,173,296, opacity=25, lineWidth=1) #shadow of shirt v-neck
Line(173,296,220,282, opacity=25, lineWidth=1) #shadow of shirt v-neck

#Orb
Circle(250,410,58, fill='gold') #main middle part of orb
Circle(250,410,65, fill=None, border='yellow', borderWidth=10, opacity=20) #extra lighting shining out of orb

#Text
Label('JOY',350,25, font='monospace', fill='white', size=50)