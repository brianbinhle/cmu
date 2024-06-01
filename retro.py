#background
Rect(0,0,400,130, fill=gradient('red','fuchsia', start='top'))
Rect(0,130,400,125, fill=gradient('fuchsia','indigo','black', start='top'))
Rect(0,255,400,145, fill='black')

#glasses
glasses = Group(
    Polygon(120,55,190,60,180,100,130,90, fill=gradient('darkGray','red','black', start='top'), opacity=80),
    Polygon(120,55,190,60,180,100,130,90, fill=None, border='mediumAquamarine'),
    Polygon(210,60,280,55,270,90,220,100, fill=gradient('darkGray','red','black', start='top'), opacity=80),
    Polygon(210,60,280,55,270,90,220,100, fill=None, border='mediumAquamarine'),
    Line(185,65,215,65, fill='mediumAquamarine', lineWidth=5),
    Line(120,55,162,40, fill='mediumAquamarine'),
    Line(280,55,238,40, fill='mediumAquamarine'),
    Polygon(162,40,163,40,166,42,168,49,165,43, fill='mediumAquamarine'),
    Polygon(238,40,237,40,237,42,232,49,235,43, fill='mediumAquamarine')
    )
glasses.opacity = 90

#sun
sun = Circle(200,340,100, fill=gradient('yellow','orange','darkOrange', start='top'))
blackLine=Line(0,260,400,260, lineWidth=5)
blackLine=Line(0,280,400,280, lineWidth=5)
blackLine=Line(0,300,400,300, lineWidth=5)
blackLine=Line(0,320,400,320, lineWidth=5)
blackLine=Line(0,340,400,340, lineWidth=5)

#heartbeats
heartbeat = Group(
Line(0,200,20,270),
Line(20,270,35,130),
Line(35,130,50,215),
Line(50,215,60,190),
Line(60,190,70,220),
Line(70,220,75,200)
)
heartbeat.fill='cyan'
heartbeat2 = Group(
    Line(200,200,220,270),
    Line(220,270,235,130),
    Line(235,130,250,215),
    Line(250,215,260,190),
    Line(260,190,270,220),
    Line(270,220,275,200)
    )
heartbeat2.fill='cyan'
flatLine = Line(heartbeat.right,200,heartbeat2.left,200, fill='cyan')
flatLine2 = Line(heartbeat2.right,200,heartbeat.left,200, fill='cyan')
flatLine3 = Line(heartbeat2.right,200,400,200, fill='cyan')

#animation that hides part of the heartbeat
animation=Group(
    Rect(0,130,400,125, fill=gradient('fuchsia','indigo','black', start='top')),
    Rect(0,255,400,16, fill='black')
    )

#blue road
road1=Line(0,360,400,360, lineWidth=15, fill=gradient('dodgerBlue','blue','dodgerBlue', start='left'))
road2=Line(0,360,-400,360, lineWidth=15, fill=gradient('dodgerBlue','blue','dodgerBlue', start='left'))
road3=Line(0,375,400,375, lineWidth=12, fill=gradient('dodgerBlue','blue','dodgerBlue', start='left'))
road4=Line(0,375,-400,375, lineWidth=12, fill=gradient('dodgerBlue','blue','dodgerBlue', start='left'))
road5=Line(0,387,400,387, lineWidth=9, fill=gradient('dodgerBlue','blue','dodgerBlue', start='left'))
road6=Line(0,387,-400,387, lineWidth=9, fill=gradient('dodgerBlue','blue','dodgerBlue', start='left'))

#character
head=Oval(199,205,50,60, fill='lawnGreen')
neck=Rect(190,225,20,15, fill='lawnGreen')
toprightarm=Rect(200,250,10,30, fill='lightGreen')
bottomrightarm=Rect(180,270,30,10, fill='lightGreen')
toprightleg=Polygon(190,295,220,295,215,340,195,340, fill='darkSeaGreen')
bottomrightleg=Rect(195,340,20,45, fill='darkSeaGreen')
torso=Polygon(190,240,181,249,190,295,205,310,220,295,210,240, fill='limeGreen')
topleftleg=Polygon(190,295,220,295,215,340,195,340, fill='seaGreen')
bottomleftleg=Rect(195,340,20,45, fill='seaGreen')
topleftarm=Rect(200,250,10,30, fill='springGreen')
bottomleftarm=Rect(180,270,30,10, fill='springGreen')

#character position properties
topleftarm.direction = -1
topleftarm.rotateAngle = -27.5

toprightarm.centerX += 5
toprightarm.rotateAngle = -21.5
toprightarm.direction = 1

topleftleg.direction = -1
bottomleftleg.direction = 1

toprightleg.centerX -= 5
bottomrightleg.top -= 8
toprightleg.rotateAngle = 12
toprightleg.direction = 1
bottomrightleg.direction = 1

#onStep function
def onStep():
    heartbeat.centerX -= 2 #moves the heartbeat
    heartbeat2.centerX -= 2 #moves the 2nd heartbeat
    if heartbeat.right < 0:#wraparounds heartbeat
        heartbeat.left = 400
    if heartbeat2.right < 0:#wraparounds 2nd heartbeat
        heartbeat2.left = 400
    if heartbeat.centerX < heartbeat2.centerX:#keeps flatLines between the heartbeats
        flatLine.x1 = heartbeat.right
        flatLine.x2 = heartbeat2.left
        flatLine2.x1 = 0
        flatLine2.x2 = heartbeat.left
        flatLine3.x1 = heartbeat2.right
        flatLine3.x2 = 400
    if heartbeat.centerX > heartbeat2.centerX:#keeps flatLines between the heartbeats
        flatLine.x1 = 0
        flatLine.x2 = heartbeat2.left
        flatLine2.x1 = heartbeat2.right
        flatLine2.x2 = heartbeat.left
        flatLine3.x1 = heartbeat.right
        flatLine3.x2 = 400
    if animation.left <= 392:#reveals more of the heartbeats
        animation.left += 8
    else: #resets the heartbeats when it reaches the end of the canvas
        animation.left = 0
    
    #moves the roads
    road1.right += 4
    road2.right += 4
    road3.right += 4
    road4.right += 4
    road5.right += 4
    road6.right += 4
    
    #wraparound for the roads
    if road1.left == 400:
        road1.right = 0
    if road2.left == 400:
        road2.right = 0
    if road3.left == 400:
        road3.right = 0
    if road4.left == 400:
        road4.right = 0
    if road5.left == 400:
        road5.right = 0
    if road6.left == 400:
        road6.right = 0

    topleftarm.rotateAngle += 2*topleftarm.direction #rotates topleftarm
    toprightarm.rotateAngle += 2*toprightarm.direction #rotates toprightarm
    #changes rotating direction of leftarm and adjusts movement
    if topleftarm.rotateAngle <= -51.5 or topleftarm.rotateAngle >= -1.5:
        topleftarm.direction *= -1
    if topleftarm.direction == 1:
        topleftarm.centerX -= 0.1
        bottomleftarm.right = topleftarm.right - 1
    if topleftarm.direction == -1:
        topleftarm.centerX += 0.1
        bottomleftarm.right = topleftarm.right - 2
    bottomleftarm.bottom = topleftarm.bottom
    #changes rotating direction of rightarm and adjusts movement
    if toprightarm.rotateAngle <= -51.5 or toprightarm.rotateAngle >= -1.5:
        toprightarm.direction *= -1
    if toprightarm.direction == 1:
        toprightarm.centerX -= 0.1
        bottomrightarm.right = toprightarm.right - 1
    if toprightarm.direction == -1:
        toprightarm.centerX += 0.1
        bottomrightarm.right = toprightarm.right - 2
    bottomrightarm.bottom = toprightarm.bottom
    #changes rotating direction of leftleg and adjusts movement
    if topleftleg.rotateAngle > 59.5 or topleftleg.rotateAngle < -39.5:
        topleftleg.direction *= -1
    if topleftleg.direction == 1:
        topleftleg.rotateAngle += 4
        topleftleg.centerX -= 0.4
        bottomleftleg.left = topleftleg.left + 1
        if topleftleg.rotateAngle <= 0:
            bottomleftleg.rotateAngle += 8
        if topleftleg.rotateAngle < -15:
            bottomleftleg.left = topleftleg.right - 15
            bottomleftleg.top = topleftleg.bottom - 20
        elif topleftleg.rotateAngle < -10:
            bottomleftleg.left = topleftleg.right - 20
            bottomleftleg.top = topleftleg.bottom - 15
        elif topleftleg.rotateAngle < -5:
            bottomleftleg.left = topleftleg.right - 20
            bottomleftleg.top = topleftleg.bottom - 10
        elif topleftleg.rotateAngle < 3:
            bottomleftleg.left = topleftleg.left + 4
        elif topleftleg.rotateAngle < 5:
            bottomleftleg.left = topleftleg.left + 2
    if topleftleg.direction == -1:
        topleftleg.rotateAngle -= 4
        topleftleg.centerX += 0.4
        bottomleftleg.left = topleftleg.left + 1
        if topleftleg.rotateAngle < 0:
            bottomleftleg.rotateAngle -= 8
        if topleftleg.rotateAngle < -15:
            bottomleftleg.left = topleftleg.right - 15
            bottomleftleg.top = topleftleg.bottom - 20
        elif topleftleg.rotateAngle < -10:
            bottomleftleg.left = topleftleg.right - 20
            bottomleftleg.top = topleftleg.bottom - 15
        elif topleftleg.rotateAngle < -5:
            bottomleftleg.left = topleftleg.right - 20
            bottomleftleg.top = topleftleg.bottom - 10
        elif topleftleg.rotateAngle < 3:
            bottomleftleg.left = topleftleg.left + 4
        elif topleftleg.rotateAngle < 5:
            bottomleftleg.left = topleftleg.left + 2
    #changes rotating direction of rightleg and adjusts movement
    if toprightleg.rotateAngle > 59.5 or toprightleg.rotateAngle < -39.5:
        toprightleg.direction *= -1
    if toprightleg.direction == 1:
        toprightleg.rotateAngle += 4
        toprightleg.centerX -= 0.4
        bottomrightleg.left = toprightleg.left + 1
        if toprightleg.rotateAngle <= 0:
            bottomrightleg.rotateAngle += 8
        if toprightleg.rotateAngle < -15:
            bottomrightleg.left = toprightleg.right - 15
            bottomrightleg.top = toprightleg.bottom - 20
        elif toprightleg.rotateAngle < -10:
            bottomrightleg.left = toprightleg.right - 20
            bottomrightleg.top = toprightleg.bottom - 15
        elif toprightleg.rotateAngle < -5:
            bottomrightleg.left = toprightleg.right - 20
            bottomrightleg.top = toprightleg.bottom - 10
        elif toprightleg.rotateAngle < 3:
            bottomrightleg.left = toprightleg.left + 4
        elif toprightleg.rotateAngle < 5:
            bottomrightleg.left = toprightleg.left + 2
    if toprightleg.direction == -1:
        toprightleg.rotateAngle -= 4
        toprightleg.centerX += 0.4
        bottomrightleg.left = toprightleg.left + 1
        if toprightleg.rotateAngle < 0:
            bottomrightleg.rotateAngle -= 8
        if toprightleg.rotateAngle < -15:
            bottomrightleg.left = toprightleg.right - 15
            bottomrightleg.top = toprightleg.bottom - 20
        elif toprightleg.rotateAngle < -10:
            bottomrightleg.left = toprightleg.right - 20
            bottomrightleg.top = toprightleg.bottom - 15
        elif toprightleg.rotateAngle < -5:
            bottomrightleg.left = toprightleg.right - 20
            bottomrightleg.top = toprightleg.bottom - 10
        elif toprightleg.rotateAngle < 3:
            bottomrightleg.left = toprightleg.left + 4
        elif toprightleg.rotateAngle < 5:
            bottomrightleg.left = toprightleg.left + 2
    
    if animation.left == 400: #removes glasses once heartbeats reach the end of the canvas
        glasses.clear()
    
    glasses.toFront()