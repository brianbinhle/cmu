#background
app.background = 'lightSalmon' #sets the background to lightSalmon.. this represents the wall
Rect(0,250,400,150, fill='saddleBrown') #creates the floor which is saddleBrown

#dresser
dresser = Group(
    Rect(145,195,105,65, fill='brown'), #front of dresser
    Polygon(250,195,240,185,135,185,135,250,145,260,145,195, fill='brown') #side of dresser
    )

#tv
tv = Group(
    Rect(148,130,85,50), #main screen of tv
    Rect(188,180,9,10) #handle of tv
    )

#window
window = Group(
    Rect(5,100,90,90, fill=gradient('darkBlue','midnightBlue')), #sky
    Rect(5,100,90,90, fill=None, border='white', borderWidth=5), #outer window strips
    Line(5,145,95,145, fill='white', lineWidth=3), #center horizontal window strip
    Line(50,100,50,190, fill='white', lineWidth=3) #center vertical window strip
    )

#keys
key = Group(
    Circle(50,40,10, fill=None, border='yellow', borderWidth=5), #hole of the key
    Rect(47,45,6,30, fill='yellow'), #main segment
    Rect(43,65,10,6, fill='yellow'), #chip
    Rect(43,55,10,6, fill='yellow'), #chip
    Circle(50,75,3, fill='yellow'), #round edge
    Circle(43,58,3, fill='yellow'), #round edge
    Circle(43,68,3, fill='yellow') #round edge
    )
key.rotateAngle -= 90

#keys
key2 = Group(
    Circle(190,290,10, fill=None, border='yellow', borderWidth=5), #hole of the key
    Rect(187,295,6,30, fill='yellow'), #main
    Rect(183,315,10,6, fill='yellow'), #chip
    Rect(183,305,10,6, fill='yellow'), #chip
    Circle(190,325,3, fill='yellow'), #round edge
    Circle(183,308,3, fill='yellow'), #round edge
    Circle(183,318,3, fill='yellow') #round edge
    )
key2.rotateAngle -= 90

#bookshelf
bookshelf = Group(
    Rect(0,25,105,50), #main frame of bookshelf
    Rect(0,30,100,40, fill=gradient('red','blue','green','red','blue','green','red','blue','green','red','blue','green', start='left')), #books
    Line(0,50,100,50, lineWidth=50, dashes=(2,3)) #lines separating each book
    )

#carpet
carpet = Polygon(115,280,280,280,300,325,130,325, fill='lavender', border='black', borderWidth=3)

#couch
couch = Group(
    Rect(130,325,170,10, fill='green'), #seats of the couch
    Oval(130,315,14,7, fill='darkGreen'), #round edge
    Polygon(123,315,137,315,145,335,134,335, fill='darkGreen'), #arm of couch
    Polygon(123,315,124,347,134,365,134,335, fill='darkGreen'), #side of couch
    Rect(134,335,181,30, fill='darkGreen'), #back of couch
    Oval(219,335,170,35, fill='darkGreen'), #round top of couch
    Oval(300,315,14,7, fill='darkGreen'), #round edge
    Polygon(307,315,315,335,304,335,293,315, fill='darkGreen'), #arm of couch
    Polygon(293,315,294,347,304,365,304,335, fill='darkGreen') #side of couch
    )

#table
table = Group(
    Polygon(400,210,320,210,340,275,400,275), #top of table
    Rect(320,210,5,45), #leg
    Rect(340,275,5,25) #leg
    )
table.fill = 'papayaWhip'

flashlight = Circle(200, 200, 575, fill=None, border='black', borderWidth=500, opacity=90) #flashlight
message = Label('Find the Keys!',300,50, size=20, fill='red') #message that tells the readers to find the keys!
counter = Label(0,285,75, size=20, fill='red') #counter to count for when a key is found
totalNeeded = Label('/2',300,75, size=20, fill='red') #the total number of keys needed to finish the game

#finish the game screen
def completed(centerX,centerY):
    Star(centerX,centerY,5,5, fill='blue') #draws blue star
    Star(centerX-10,centerY+5,5,5, fill='yellow') #draws yellow star
    Star(centerX+10,centerY+5,5,5, fill='green') #draws green star
    Label('Completed!',centerX,centerY+20, size=15, font='monospace', bold=True, fill='white') #draws 'Completed!' label

#onMousePress function to make objects to disappear, add to the counter, and eventually finish the game
def onMousePress(x,y): #wherever you click
    if 0<x<105 and 25<y<75: #if you click on the bookshelf
        if bookshelf.visible == False and 27<x<75 and 42<y<62: #if the bookshelf is already invisible and you clicked on the key
            if key.visible == True: #if the key is already visible
                counter.value += 1 #add 1 to the counter when a key is found
                if counter.value == 2: #when all 2 keys are found
                    counter.fill='lawnGreen' #changes the color of the 2
                    totalNeeded.fill='lawnGreen' #changes the color of the '/2'
                    completed(x,y) #helper function to show the completed screen
            key.visible = False #make the key invisible
        else:
            bookshelf.visible = False #make the bookshelf invisible
    if 115<x<280 and 280<y<325: #if you click on the carpet
        if carpet.visible == False and 167<x<215 and 292<y<312: #if the carpet is already invisible and you clicked on the key
            if key2.visible == True: #if the key is already visible
                counter.value += 1 #add 1 to the counter when a key is found
                if counter.value == 2: #when all 2 keys are found
                    counter.fill='lawnGreen' #changes the color of the 2
                    totalNeeded.fill='lawnGreen' #changes the color of the '/2'
                    completed(x,y) #helper function to show the completed screen
            key2.visible = False #makes the key invisible
        else:
            carpet.visible = False #makes the carpet invisible
    if 148<x<233 and 130<y<180: #if you click on the tv
        tv.visible = False #make the tv invisible
    if 320<x<400 and 210<y<300: #if you click on the table
        table.visible = False #make the table invisible
    if 135<x<250 and 185<y<260: #if you click on the dresser
        dresser.visible = False #make the dresser invisible
    if 124<x<315 and 325<y<365: #if you click on the couch
        couch.visible = False #make the couch invisible
        
#onMouseMove function to move the flashlight
def onMouseMove(x,y):
    flashlight.centerX = x #enables the flashlight to move with your mouse on the x-axis
    flashlight.centerY = y #enables the flashlight to move with your mouse on the x-axis
#onMouseDrag function that also enables the flashlight to move when dragged
def onMouseDrag(x,y):
    onMouseMove(x,y) #helper function that makes it work for onMouseDrag too