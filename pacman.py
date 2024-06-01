#Background Color of Maze
Rectangle = Rect(0,0,400,400, fill='dodgerBlue')

#Maze
horizontalLines = Group(#horizontal lines of the maze
Rect(20,20,160,20),
Rect(220,20,160,20),
Rect(20,60,360,20),
Rect(20,100,80,20),
Rect(120,100,60,20),
Rect(220,100,60,20),
Rect(300,100,80,20),
Rect(20,260,80,20),
Rect(20,300,120,20),
Rect(20,340,160,20),
Rect(300,260,80,20),
Rect(260,300,120,20),
Rect(220,340,160,20),
Rect(120,140,160,20),
Rect(120,220,160,20),
Rect(0,180,140,20),
Rect(260,180,140,20),
Rect(120,260,60,20),
Rect(220,260,60,20),
Rect(160,300,80,20)
)
verticalLines = Group(#vertical lines of the maze
Rect(80,20,20,300),
Rect(300,20,20,300),
Rect(120,60,20,60),
Rect(260,60,20,60),
Rect(160,100,20,60),
Rect(220,100,20,60),
Rect(120,140,20,100),
Rect(160,20,20,60),
Rect(220,20,20,60),
Rect(20,20,20,100),
Rect(360,20,20,100),
Rect(160,220,20,60),
Rect(220,220,20,60),
Rect(120,260,20,100),
Rect(260,260,20,100),
Rect(20,260,20,100),
Rect(360,260,20,100),
Rect(160,300,20,60),
Rect(220,300,20,60),
Rect(260,140,20,100)
)
#Pacman Box
Rect(160,170,80,40)
Rect(180,160,40,15)
Line(160,170,180,170, lineWidth=4)
Line(220,170,240,170, lineWidth=4)
Line(160,170,160,210, lineWidth=4)
Line(160,210,240,210, lineWidth=4)
Line(240,170,240,210)

#Coins
coin1=Circle(30,30,4, fill='orange')
coin2=Circle(50,30,4, fill='orange')
coin3=Circle(70,30,4, fill='orange')
coin4=Circle(90,30,4, fill='orange')
coin5=Circle(110,30,4, fill='orange')
coin6=Circle(130,30,4, fill='orange')
coin7=Circle(150,30,4, fill='orange')
coin8=Circle(170,30,4, fill='orange')
coin9=Circle(230,30,4, fill='orange')
coin10=Circle(250,30,4, fill='orange')
coin11=Circle(270,30,4, fill='orange')
coin12=Circle(290,30,4, fill='orange')
coin13=Circle(310,30,4, fill='orange')
coin14=Circle(330,30,4, fill='orange')
coin15=Circle(350,30,4, fill='orange')
coin16=Circle(370,30,4, fill='orange')
coin17=Circle(30,50,4, fill='orange')
coin18=Circle(90,50,4, fill='orange')
coin19=Circle(170,50,4, fill='orange')
coin20=Circle(230,50,4, fill='orange')
coin21=Circle(310,50,4, fill='orange')
coin22=Circle(370,50,4, fill='orange')
coin23=Circle(30,70,4, fill='orange')
coin24=Circle(50,70,4, fill='orange')
coin25=Circle(70,70,4, fill='orange')
coin26=Circle(90,70,4, fill='orange')
coin27=Circle(110,70,4, fill='orange')
coin28=Circle(130,70,4, fill='orange')
coin29=Circle(150,70,4, fill='orange')
coin30=Circle(170,70,4, fill='orange')
coin31=Circle(190,70,4, fill='orange')
coin32=Circle(210,70,4, fill='orange')
coin33=Circle(230,70,4, fill='orange')
coin34=Circle(250,70,4, fill='orange')
coin35=Circle(270,70,4, fill='orange')
coin36=Circle(290,70,4, fill='orange')
coin37=Circle(310,70,4, fill='orange')
coin38=Circle(330,70,4, fill='orange')
coin39=Circle(350,70,4, fill='orange')
coin40=Circle(370,70,4, fill='orange')
coin41=Circle(30,90,4, fill='orange')
coin42=Circle(90,90,4, fill='orange')
coin43=Circle(130,90,4, fill='orange')
coin44=Circle(270,90,4, fill='orange')
coin45=Circle(310,90,4, fill='orange')
coin46=Circle(370,90,4, fill='orange')
coin47=Circle(30,110,4, fill='orange')
coin48=Circle(50,110,4, fill='orange')
coin49=Circle(70,110,4, fill='orange')
coin50=Circle(90,110,4, fill='orange')
coin51=Circle(130,110,4, fill='orange')
coin52=Circle(150,110,4, fill='orange')
coin53=Circle(170,110,4, fill='orange')
coin54=Circle(230,110,4, fill='orange')
coin55=Circle(250,110,4, fill='orange')
coin56=Circle(270,110,4, fill='orange')
coin57=Circle(310,110,4, fill='orange')
coin58=Circle(330,110,4, fill='orange')
coin59=Circle(350,110,4, fill='orange')
coin60=Circle(370,110,4, fill='orange')

coin61=Circle(90,130,4, fill='orange')
coin62=Circle(90,150,4, fill='orange')
coin63=Circle(90,170,4, fill='orange')
coin64=Circle(90,190,4, fill='orange')
coin65=Circle(90,210,4, fill='orange')
coin66=Circle(90,230,4, fill='orange')
coin67=Circle(90,250,4, fill='orange')
coin68=Circle(310,130,4, fill='orange')
coin69=Circle(310,150,4, fill='orange')
coin70=Circle(310,170,4, fill='orange')
coin71=Circle(310,190,4, fill='orange')
coin72=Circle(310,210,4, fill='orange')
coin73=Circle(310,230,4, fill='orange')
coin74=Circle(310,250,4, fill='orange')

coin75=Circle(30,270,4, fill='orange')
coin76=Circle(50,270,4, fill='orange')
coin77=Circle(70,270,4, fill='orange')
coin78=Circle(90,270,4, fill='orange')
coin79=Circle(130,270,4, fill='orange')
coin80=Circle(150,270,4, fill='orange')
coin81=Circle(170,270,4, fill='orange')
coin82=Circle(230,270,4, fill='orange')
coin83=Circle(250,270,4, fill='orange')
coin84=Circle(270,270,4, fill='orange')
coin85=Circle(310,270,4, fill='orange')
coin86=Circle(330,270,4, fill='orange')
coin87=Circle(350,270,4, fill='orange')
coin88=Circle(370,270,4, fill='orange')
coin89=Circle(30,290,4, fill='orange')
coin90=Circle(90,290,4, fill='orange')
coin91=Circle(130,290,4, fill='orange')
coin92=Circle(270,290,4, fill='orange')
coin93=Circle(310,290,4, fill='orange')
coin94=Circle(370,290,4, fill='orange')
coin95=Circle(30,310,4, fill='orange')
coin96=Circle(50,310,4, fill='orange')
coin97=Circle(70,310,4, fill='orange')
coin98=Circle(90,310,4, fill='orange')
coin99=Circle(110,310,4, fill='orange')
coin100=Circle(130,310,4, fill='orange')
coin101=Circle(170,310,4, fill='orange')
coin102=Circle(190,310,4, fill='orange')
coin103=Circle(210,310,4, fill='orange')
coin104=Circle(230,310,4, fill='orange')
coin105=Circle(270,310,4, fill='orange')
coin106=Circle(290,310,4, fill='orange')
coin107=Circle(310,310,4, fill='orange')
coin108=Circle(330,310,4, fill='orange')
coin109=Circle(350,310,4, fill='orange')
coin110=Circle(370,310,4, fill='orange')
coin111=Circle(30,330,4, fill='orange')
coin112=Circle(130,330,4, fill='orange')
coin113=Circle(170,330,4, fill='orange')
coin114=Circle(230,330,4, fill='orange')
coin115=Circle(270,330,4, fill='orange')
coin116=Circle(370,330,4, fill='orange')
coin117=Circle(30,350,4, fill='orange')
coin118=Circle(50,350,4, fill='orange')
coin119=Circle(70,350,4, fill='orange')
coin120=Circle(90,350,4, fill='orange')
coin121=Circle(110,350,4, fill='orange')
coin122=Circle(130,350,4, fill='orange')
coin123=Circle(150,350,4, fill='orange')
coin124=Circle(170,350,4, fill='orange')
coin125=Circle(230,350,4, fill='orange')
coin126=Circle(250,350,4, fill='orange')
coin127=Circle(270,350,4, fill='orange')
coin128=Circle(290,350,4, fill='orange')
coin129=Circle(310,350,4, fill='orange')
coin130=Circle(330,350,4, fill='orange')
coin131=Circle(350,350,4, fill='orange')
coin132=Circle(370,350,4, fill='orange')

#Pacman
pacman=Group(
    Circle(200,150,8, fill='yellow'),
    Line(200,145,205,150),
    Line(200,155,205,150),
    Line(200,145,195,150, fill=None),
    Line(200,155,195,150, fill=None)
    )

#Nodes
#Vertical Nodes
#top
verticalNodes = Group(
Line(20,20,40,20, fill='darkBlue'),
Line(80,20,100,20, fill='darkBlue'),
Line(160,20,180,20, fill='darkBlue'),
Line(220,20,240,20, fill='darkBlue'),
Line(300,20,320,20, fill='darkBlue'),
Line(360,20,380,20, fill='darkBlue'),

Line(120,60,140,60, fill='darkBlue'),
Line(260,60,280,60, fill='darkBlue'),

Line(160,100,180,100, fill='darkBlue'),
Line(220,100,240,100, fill='darkBlue'),

Line(120,140,140,140, fill='darkBlue'),
Line(260,140,280,140, fill='darkBlue'),

Line(160,220,180,220, fill='darkBlue'),
Line(220,220,240,220, fill='darkBlue'),

Line(20,260,40,260, fill='darkBlue'),
Line(120,260,140,260, fill='darkBlue'),
Line(260,260,280,260, fill='darkBlue'),
Line(360,260,380,260, fill='darkBlue'),

Line(160,300,180,300, fill='darkBlue'),
Line(220,300,240,300, fill='darkBlue'),
#bottom
Line(160,80,180,80, fill='darkBlue'),
Line(220,80,240,80, fill='darkBlue'),

Line(20,120,40,120, fill='darkBlue'),
Line(120,120,140,120, fill='darkBlue'),

Line(260,120,280,120, fill='darkBlue'),
Line(360,120,380,120, fill='darkBlue'),

Line(160,160,180,160, fill='darkBlue'),
Line(220,160,240,160, fill='darkBlue'),

Line(120,240,140,240, fill='darkBlue'),
Line(260,240,280,240, fill='darkBlue'),

Line(160,280,180,280, fill='darkBlue'),
Line(220,280,240,280, fill='darkBlue'),

Line(80,320,100,320, fill='darkBlue'),
Line(300,320,320,320, fill='darkBlue'),

Line(20,360,40,360, fill='darkBlue'),
Line(120,360,140,360, fill='darkBlue'),
Line(160,360,180,360, fill='darkBlue'),
Line(220,360,240,360, fill='darkBlue'),
Line(260,360,280,360, fill='darkBlue'),
Line(360,360,380,360, fill='darkBlue')
)
#Horizontal Nodes
#left
horizontalNodes = Group(
Line(20,20,20,40, fill='darkBlue'),
Line(220,20,220,40, fill='darkBlue'),

Line(20,60,20,80, fill='darkBlue'),

Line(20,100,20,120, fill='darkBlue'),
Line(120,100,120,120, fill='darkBlue'),
Line(220,100,220,120, fill='darkBlue'),
Line(300,100,300,120, fill='darkBlue'),

Line(120,140,120,160, fill='darkBlue'),

Line(260,180,260,200, fill='darkBlue'),

Line(120,220,120,240, fill='darkBlue'),

Line(20,260,20,280, fill='darkBlue'),
Line(120,260,120,280, fill='darkBlue'),
Line(220,260,220,280, fill='darkBlue'),
Line(300,260,300,280, fill='darkBlue'),

Line(20,300,20,320, fill='darkBlue'),
Line(160,300,160,320, fill='darkBlue'),
Line(260,300,260,320, fill='darkBlue'),

Line(20,340,20,360, fill='darkBlue'),
Line(220,340,220,360, fill='darkBlue'),
#right
Line(180,20,180,40, fill='darkBlue'),
Line(380,20,380,40, fill='darkBlue'),

Line(380,60,380,80, fill='darkBlue'),

Line(100,100,100,120, fill='darkBlue'),
Line(180,100,180,120, fill='darkBlue'),
Line(280,100,280,120, fill='darkBlue'),
Line(380,100,380,120, fill='darkBlue'),

Line(280,140,280,160, fill='darkBlue'),

Line(140,180,140,200, fill='darkBlue'),

Line(280,220,280,240, fill='darkBlue'),

Line(100,260,100,280, fill='darkBlue'),
Line(180,260,180,280, fill='darkBlue'),
Line(280,260,280,280, fill='darkBlue'),
Line(380,260,380,280, fill='darkBlue'),

Line(140,300,140,320, fill='darkBlue'),
Line(240,300,240,320, fill='darkBlue'),
Line(380,300,380,320, fill='darkBlue'),

Line(180,340,180,360, fill='darkBlue'),
Line(380,340,380,360, fill='darkBlue')
)

#scoreboard
score=Label(0,330,380, fill='yellow', font='monospace', size=20, align='right')#number that increases when coin is collected
scoreTotal=Label('/132',370,380, fill='yellow', font='monospace', size=20, align='center')#total number of coins
endscreen=Group(#You Win! endscreen
    Rect(200,190,250,100,fill='white',align='center',border='lightGreen'),
    Label('You Win!',200,190,size=45,fill='green',align='center'),
    visible=False
    )

#onKeyHold
def onKeyHold(keys):
    if pacman.centerX >= 392:#moves pacman to other side of map
        pacman.centerX = 10
    if pacman.centerX <= 8:#moves pacman to other side of map
        pacman.centerX = 390
    if 'up' in keys and verticalLines.containsShape(pacman):#moves pacman up if 'up' key is held and is in vertical lines of the maze
        pacman.rotateAngle = 270
        pacman.centerY -= 2
    if 'down' in keys and verticalLines.containsShape(pacman):#moves pacman down if 'down' key is held and is in vertical lines of the maze
        pacman.rotateAngle = 90
        pacman.centerY += 2
    if 'left' in keys and horizontalLines.containsShape(pacman):#moves pacman left if 'left' key is held and is in horizontal lines of the maze
        pacman.rotateAngle = 180
        pacman.centerX -= 2
    if 'right' in keys and horizontalLines.containsShape(pacman):#moves pacman right if 'right' key is held and is in horizontal lines of the maze
        pacman.rotateAngle = 0
        pacman.centerX += 2
    if pacman.hitsShape(verticalNodes):#stops pacman from going out of the maze bounds vertically
        if pacman.centerY<45:
            pacman.centerY = 30
        elif pacman.centerY<85:
            pacman.centerY = 70
        elif pacman.centerY<125:
            pacman.centerY = 110
        elif pacman.centerY<165:
            pacman.centerY = 150
        elif pacman.centerY<205:
            pacman.centerY = 190
        elif pacman.centerY<245:
            pacman.centerY = 230
        elif pacman.centerY <285:
            pacman.centerY = 270
        elif pacman.centerY <325:
            pacman.centerY = 310
        elif pacman.centerY <365:
            pacman.centerY = 350
    if pacman.hitsShape(horizontalNodes):#stops pacman from going out of maze bounds horizontally
        if pacman.centerX<45:
            pacman.centerX = 30
        elif pacman.centerX<105:
            pacman.centerX = 90
        elif pacman.centerX<145:
            pacman.centerX = 130
        elif pacman.centerX<185:
            pacman.centerX = 170
        elif pacman.centerX<245:
            pacman.centerX = 230
        elif pacman.centerX<285:
            pacman.centerX = 270
        elif pacman.centerX < 325:
            pacman.centerX = 310
        elif pacman.centerX < 385:
            pacman.centerX = 370
    #adds points to score when pacman hits a coin
    if pacman.hitsShape(coin1) and coin1.visible==True:
        coin1.visible=False
        score.value+=1
    if pacman.hitsShape(coin2) and coin2.visible==True:
        coin2.visible=False
        score.value+=1
    if pacman.hitsShape(coin3) and coin3.visible==True:
        coin3.visible=False
        score.value+=1
    if pacman.hitsShape(coin4) and coin4.visible==True:
        coin4.visible=False
        score.value+=1
    if pacman.hitsShape(coin5) and coin5.visible==True:
        coin5.visible=False
        score.value+=1
    if pacman.hitsShape(coin6) and coin6.visible==True:
        coin6.visible=False
        score.value+=1
    if pacman.hitsShape(coin7) and coin7.visible==True:
        coin7.visible=False
        score.value+=1
    if pacman.hitsShape(coin8) and coin8.visible==True:
        coin8.visible=False
        score.value+=1
    if pacman.hitsShape(coin9) and coin9.visible==True:
        coin9.visible=False
        score.value+=1
    if pacman.hitsShape(coin9) and coin9.visible==True:
        coin9.visible=False
        score.value+=1
    if pacman.hitsShape(coin10) and coin10.visible==True:
        coin10.visible=False
        score.value+=1
    if pacman.hitsShape(coin11) and coin11.visible==True:
        coin11.visible=False
        score.value+=1
    if pacman.hitsShape(coin12) and coin12.visible==True:
        coin12.visible=False
        score.value+=1
    if pacman.hitsShape(coin13) and coin13.visible==True:
        coin13.visible=False
        score.value+=1
    if pacman.hitsShape(coin14) and coin14.visible==True:
        coin14.visible=False
        score.value+=1
    if pacman.hitsShape(coin15) and coin15.visible==True:
        coin15.visible=False
        score.value+=1
    if pacman.hitsShape(coin16) and coin16.visible==True:
        coin16.visible=False
        score.value+=1
    if pacman.hitsShape(coin17) and coin17.visible==True:
        coin17.visible=False
        score.value+=1
    if pacman.hitsShape(coin18) and coin18.visible==True:
        coin18.visible=False
        score.value+=1
    if pacman.hitsShape(coin19) and coin19.visible==True:
        coin19.visible=False
        score.value+=1
    if pacman.hitsShape(coin20) and coin20.visible==True:
        coin20.visible=False
        score.value+=1
    if pacman.hitsShape(coin21) and coin21.visible==True:
        coin21.visible=False
        score.value+=1
    if pacman.hitsShape(coin22) and coin22.visible==True:
        coin22.visible=False
        score.value+=1
    if pacman.hitsShape(coin23) and coin23.visible==True:
        coin23.visible=False
        score.value+=1
    if pacman.hitsShape(coin24) and coin24.visible==True:
        coin24.visible=False
        score.value+=1
    if pacman.hitsShape(coin25) and coin25.visible==True:
        coin25.visible=False
        score.value+=1
    if pacman.hitsShape(coin26) and coin26.visible==True:
        coin26.visible=False
        score.value+=1
    if pacman.hitsShape(coin27) and coin27.visible==True:
        coin27.visible=False
        score.value+=1
    if pacman.hitsShape(coin28) and coin28.visible==True:
        coin28.visible=False
        score.value+=1
    if pacman.hitsShape(coin29) and coin29.visible==True:
        coin29.visible=False
        score.value+=1
    if pacman.hitsShape(coin30) and coin30.visible==True:
        coin30.visible=False
        score.value+=1
    if pacman.hitsShape(coin31) and coin31.visible==True:
        coin31.visible=False
        score.value+=1
    if pacman.hitsShape(coin32) and coin32.visible==True:
        coin32.visible=False
        score.value+=1
    if pacman.hitsShape(coin33) and coin33.visible==True:
        coin33.visible=False
        score.value+=1
    if pacman.hitsShape(coin34) and coin34.visible==True:
        coin34.visible=False
        score.value+=1
    if pacman.hitsShape(coin35) and coin35.visible==True:
        coin35.visible=False
        score.value+=1
    if pacman.hitsShape(coin36) and coin36.visible==True:
        coin36.visible=False
        score.value+=1
    if pacman.hitsShape(coin37) and coin37.visible==True:
        coin37.visible=False
        score.value+=1
    if pacman.hitsShape(coin38) and coin38.visible==True:
        coin38.visible=False
        score.value+=1
    if pacman.hitsShape(coin39) and coin39.visible==True:
        coin39.visible=False
        score.value+=1
    if pacman.hitsShape(coin40) and coin40.visible==True:
        coin40.visible=False
        score.value+=1
    if pacman.hitsShape(coin41) and coin41.visible==True:
        coin41.visible=False
        score.value+=1
    if pacman.hitsShape(coin42) and coin42.visible==True:
        coin42.visible=False
        score.value+=1
    if pacman.hitsShape(coin43) and coin43.visible==True:
        coin43.visible=False
        score.value+=1
    if pacman.hitsShape(coin44) and coin44.visible==True:
        coin44.visible=False
        score.value+=1
    if pacman.hitsShape(coin45) and coin45.visible==True:
        coin45.visible=False
        score.value+=1
    if pacman.hitsShape(coin46) and coin46.visible==True:
        coin46.visible=False
        score.value+=1
    if pacman.hitsShape(coin47) and coin47.visible==True:
        coin47.visible=False
        score.value+=1
    if pacman.hitsShape(coin48) and coin48.visible==True:
        coin48.visible=False
        score.value+=1
    if pacman.hitsShape(coin49) and coin49.visible==True:
        coin49.visible=False
        score.value+=1
    if pacman.hitsShape(coin50) and coin50.visible==True:
        coin50.visible=False
        score.value+=1
    if pacman.hitsShape(coin51) and coin51.visible==True:
        coin51.visible=False
        score.value+=1
    if pacman.hitsShape(coin52) and coin52.visible==True:
        coin52.visible=False
        score.value+=1
    if pacman.hitsShape(coin53) and coin53.visible==True:
        coin53.visible=False
        score.value+=1
    if pacman.hitsShape(coin54) and coin54.visible==True:
        coin54.visible=False
        score.value+=1
    if pacman.hitsShape(coin55) and coin55.visible==True:
        coin55.visible=False
        score.value+=1
    if pacman.hitsShape(coin56) and coin56.visible==True:
        coin56.visible=False
        score.value+=1
    if pacman.hitsShape(coin57) and coin57.visible==True:
        coin57.visible=False
        score.value+=1
    if pacman.hitsShape(coin58) and coin58.visible==True:
        coin58.visible=False
        score.value+=1
    if pacman.hitsShape(coin59) and coin59.visible==True:
        coin59.visible=False
        score.value+=1
    if pacman.hitsShape(coin60) and coin60.visible==True:
        coin60.visible=False
        score.value+=1
    if pacman.hitsShape(coin61) and coin61.visible==True:
        coin61.visible=False
        score.value+=1
    if pacman.hitsShape(coin62) and coin62.visible==True:
        coin62.visible=False
        score.value+=1
    if pacman.hitsShape(coin63) and coin63.visible==True:
        coin63.visible=False
        score.value+=1
    if pacman.hitsShape(coin64) and coin64.visible==True:
        coin64.visible=False
        score.value+=1
    if pacman.hitsShape(coin65) and coin65.visible==True:
        coin65.visible=False
        score.value+=1
    if pacman.hitsShape(coin66) and coin66.visible==True:
        coin66.visible=False
        score.value+=1
    if pacman.hitsShape(coin67) and coin67.visible==True:
        coin67.visible=False
        score.value+=1
    if pacman.hitsShape(coin68) and coin68.visible==True:
        coin68.visible=False
        score.value+=1
    if pacman.hitsShape(coin69) and coin69.visible==True:
        coin69.visible=False
        score.value+=1
    if pacman.hitsShape(coin70) and coin70.visible==True:
        coin70.visible=False
        score.value+=1
    if pacman.hitsShape(coin71) and coin71.visible==True:
        coin71.visible=False
        score.value+=1
    if pacman.hitsShape(coin72) and coin72.visible==True:
        coin72.visible=False
        score.value+=1
    if pacman.hitsShape(coin73) and coin73.visible==True:
        coin73.visible=False
        score.value+=1
    if pacman.hitsShape(coin74) and coin74.visible==True:
        coin74.visible=False
        score.value+=1
    if pacman.hitsShape(coin75) and coin75.visible==True:
        coin75.visible=False
        score.value+=1
    if pacman.hitsShape(coin76) and coin76.visible==True:
        coin76.visible=False
        score.value+=1
    if pacman.hitsShape(coin77) and coin77.visible==True:
        coin77.visible=False
        score.value+=1
    if pacman.hitsShape(coin78) and coin78.visible==True:
        coin78.visible=False
        score.value+=1
    if pacman.hitsShape(coin79) and coin79.visible==True:
        coin79.visible=False
        score.value+=1
    if pacman.hitsShape(coin80) and coin80.visible==True:
        coin80.visible=False
        score.value+=1
    if pacman.hitsShape(coin81) and coin81.visible==True:
        coin81.visible=False
        score.value+=1
    if pacman.hitsShape(coin82) and coin82.visible==True:
        coin82.visible=False
        score.value+=1
    if pacman.hitsShape(coin83) and coin83.visible==True:
        coin83.visible=False
        score.value+=1
    if pacman.hitsShape(coin84) and coin84.visible==True:
        coin84.visible=False
        score.value+=1
    if pacman.hitsShape(coin85) and coin85.visible==True:
        coin85.visible=False
        score.value+=1
    if pacman.hitsShape(coin86) and coin86.visible==True:
        coin86.visible=False
        score.value+=1
    if pacman.hitsShape(coin87) and coin87.visible==True:
        coin87.visible=False
        score.value+=1
    if pacman.hitsShape(coin88) and coin88.visible==True:
        coin88.visible=False
        score.value+=1
    if pacman.hitsShape(coin89) and coin89.visible==True:
        coin89.visible=False
        score.value+=1
    if pacman.hitsShape(coin90) and coin90.visible==True:
        coin90.visible=False
        score.value+=1
    if pacman.hitsShape(coin91) and coin91.visible==True:
        coin91.visible=False
        score.value+=1
    if pacman.hitsShape(coin92) and coin92.visible==True:
        coin92.visible=False
        score.value+=1
    if pacman.hitsShape(coin93) and coin93.visible==True:
        coin93.visible=False
        score.value+=1
    if pacman.hitsShape(coin94) and coin94.visible==True:
        coin94.visible=False
        score.value+=1
    if pacman.hitsShape(coin95) and coin95.visible==True:
        coin95.visible=False
        score.value+=1
    if pacman.hitsShape(coin96) and coin96.visible==True:
        coin96.visible=False
        score.value+=1
    if pacman.hitsShape(coin97) and coin97.visible==True:
        coin97.visible=False
        score.value+=1
    if pacman.hitsShape(coin98) and coin98.visible==True:
        coin98.visible=False
        score.value+=1
    if pacman.hitsShape(coin99) and coin99.visible==True:
        coin99.visible=False
        score.value+=1
    if pacman.hitsShape(coin100) and coin100.visible==True:
        coin100.visible=False
        score.value+=1
    if pacman.hitsShape(coin101) and coin101.visible==True:
        coin101.visible=False
        score.value+=1
    if pacman.hitsShape(coin102) and coin102.visible==True:
        coin102.visible=False
        score.value+=1
    if pacman.hitsShape(coin103) and coin103.visible==True:
        coin103.visible=False
        score.value+=1
    if pacman.hitsShape(coin104) and coin104.visible==True:
        coin104.visible=False
        score.value+=1
    if pacman.hitsShape(coin105) and coin105.visible==True:
        coin105.visible=False
        score.value+=1
    if pacman.hitsShape(coin106) and coin106.visible==True:
        coin106.visible=False
        score.value+=1
    if pacman.hitsShape(coin107) and coin107.visible==True:
        coin107.visible=False
        score.value+=1
    if pacman.hitsShape(coin108) and coin108.visible==True:
        coin108.visible=False
        score.value+=1
    if pacman.hitsShape(coin109) and coin109.visible==True:
        coin109.visible=False
        score.value+=1
    if pacman.hitsShape(coin109) and coin109.visible==True:
        coin109.visible=False
        score.value+=1
    if pacman.hitsShape(coin110) and coin110.visible==True:
        coin110.visible=False
        score.value+=1
    if pacman.hitsShape(coin111) and coin111.visible==True:
        coin111.visible=False
        score.value+=1
    if pacman.hitsShape(coin112) and coin112.visible==True:
        coin112.visible=False
        score.value+=1
    if pacman.hitsShape(coin113) and coin113.visible==True:
        coin113.visible=False
        score.value+=1
    if pacman.hitsShape(coin114) and coin114.visible==True:
        coin114.visible=False
        score.value+=1
    if pacman.hitsShape(coin115) and coin115.visible==True:
        coin115.visible=False
        score.value+=1
    if pacman.hitsShape(coin116) and coin116.visible==True:
        coin116.visible=False
        score.value+=1
    if pacman.hitsShape(coin117) and coin117.visible==True:
        coin117.visible=False
        score.value+=1
    if pacman.hitsShape(coin118) and coin118.visible==True:
        coin118.visible=False
        score.value+=1
    if pacman.hitsShape(coin119) and coin119.visible==True:
        coin119.visible=False
        score.value+=1
    if pacman.hitsShape(coin120) and coin120.visible==True:
        coin120.visible=False
        score.value+=1
    if pacman.hitsShape(coin121) and coin121.visible==True:
        coin121.visible=False
        score.value+=1
    if pacman.hitsShape(coin122) and coin122.visible==True:
        coin122.visible=False
        score.value+=1
    if pacman.hitsShape(coin123) and coin123.visible==True:
        coin123.visible=False
        score.value+=1
    if pacman.hitsShape(coin124) and coin124.visible==True:
        coin124.visible=False
        score.value+=1
    if pacman.hitsShape(coin125) and coin125.visible==True:
        coin125.visible=False
        score.value+=1
    if pacman.hitsShape(coin126) and coin126.visible==True:
        coin126.visible=False
        score.value+=1
    if pacman.hitsShape(coin127) and coin127.visible==True:
        coin127.visible=False
        score.value+=1
    if pacman.hitsShape(coin128) and coin128.visible==True:
        coin128.visible=False
        score.value+=1
    if pacman.hitsShape(coin129) and coin129.visible==True:
        coin129.visible=False
        score.value+=1
    if pacman.hitsShape(coin130) and coin130.visible==True:
        coin130.visible=False
        score.value+=1
    if pacman.hitsShape(coin131) and coin131.visible==True:
        coin131.visible=False
        score.value+=1
    if pacman.hitsShape(coin132) and coin132.visible==True:
        coin132.visible=False
        score.value+=1
    if score.value >= 132:#when collected enough coins, the player wins the game and endscreen is visible
        endscreen.visible=True
        
#Extra Designs
Line(0,130,70,130, fill='darkBlue', lineWidth=4)
Line(0,170,70,170, fill='darkBlue', lineWidth=4)
Line(70,130,70,170, fill='darkBlue', lineWidth=4)
Line(330,130,400,130, fill='darkBLue', lineWidth=4)
Line(330,170,400,170, fill='darkBLue', lineWidth=4)
Line(330,130,330,170, fill='darkBLue', lineWidth=4)
Line(0,210,70,210, fill='darkBLue', lineWidth=4)
Line(0,250,70,250, fill='darkBLue', lineWidth=4)
Line(70,210,70,250, fill='darkBLue', lineWidth=4)
Line(330,210,400,210, fill='darkBLue', lineWidth=4)
Line(330,250,400,250, fill='darkBLue', lineWidth=4)
Line(330,210,330,250, fill='darkBLue', lineWidth=4)
Label('Pacman Maze',200,380, fill='yellow', font='monospace', size=20, align='center')