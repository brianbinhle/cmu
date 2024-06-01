app.cycle = True #creates a variable whether or not to pause the program
app.speed = 2 #creates a speed for the car to move along the road
app.message = Label('Invalid Input. Reset the program.',200,100, fill='red', size=20, visible=False) #message when user Input is invalid
app.setTimeOfDay = app.getTextInput("Enter an hour to start the day  (0-23): ") #user Input of hour in the day

if app.setTimeOfDay.isdigit(): #if the input is a number
    if 0 <= int(app.setTimeOfDay) < 24: #and an int between 0 and 24
        app.printTimeOfDay = Label(app.setTimeOfDay + ":00",375,375, size=50) #label that shows the current time
    else: #if the digit is not an hour between 0 and 24
        app.message.visible = True #invalid input
else: #if the input if not a number
    app.message.visible = True #invalid input

app.printTimeOfDay.right = 395 #adjusts the position of the label to the bottom right of the screen

background = Rect(0,0,400,250, fill=gradient('fuchsia','indigo', start='top')) #sets the background to a synthwave style

sunAndMoon = Group( #the sun and the moon
    Star(0,250,75,8, fill='gold', roundness=25),
    Circle(0,250,50, fill='yellow'),
    Star(400,250,75,8, fill=None, roundness=25),
    Circle(400,250,50, fill='lightGray')
    )

mountains = Group( #the mountains in the background
    Polygon(0,205,45,170,66,182,58,160,75,140,155,250,0,250, fill='lightBlue', opacity=50),
    Polygon(0,155,15,130,55,250,0,250, fill='lightBlue', opacity=50),
    Polygon(45,250,125,130,150,140,215,250, fill='lightBlue', opacity=50),
    Polygon(150,250,200,168,255,250, fill='lightBlue', opacity=50),
    Polygon(190,250,230,200,255,200,305,250, fill='lightBlue', opacity=50),
    Polygon(255,250,350,100,400,170,400,250, fill='lightBlue', opacity=50),
    Polygon(245,180,265,150,325,155,365,250,225,250, fill='lightBlue', opacity=50)
    )

road = Rect(0,250,400,60) #the black road

#white markings for the road
whiteLine1 = Rect(0,275,25,10, fill='white')
whiteLine2 = Rect(60,275,25,10, fill='white')
whiteLine3 = Rect(120,275,25,10, fill='white')
whiteLine4 = Rect(180,275,25,10, fill='white')
whiteLine5 = Rect(240,275,25,10, fill='white')
whiteLine6 = Rect(300,275,25,10, fill='white')
whiteLine7 = Rect(360,275,25,10, fill='white')
whiteLines = Group(whiteLine1,whiteLine2,whiteLine3,whiteLine4,whiteLine5,whiteLine6,whiteLine7)

Rect(0,310,400,90, fill='mediumSeaGreen') #grass

tree = Group( #the tree in the background
    Rect(50,200,25,50, fill='brown'),
    Circle(45,185,25, fill='oliveDrab'),
    Circle(80,180,25, fill='oliveDrab'),
    Circle(90,150,25, fill='oliveDrab'),
    Circle(80,125,25, fill='oliveDrab'),
    Circle(60,150,25, fill='oliveDrab'),
    Circle(55,130,25, fill='oliveDrab'),
    Circle(35,160,25, fill='oliveDrab')
    )
tree.centerX=320 #adjusts the position of the tree
tree.opacity=90 #changes the opacity to look more realistic

car = Group( #draws the car
    Rect(65,340,65,20, fill='maroon'),
    Polygon(75,340,80,320,120,320,125,340, fill='maroon'),
    Circle(80,360,12, fill='black'),
    Circle(115,360,12, fill='black'),
    Circle(80,360,10, fill='gray'),
    Circle(115,360,10, fill='gray'),
    Star(115,360,10,6, roundness=10),
    Star(80,360,10,6, roundness=10),
    Polygon(80,340,85,325,115,325,120,340, fill='turquoise')
    )
#sets the car's position
car.centerX = 250
car.centerY = 250

spaceText = 'press space to accelerate'#text for the directions on to press space
rText = 'Press r to reset and slow down'#text for the directions on to press r

carVroom = Group()
spaceLabel = Group()
spaceLabel2 = Group()
for i in range(len(spaceText)):#creates a label for the spaceText
    letter = spaceText[i]
    spaceLabel2.add(Label(letter,5+7*(i+1),350, size=15))
    
resetLabel = Group()
resetLabel2 = Group()
for i in range(len(rText)):#creates a label for the reset Text
    letter = rText[i]
    resetLabel2.add(Label(letter,5+7*(i+1),375, size=15))

def onKeyPress(key):#onKeyPress function
    if key == 'space': #if user presses space
        spaceLabel.clear() #clear any existing labels for spaceText
        spaceLabel2.clear()
        for i in range(len(spaceText)): #colors the word 'space' in the label
            letter = spaceText[i]
            if 6 <= i <= 10:
                color = 'red'
            else:
                color = 'black'
            spaceLabel.add(Label(letter,5+7*(i+1),350, fill=color, size=15))
        resetLabel.fill = 'black' #resets the color of the resetLabel because a new key press was triggered
        
        while car.centerX > 100: #draws the animation for the car moving
            carVroom.add(#by making many duplicates of the car over the movement and making it transluscent
            Rect(car.centerX-32,car.centerY-6,65,20, fill='maroon', opacity=10),
            Polygon(car.centerX-22,car.centerY-6,car.centerX-27,car.centerY-26,car.centerX+23,car.centerY-26,car.centerX+28,car.centerY-6, fill='maroon', opacity=10),
            Circle(car.centerX-27,car.centerY+14,12, fill='black', opacity=10),
            Circle(car.centerX+18,car.centerY+14,12, fill='black', opacity=10),
            Circle(car.centerX-27,car.centerY+14,10, fill='gray', opacity=10),
            Circle(car.centerX-18,car.centerY+14,10, fill='gray', opacity=10),
            Star(car.centerX+18,car.centerY+14,10,6, roundness=10, opacity=10),
            Star(car.centerX-27,car.centerY+14,10,6, roundness=10, opacity=10),
            Polygon(car.centerX-27,car.centerY-6,car.centerX-12,car.centerY-21,car.centerX+18,car.centerY-21,car.centerX+23,car.centerY-6, fill='turquoise', opacity=10)
            )
            car.centerX -= 5
        car.toFront()
        
        app.speed = 5 #speeds up the car when 'space' is pressed
        
    if key == 'r': #when r is pressed
        resetLabel.clear() #clear any existing labels for the resetText
        resetLabel2.clear()
        for i in range(len(rText)): #colors the word 'r' in the label
            letter = rText[i]
            if i == 6:
                color = 'red'
            else:
                color = 'black'
            resetLabel.add(Label(letter,5+7*(i+1),375, fill=color, size=15))
        spaceLabel.fill = 'black' #resets the color of the spaceLabel because a new key press was triggered
        
        carVroom.clear() #clears the animation
        car.centerX = 250 #resets to normal position
        
        app.speed = 2 #resets to normal speed

sunAndMoon.rotateAngle = int(app.setTimeOfDay)*15 - 90 #changes the rotateAngle based on the user input

def onStep():
    #moves the background to simulate the car moving
    for whiteLine in whiteLines:#moves the white lines
        whiteLine.centerX += app.speed
        if whiteLine.left > 400:
            whiteLine.right = 0
    for mountain in mountains:#moves the mountains
        mountain.centerX += app.speed
        if mountain.centerX > 400:
            mountain.centerX = 0
    for trees in tree:#moves the tree
        trees.centerX += app.speed
        if trees.centerX > 400:
            trees.centerX = 0
    
    if sunAndMoon.rotateAngle/15 + 6 < 23: #finds the values to change the clock value based on the current rotateAngle
        app.timeOfDay = sunAndMoon.rotateAngle/15 + 6
    else:
        app.timeOfDay = sunAndMoon.rotateAngle/15 - 18
    
    app.printTimeOfDay.value = str(int(app.timeOfDay+1)) + ":00" #adjusts the time to round to the hour and adjusts the text of the clock
    app.printTimeOfDay.right = 395 #adjusts the position of the clock to be centered
    
    if app.cycle == True: #if the app is not paused
        
        if sunAndMoon.rotateAngle < 360: #rotate the Sun and moon
            sunAndMoon.rotateAngle += 1.8
        else:
            sunAndMoon.rotateAngle = 0 #reset the sun and moon to cycle the rotateAngle

app.printTimeOfDay.toFront()