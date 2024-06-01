dimBackground=Rect(0,0,400,400, fill='black', opacity=50)
gameTitle=Label('Tiled',200,75, size=75, fill='cyan', font='orbitron', align='center')
playButton = Rect(200,200,125,75, align='center', fill='lime', border='green')
playButtonText=Label('Play',200,200, size=30, align='center', fill='limeGreen')
startScreen=Group(dimBackground,gameTitle,playButton,playButtonText)

goal = Group(
    Label('Objective: Use arrow keys to remove all tiles',200,15, size=15, font='orbitron'),
    Label('from the board before reaching the red tile',200,35, size=15, font='orbitron'),
    visible=False
    )
tryAgain = Label('Try Again',200,25, size=25, fill='red', font='orbitron', visible=False)
score = Label(0,355,380, size=20, font='orbitron')
Label('Levels Beaten:    /3',285,380, size=20, font='orbitron')
nextLevel = Group(
    Rect(200,200,135,50, fill='lime', border='green', align='center', borderWidth=1.5),
    Label('Next Level >>',200,200, fill='limeGreen', size=20),
    visible=False
    )
beatLevel = Label('You beat Level 1!',200,25, size=25, fill='limeGreen', font='orbitron', visible=False)
endScreen = Label('You won!',200,200, size=25, fill='limeGreen', font='orbitron', visible=False)

tile1_1=Rect(100,200,100,100, align='center', fill='lightGray', border='black')
tile1_2=Rect(100,300,100,100, align='center', fill='lightGray', border='black')
tile1_3=Rect(200,100,100,100, align='center', fill='lightGray', border='black')
tile1_4=Rect(200,200,100,100, align='center', fill='lightGray', border='black')
tile1_5=Rect(200,300,100,100, align='center', fill='lightGray', border='black')
tile1_6=Rect(300,100,100,100, align='center', fill='lightGray', border='black')
tile1_7=Rect(300,200,100,100, align='center', fill='lightGray', border='black')
tile1_end=Rect(300,300,100,100, align='center', fill='red', border='black')
level1=Group(tile1_1,tile1_2,tile1_3,tile1_4,tile1_5,tile1_6,tile1_7,tile1_end)

tile2_1=Rect(100,300,50,50, fill='lightGray', border='black')
tile2_2=Rect(150,300,50,50, fill='lightGray', border='black')
tile2_3=Rect(200,300,50,50, fill='lightGray', border='black')
tile2_4=Rect(250,300,50,50, fill='lightGray', border='black')
tile2_5=Rect(200,250,50,50, fill='lightGray', border='black')
tile2_6=Rect(250,250,50,50, fill='lightGray', border='black')
tile2_7=Rect(50,200,50,50, fill='lightGray', border='black')
tile2_8=Rect(100,200,50,50, fill='lightGray', border='black')
tile2_9=Rect(150,200,50,50, fill='lightGray', border='black')
tile2_10=Rect(200,200,50,50, fill='lightGray', border='black')
tile2_11=Rect(250,200,50,50, fill='lightGray', border='black')
tile2_12=Rect(300,200,50,50, fill='lightGray', border='black')
tile2_13=Rect(50,150,50,50, fill='lightGray', border='black')
tile2_14=Rect(100,150,50,50, fill='lightGray', border='black')
tile2_15=Rect(200,150,50,50, fill='lightGray', border='black')
tile2_16=Rect(250,150,50,50, fill='lightGray', border='black')
tile2_17=Rect(300,150,50,50, fill='lightGray', border='black')
tile2_18=Rect(100,100,50,50, fill='lightGray', border='black')
tile2_19=Rect(150,100,50,50, fill='lightGray', border='black')
tile2_20=Rect(200,100,50,50, fill='lightGray', border='black')
tile2_21=Rect(250,100,50,50, fill='lightGray', border='black')
tile2_22=Rect(300,100,50,50, fill='lightGray', border='black')
tile2_end=Rect(150,150,50,50, fill='red', border='black')
level2=Group(tile2_1,tile2_2,tile2_3,tile2_4,tile2_5,tile2_6,tile2_7,tile2_8,tile2_9,tile2_10,tile2_11,tile2_12,tile2_13,tile2_14,tile2_15,tile2_16,tile2_17,tile2_18,tile2_19,tile2_20,tile2_21,tile2_22,tile2_end, visible=False)

tile3_1=Rect(0,50,50,50, fill='lightGray', border='black')
tile3_2=Rect(50,50,50,50, fill='lightGray', border='black')
tile3_3=Rect(100,50,50,50, fill='lightGray', border='black')
tile3_4=Rect(200,50,50,50, fill='lightGray', border='black')
tile3_5=Rect(250,50,50,50, fill='lightGray', border='black')
tile3_6=Rect(300,50,50,50, fill='lightGray', border='black')
tile3_7=Rect(350,50,50,50, fill='lightGray', border='black')
tile3_8=Rect(0,100,50,50, fill='lightGray', border='black')
tile3_9=Rect(100,100,50,50, fill='lightGray', border='black')
tile3_10=Rect(150,100,50,50, fill='lightGray', border='black')
tile3_11=Rect(200,100,50,50, fill='lightGray', border='black')
tile3_12=Rect(250,100,50,50, fill='lightGray', border='black')
tile3_13=Rect(350,100,50,50, fill='lightGray', border='black')
tile3_14=Rect(0,150,50,50, fill='lightGray', border='black')
tile3_15=Rect(50,150,50,50, fill='lightGray', border='black')
tile3_16=Rect(100,150,50,50, fill='lightGray', border='black')
tile3_17=Rect(150,150,50,50, fill='lightGray', border='black')
tile3_18=Rect(250,150,50,50, fill='lightGray', border='black')
tile3_19=Rect(350,150,50,50, fill='lightGray', border='black')
tile3_20=Rect(0,200,50,50, fill='lightGray', border='black')
tile3_21=Rect(50,200,50,50, fill='lightGray', border='black')
tile3_22=Rect(150,200,50,50, fill='lightGray', border='black')
tile3_23=Rect(250,200,50,50, fill='lightGray', border='black')
tile3_24=Rect(300,200,50,50, fill='lightGray', border='black')
tile3_25=Rect(350,200,50,50, fill='lightGray', border='black')
tile3_26=Rect(0,200,50,50, fill='lightGray', border='black')
tile3_27=Rect(50,200,50,50, fill='lightGray', border='black')
tile3_28=Rect(150,200,50,50, fill='lightGray', border='black')
tile3_29=Rect(250,200,50,50, fill='lightGray', border='black')
tile3_30=Rect(300,200,50,50, fill='lightGray', border='black')
tile3_31=Rect(350,200,50,50, fill='lightGray', border='black')
tile3_32=Rect(0,250,50,50, fill='lightGray', border='black')
tile3_33=Rect(50,250,50,50, fill='lightGray', border='black')
tile3_34=Rect(150,250,50,50, fill='lightGray', border='black')
tile3_35=Rect(200,250,50,50, fill='lightGray', border='black')
tile3_36=Rect(250,250,50,50, fill='lightGray', border='black')
tile3_37=Rect(300,250,50,50, fill='lightGray', border='black')
tile3_38=Rect(350,250,50,50, fill='lightGray', border='black')
tile3_39=Rect(50,300,50,50, fill='lightGray', border='black')
tile3_40=Rect(100,300,50,50, fill='lightGray', border='black')
tile3_41=Rect(150,300,50,50, fill='lightGray', border='black')
tile3_42=Rect(200,300,50,50, fill='lightGray', border='black')
tile3_43=Rect(250,300,50,50, fill='lightGray', border='black')
tile3_44=Rect(300,300,50,50, fill='lightGray', border='black')
tile3_45=Rect(350,300,50,50, fill='lightGray', border='black')
tile3_end=Rect(0,300,50,50, fill='red', border='black')
level3=Group(tile3_1,tile3_2,tile3_3,tile3_4,tile3_5,tile3_6,tile3_7,tile3_8,tile3_9,tile3_10,tile3_11,tile3_12,tile3_13,tile3_14,tile3_15,tile3_16,tile3_17,tile3_18,tile3_19,tile3_20,tile3_21,tile3_22,tile3_23,tile3_24,tile3_25,tile3_26,tile3_27,tile3_28,tile3_29,tile3_30,tile3_31,tile3_32,tile3_33,tile3_34,tile3_35,tile3_36,tile3_37,tile3_38,tile3_39,tile3_40,tile3_41,tile3_42,tile3_43,tile3_44,tile3_45,tile3_end, visible=False)

restartLevelButton = Group(
    Rect(0,360,140,40, fill='crimson', border='darkRed'),
    Label('Restart Level',70,380,size=15,font='orbitron',fill='fireBrick'),
    visible=False
    )

def restartLevel1():
    tile1_1.visible=True
    tile1_2.visible=True
    tile1_3.visible=True
    tile1_4.visible=True
    tile1_5.visible=True
    tile1_6.visible=True
    tile1_7.visible=True
    tile1_end.visible=True
    playerTile.centerX=100
    playerTile.centerY=100

def restartLevel2():
    tile2_1.visible=True
    tile2_2.visible=True
    tile2_3.visible=True
    tile2_4.visible=True
    tile2_5.visible=True
    tile2_6.visible=True
    tile2_7.visible=True
    tile2_8.visible=True
    tile2_9.visible=True
    tile2_10.visible=True
    tile2_11.visible=True
    tile2_12.visible=True
    tile2_13.visible=True
    tile2_14.visible=True
    tile2_15.visible=True
    tile2_16.visible=True
    tile2_17.visible=True
    tile2_18.visible=True
    tile2_19.visible=True
    tile2_20.visible=True
    tile2_21.visible=True
    tile2_22.visible=True
    tile2_end.visible=True
    playerTile.centerX = 75
    playerTile.centerY = 325
    
def restartLevel3():
    tile3_1.visible=True
    tile3_2.visible=True
    tile3_3.visible=True
    tile3_4.visible=True
    tile3_5.visible=True
    tile3_6.visible=True
    tile3_7.visible=True
    tile3_8.visible=True
    tile3_9.visible=True
    tile3_10.visible=True
    tile3_11.visible=True
    tile3_12.visible=True
    tile3_13.visible=True
    tile3_14.visible=True
    tile3_15.visible=True
    tile3_16.visible=True
    tile3_17.visible=True
    tile3_18.visible=True
    tile3_19.visible=True
    tile3_20.visible=True
    tile3_21.visible=True
    tile3_22.visible=True
    tile3_23.visible=True
    tile3_24.visible=True
    tile3_25.visible=True
    tile3_26.visible=True
    tile3_27.visible=True
    tile3_28.visible=True
    tile3_29.visible=True
    tile3_30.visible=True
    tile3_31.visible=True
    tile3_32.visible=True
    tile3_33.visible=True
    tile3_34.visible=True
    tile3_35.visible=True
    tile3_36.visible=True
    tile3_37.visible=True
    tile3_38.visible=True
    tile3_39.visible=True
    tile3_40.visible=True
    tile3_41.visible=True
    tile3_42.visible=True
    tile3_43.visible=True
    tile3_44.visible=True
    tile3_45.visible=True
    tile3_end.visible=True
    playerTile.centerX = 175
    playerTile.centerY = 75

playerTile=Rect(100,100,98,98, align='center', fill='orange')

def onMousePress(mouseX,mouseY):
    if playButton.hits(mouseX,mouseY) and playButton.visible==True:
        dimBackground.visible = False
        gameTitle.visible = False
        playButton.visible = False
        playButtonText.visible = False
    if nextLevel.hits(mouseX,mouseY) and nextLevel.visible==True:
        beatLevel.visible=False
        dimBackground.visible=False
        nextLevel.visible=False
        level1.visible=False
        playerTile.width = 48
        playerTile.height = 48
        if score.value == 1:
            playerTile.visible = True
            playerTile.centerX = 75
            playerTile.centerY = 325
            level2.visible=True
        if score.value == 2:
            playerTile.visible = True
            playerTile.centerX = 175
            playerTile.centerY = 75
            level3.visible=True
        if score.value == 3:
            playerTile.visible = False
            endScreen.visible = True
    if restartLevelButton.hits(mouseX,mouseY):
        if score.value == 0 and dimBackground.visible == False:
            restartLevel1()
        if score.value == 1 and dimBackground.visible == False:
            restartLevel2()
        if score.value == 2 and dimBackground.visible == False:
            restartLevel3()
    if dimBackground.visible == False and score.value < 3:
        restartLevelButton.visible = True
        if tryAgain.visible == False:
            goal.visible = True

def onKeyPress(key):
    if score.value < 3:
        goal.visible = True
    tryAgain.visible=False
    if key == 'up' and dimBackground.visible == False:
        if score.value == 0:
            playerTile.centerY -= 100
            if level1.containsShape(playerTile) == False:
                playerTile.centerY += 100
        if score.value >= 1:
            playerTile.centerY -= 50
            if level2.containsShape(playerTile) == False and score.value == 1:
                playerTile.centerY += 50
            if level3.containsShape(playerTile) == False and score.value == 2:
                playerTile.centerY += 50
    if key == 'down' and dimBackground.visible == False:
        if score.value == 0:
            playerTile.centerY += 100
            if level1.containsShape(playerTile) == False:
                playerTile.centerY -= 100
        if score.value >= 1:
            playerTile.centerY += 50
            if level2.containsShape(playerTile) == False and score.value == 1:
                playerTile.centerY -= 50
            if level3.containsShape(playerTile) == False and score.value == 2:
                playerTile.centerY -= 50
    if key == 'left' and dimBackground.visible == False:
        if score.value == 0:
            playerTile.centerX -= 100
            if level1.containsShape(playerTile) == False:
                playerTile.centerX += 100
        if score.value >= 1:
            playerTile.centerX -= 50
            if level2.containsShape(playerTile) == False and score.value == 1:
                playerTile.centerX += 50
            if level3.containsShape(playerTile) == False and score.value == 2:
                playerTile.centerX += 50
    if key == 'right' and dimBackground.visible == False:
        if score.value == 0:
            playerTile.centerX += 100
            if level1.containsShape(playerTile) == False:
                playerTile.centerX -= 100
        if score.value >= 1:
            playerTile.centerX += 50
            if level2.containsShape(playerTile) == False and score.value == 1:
                playerTile.centerX -= 50
            if level3.containsShape(playerTile) == False and score.value == 2:
                playerTile.centerX -= 50
    if playerTile.hitsShape(tile1_1):
        tile1_1.visible = False
    if playerTile.hitsShape(tile1_2):
        tile1_2.visible = False
    if playerTile.hitsShape(tile1_3):
        tile1_3.visible = False
    if playerTile.hitsShape(tile1_4):
        tile1_4.visible = False
    if playerTile.hitsShape(tile1_5):
        tile1_5.visible = False
    if playerTile.hitsShape(tile1_6):
        tile1_6.visible = False
    if playerTile.hitsShape(tile1_7):
        tile1_7.visible = False
    if playerTile.hitsShape(tile1_end):
        tile1_end.visible = False
        if len(level1.children) == 0 and score.value==0:
            beatLevel.visible=True
            nextLevel.visible=True
            dimBackground.visible=True
            score.value = 1
            playerTile.visible = False
        elif len(level1.children) != 0:
            restartLevel1()
            tryAgain.visible=True
    if playerTile.hitsShape(tile2_1):
        tile2_1.visible = False
    if playerTile.hitsShape(tile2_2):
        tile2_2.visible = False
    if playerTile.hitsShape(tile2_3):
        tile2_3.visible = False
    if playerTile.hitsShape(tile2_4):
        tile2_4.visible = False
    if playerTile.hitsShape(tile2_5):
        tile2_5.visible = False
    if playerTile.hitsShape(tile2_6):
        tile2_6.visible = False
    if playerTile.hitsShape(tile2_7):
        tile2_7.visible = False
    if playerTile.hitsShape(tile2_8):
        tile2_8.visible = False
    if playerTile.hitsShape(tile2_9):
        tile2_9.visible = False
    if playerTile.hitsShape(tile2_10):
        tile2_10.visible = False
    if playerTile.hitsShape(tile2_11):
        tile2_11.visible = False
    if playerTile.hitsShape(tile2_12):
        tile2_12.visible = False
    if playerTile.hitsShape(tile2_13):
        tile2_13.visible = False
    if playerTile.hitsShape(tile2_14):
        tile2_14.visible = False
    if playerTile.hitsShape(tile2_15):
        tile2_15.visible = False
    if playerTile.hitsShape(tile2_16):
        tile2_16.visible = False
    if playerTile.hitsShape(tile2_17):
        tile2_17.visible = False
    if playerTile.hitsShape(tile2_18):
        tile2_18.visible = False
    if playerTile.hitsShape(tile2_19):
        tile2_19.visible = False
    if playerTile.hitsShape(tile2_20):
        tile2_20.visible = False
    if playerTile.hitsShape(tile2_21):
        tile2_21.visible = False
    if playerTile.hitsShape(tile2_22):
        tile2_22.visible = False
    if playerTile.hitsShape(tile2_end):
        tile2_end.visible = False
        if len(level2.children) == 0 and score.value==1:
            beatLevel.value='You beat Level 2!'
            beatLevel.visible=True
            nextLevel.visible=True
            dimBackground.visible=True
            playerTile.visible=False
            score.value = 2
        elif len(level2.children) != 0 and score.value==1:
            restartLevel2()
            tryAgain.visible=True
    if playerTile.hitsShape(tile3_1):
        tile3_1.visible = False
    if playerTile.hitsShape(tile3_2):
        tile3_2.visible = False
    if playerTile.hitsShape(tile3_3):
        tile3_3.visible = False
    if playerTile.hitsShape(tile3_4):
        tile3_4.visible = False
    if playerTile.hitsShape(tile3_5):
        tile3_5.visible = False
    if playerTile.hitsShape(tile3_6):
        tile3_6.visible = False
    if playerTile.hitsShape(tile3_7):
        tile3_7.visible = False
    if playerTile.hitsShape(tile3_8):
        tile3_8.visible = False
    if playerTile.hitsShape(tile3_9):
        tile3_9.visible = False
    if playerTile.hitsShape(tile3_10):
        tile3_10.visible = False
    if playerTile.hitsShape(tile3_11):
        tile3_11.visible = False
    if playerTile.hitsShape(tile3_12):
        tile3_12.visible = False
    if playerTile.hitsShape(tile3_13):
        tile3_13.visible = False
    if playerTile.hitsShape(tile3_14):
        tile3_14.visible = False
    if playerTile.hitsShape(tile3_15):
        tile3_15.visible = False
    if playerTile.hitsShape(tile3_16):
        tile3_16.visible = False
    if playerTile.hitsShape(tile3_17):
        tile3_17.visible = False
    if playerTile.hitsShape(tile3_18):
        tile3_18.visible = False
    if playerTile.hitsShape(tile3_19):
        tile3_19.visible = False
    if playerTile.hitsShape(tile3_20):
        tile3_20.visible = False
    if playerTile.hitsShape(tile3_21):
        tile3_21.visible = False
    if playerTile.hitsShape(tile3_22):
        tile3_22.visible = False
    if playerTile.hitsShape(tile3_23):
        tile3_23.visible = False
    if playerTile.hitsShape(tile3_24):
        tile3_24.visible = False
    if playerTile.hitsShape(tile3_25):
        tile3_25.visible = False
    if playerTile.hitsShape(tile3_26):
        tile3_26.visible = False
    if playerTile.hitsShape(tile3_27):
        tile3_27.visible = False
    if playerTile.hitsShape(tile3_28):
        tile3_28.visible = False
    if playerTile.hitsShape(tile3_29):
        tile3_29.visible = False
    if playerTile.hitsShape(tile3_30):
        tile3_30.visible = False
    if playerTile.hitsShape(tile3_31):
        tile3_31.visible = False
    if playerTile.hitsShape(tile3_32):
        tile3_32.visible = False
    if playerTile.hitsShape(tile3_33):
        tile3_33.visible = False
    if playerTile.hitsShape(tile3_34):
        tile3_34.visible = False
    if playerTile.hitsShape(tile3_35):
        tile3_35.visible = False
    if playerTile.hitsShape(tile3_36):
        tile3_36.visible = False
    if playerTile.hitsShape(tile3_37):
        tile3_37.visible = False
    if playerTile.hitsShape(tile3_38):
        tile3_38.visible = False
    if playerTile.hitsShape(tile3_39):
        tile3_39.visible = False
    if playerTile.hitsShape(tile3_40):
        tile3_40.visible = False
    if playerTile.hitsShape(tile3_41):
        tile3_41.visible = False
    if playerTile.hitsShape(tile3_42):
        tile3_42.visible = False
    if playerTile.hitsShape(tile3_43):
        tile3_43.visible = False
    if playerTile.hitsShape(tile3_44):
        tile3_44.visible = False
    if playerTile.hitsShape(tile3_45):
        tile3_45.visible = False
    if playerTile.hitsShape(tile3_end):
        tile3_end.visible = False
        if len(level3.children) == 0 and score.value==2:
            beatLevel.value='You beat Level 3!'
            beatLevel.visible=True
            nextLevel.visible=True
            dimBackground.visible=True
            score.value = 3
            playerTile.visible=False
        elif len(level3.children) != 0 and score.value==2:
            restartLevel3()
            tryAgain.visible=True
    if dimBackground.visible == True:
        restartLevelButton.visible = False
        goal.visible = False
    if tryAgain.visible == True:
        goal.visible = False
    
startScreen.toFront()