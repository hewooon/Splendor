from bangtal import *
from random import *
from enum import Enum
import random

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)
setGameOption(GameOption.ROOM_TITLE, False)
scene = Scene("Splendor","Images/배경.png")
mainScene = Scene("main","Images/background.png")
startScene = Scene("start","Images/background.png")
endScene = Scene("end","Images/background.png")
helpScene = Scene("help","Images/help배경.png")

start = Object("Images/start.png")
start.locate(mainScene,950,500)
start.setScale(2)
start.show()

help = Object("Images/help.png")
help.locate(mainScene,950,350)
help.setScale(2)
help.show()

home = Object("Images/home.png")
home.locate(helpScene,1150,600)
home.setScale(0.4)
home.show()

end = Object("Images/end.png")
end.locate(mainScene,950,200)
end.setScale(2)
end.show()

end1 = Object("Images/end.png")
end1.locate(endScene,950,350)
end1.setScale(2)
end1.show()

yours = Object("Images/yours.png")
yours.locate(scene,20,10)
yours.setScale(2)
yours.show()

skip = Object("Images/skip.png")
skip.locate(scene,300,10)
skip.setScale(2)
skip.show()

back = Object("Images/back.png")
back.locate(scene,20,10)
back.setScale(2)

vsAI = Object("Images/vsAI.png")
vsAI.locate(startScene,950,450)
vsAI.setScale(1.8)
vsAI.show()

vsPlayer = Object("Images/vsPlayer.png")
vsPlayer.locate(startScene,950,250)
vsPlayer.setScale(1.8)
vsPlayer.show()

def vsAI_onMouseAction(x,y,action):
    global withAI
    withAI = True
    scene.enter()
    myCardInfo()
    cardSetting()
    cardInfo()
    gemSetting()
    updateScore()
    updateMyGem()
vsAI.onMouseAction = vsAI_onMouseAction

def start_onMouseAction(x,y,action):
    startScene.enter()
start.onMouseAction = start_onMouseAction

def vsPlayer_onMouseAction(x,y,action):
    scene.enter()
    myCardInfo()
    cardSetting()
    cardInfo()
    gemSetting()
    updateScore()
    updateMyGem()
vsPlayer.onMouseAction = vsPlayer_onMouseAction

def help_onMouseAction(x,y,action):
    helpScene.enter()
help.onMouseAction = help_onMouseAction

def home_onMouseAction(x,y,action):
    mainScene.enter()
home.onMouseAction = home_onMouseAction

def end_onMouseAction(x,y,action):
    endGame()
end.onMouseAction = end_onMouseAction

def end1_onMouseAction(x,y,action):
    endGame()
end1.onMouseAction = end1_onMouseAction

checking_yours = False

def yours_onMouseAction(x,y,action):
    global checking_yours
    checking_yours = not checking_yours
    showYours()
    skip.hide()
    yours.hide()
    back.show()
yours.onMouseAction = yours_onMouseAction

def skip_onMouseAction(x,y,action):
    changeTurn()
skip.onMouseAction = skip_onMouseAction

def back_onMouseAction(x,y,action):
    goBack()
    skip.show()
    back.hide()
    yours.show()
back.onMouseAction = back_onMouseAction

step1_r = [ ['D',0,0,1,1,1,1],['D',0,0,0,1,1,2],['D',0,0,2,0,0,2],['D',0,1,0,3,0,1],['D',0,0,0,0,0,3],['D',0,0,1,1,2,1],['D',0,0,2,1,2,0],['D',1,0,0,0,4,0],
       ['R',0,2,1,0,0,0],['R',0,1,1,2,0,1],['R',0,1,1,1,0,1],['R',0,0,0,1,1,3],['R',0,3,0,0,0,0],['R',0,0,1,2,0,2],['R',0,2,0,0,0,2],['R',1,0,0,4,0,0],
       ['O',0,0,2,0,1,0],['O',0,0,0,2,2,0],['O',0,0,1,0,3,1],['O',0,1,1,1,1,0],['O',0,2,1,1,1,0],['O',0,2,0,2,1,0],['O',0,0,0,3,0,0],['O',1,4,0,0,0,0],
       ['E',0,0,3,0,0,0],['E',0,3,1,1,0,0],['E',0,0,0,0,2,1],['E',0,2,2,0,0,1],['E',0,1,2,0,1,1],['E',0,1,1,0,1,1],['E',0,0,2,2,0,0],['E',1,0,4,0,0,0],
       ['S',0,1,0,0,2,2],['S',0,1,0,2,0,0],['S',0,1,0,1,1,1],['S',0,0,0,0,3,0],['S',0,0,0,0,2,2],['S',0,1,0,1,1,2],['S',0,1,3,0,1,0],['S',1,0,0,0,0,4] ]
random.shuffle(step1_r)
step2_r = [ ['D',1,0,3,0,2,2],['D',1,2,3,0,0,3],['D',2,0,0,2,1,4],['D',2,0,5,0,0,0],['D',2,0,0,3,0,5],['D',3,6,0,0,0,0],
      ['R',1,0,0,3,2,2],['R',1,3,0,0,2,3],['R',2,0,5,0,3,0],['R',2,0,0,0,5,0],['R',2,4,2,1,0,0],['R',3,0,0,0,6,0],
      ['O',1,0,3,3,0,2],['O',1,2,2,0,3,0],['O',2,1,4,0,2,0],['O',2,0,0,0,0,5],['O',2,0,0,0,5,3],['O',3,0,0,0,0,6],
      ['E',1,3,0,2,3,0],['E',1,3,2,2,0,0],['E',2,0,1,0,4,2],['E',2,5,3,0,0,0],['E',2,5,0,0,0,0],['E',3,0,0,6,0,0],
      ['S',1,2,0,2,0,3],['S',1,0,2,3,3,0],['S',2,2,0,4,0,1],['S',2,0,0,5,0,0],['S',2,3,0,5,0,0],['S',3,0,6,0,0,0] ]
random.shuffle(step2_r)
step3_r = [ ['D',3,0,3,3,3,5],['D',4,0,0,7,0,0],['D',4,3,0,6,0,3],['D',5,3,0,7,0,0],
      ['R',3,5,3,3,0,3],['R',4,0,7,0,0,0],['R',4,3,6,0,3,0],['R',5,0,7,0,3,0],
      ['O',3,3,5,3,3,0],['O',4,0,3,0,6,3],['O',4,0,0,0,7,0],['O',5,0,0,0,7,3],
      ['E',3,3,3,0,5,3],['E',4,0,0,0,0,7],['E',4,0,0,3,3,6],['E',5,0,0,3,0,7],
      ['S',3,3,0,5,3,3],['S',4,7,0,0,0,0],['S',4,6,3,3,0,0],['S',5,7,3,0,0,0] ]
random.shuffle(step3_r)

p1 = Object("Images/player1.png")
p1.locate(scene,20,650)
p1.setScale(0.75)
p1.show() 

p2 = Object("Images/player2.png")
p2.locate(scene,20,651)
p2.setScale(0.75)

score = Object("Images/score.png")
score.locate(scene,300,650)
score.setScale(0.75)
score.show()

class Turn(Enum):
    PLAYER1 = 1
    PLAYER2 = 2
turn = Turn.PLAYER1

class Player():
    def __init__(self):
        self.score = 0
        self.gem = []
        self.dc = []
        self.onyx = []
        self.diamond = []
        self.ruby = []
        self.sapphire = []
        self.emerald = []
player1 = Player()
player2 = Player()
aiPlayer = Player()
withAI = False

for i in range(5):
    player1.gem.append(0)
    player2.gem.append(0)
    aiPlayer.gem.append(0)
    player1.dc.append(0)
    player2.dc.append(0)
    aiPlayer.dc.append(0)

def setNumber(num):
    object = 0
    if num == 0:
        object = Object("Images/0.png")
    elif num == 1:
        object = Object("Images/1.png")
    elif num == 2:
        object = Object("Images/2.png")
    elif num == 3:
        object = Object("Images/3.png")
    elif num == 4:
        object = Object("Images/4.png")
    elif num == 5:
        object = Object("Images/5.png")
    elif num == 6:
        object = Object("Images/6.png")
    elif num == 7:
        object = Object("Images/7.png")
    elif num == 8:
        object = Object("Images/8.png")
    elif num == 9:
        object = Object("Images/9.png")
    return object

field1 = []
field2 = []
field3 = []

for i in range(4):
    field1.append(step1_r[i])
    field2.append(step2_r[i])
    field3.append(step3_r[i])

def cardSetting():
    for i in range(3):
        for j in range(4):            # 필드에 카드 4장씩 세팅
            object = Object("Images/blank.png")
            object.locate(scene, 730+140*j,15+200*i)
            object.setScale(0.5)
            object.show()
            object.onMouseAction = lambda mx, my, action, ix = i+1, iy = j:card_onMouseAction(ix,iy)

deck1 = Object("Images/deck.png")
deck1.locate(scene, 590,15)
deck1.setScale(0.5)
deck1.show()

deck2 = Object("Images/deck.png")
deck2.locate(scene, 590,215)
deck2.setScale(0.5)
deck2.show()

deck3 = Object("Images/deck.png")
deck3.locate(scene, 590,415)
deck3.setScale(0.5)
deck3.show()

cardCount1 = 4
cardCount2 = 4
cardCount3 = 4
def card_onMouseAction(x,y):
    global turn, cardCount1, cardCount2, cardCount3, gemSelecting, checking_yours
    if checking_yours == False:
        if gemSelecting == False:
            if x==1:
                if(field1[y][0] != 0):
                   card=field1[y]
                else:
                   card=0
            elif x==2:
                if(field2[y][0] != 0):
                   card=field2[y]
                else:
                   card=0
            else:
                if(field3[y][0] != 0):
                   card=field3[y]
                else:
                   card=0

            if card != 0:
                isPossible = True
                player = player1
                if turn == Turn.PLAYER2:
                    player = player2
                for i in range(2,7):
                    if player.gem[i-2] < card[i] - player.dc[i-2]:
                        isPossible = False
                        showMessage("보석이 부족합니다.")
                if isPossible == True:

                    for i in range(2,7):
                        price = card[i] - player.dc[i-2]
                        if(price < 0):
                            price = 0
                        player.gem[i-2] -= price
                        gems[i-2].num += price
                   
                    classifyCard(card)
                    player.score += card[1]
                    player.dc[checkDC(card[0])] += 1

                    if x==1:
                        if(cardCount1 < 40):
                            field1[y] = step1_r[cardCount1]
                            cardCount1 += 1
                        else:
                            field1[y][0] = 0
                    elif x==2:
                        if(cardCount2 < 30):
                            field2[y] = step2_r[cardCount2]
                            cardCount2 += 1
                        else:
                            field2[y][0] = 0
                    else:
                        if(cardCount3 < 20):
                            field3[y] = step3_r[cardCount3]
                            cardCount3 += 1
                        else:
                            field3[y][0] = 0
                    if cardCount1==40:
                        deck1.hide()
                    if cardCount2==30:
                        deck2.hide()
                    if cardCount3==20:
                        deck3.hide()
                    changeTurn()
        else:
            showMessage("보석을 선택중입니다.")

def showYours():
    if turn == Turn.PLAYER1:
        p1.hide()
        p2.show()
        if withAI == True:
            p2.setImage("Images/playerAI.png")
            p2.locate(scene,100,650)
    else:
        p2.hide()
        p1.show()
    myCardInfo()
    updateMyGem()
    updateScore()

def goBack():
    global checking_yours
    if turn == Turn.PLAYER1:
        p2.hide()
        p1.show()
    else:
        p1.hide()
        p2.show()
    checking_yours = not checking_yours
    myCardInfo()
    updateMyGem()
    updateScore()

def changeTurn():
    global turn
    player = player1
    if withAI == False:
        if turn == Turn.PLAYER1:
            turn = Turn.PLAYER2
            player = player2
            showMessage("PLAYER2 차례입니다.")
            p1.hide()
            p2.show()
        else:
            turn = Turn.PLAYER1
            showMessage("PLAYER1 차례입니다.")
            p2.hide()
            p1.show()
        myCardInfo()
        updateMyGem()
        updateScore()
        gemSetting()
        cardSetting()
        cardInfo()
        if player1.score >= 15:
            showMessage("PLAYER1이 승리하였습니다.")
            endScene.enter()
        elif player2.score >= 15:
            showMessage("PLAYER2가 승리하였습니다.")
            endScene.enter()
    else:
        ai()
        myCardInfo()
        updateMyGem()
        updateScore()
        gemSetting()
        cardSetting()
        cardInfo()
        if player1.score >= 15:
            showMessage("PLAYER1이 승리하였습니다.")
            endScene.enter()
        elif aiPlayer.score >= 15:
            showMessage("AI가 승리하였습니다.")
            endScene.enter()

def classifyCard(x):
    player = player1
    if turn == Turn.PLAYER2:
        player = player2
    if x[0] == 'O':
        player.onyx.append(x)
    elif x[0] == 'D':
        player.diamond.append(x)
    elif x[0] == 'R':
        player.ruby.append(x)
    elif x[0] == 'S':
        player.sapphire.append(x)
    elif x[0] == 'E':
        player.emerald.append(x)

def checkDC(x):
    if(x == 'O'):
        tempDC = 0
    elif(x == 'D'):
        tempDC = 1
    elif(x == 'R'):
        tempDC = 2
    elif(x == 'S'):
        tempDC = 3
    elif(x == 'E'):
        tempDC = 4
    return tempDC

onyx = Object("Images/onyx.png")
diamond = Object("Images/diamond.png")
ruby = Object("Images/ruby.png")
sapphire = Object("Images/sapphire.png")
emerald = Object("Images/emerald.png")

onyx1 = Object("Images/onyx.png")
diamond1 = Object("Images/diamond.png")
ruby1 = Object("Images/ruby.png")
sapphire1 = Object("Images/sapphire.png")
emerald1 = Object("Images/emerald.png")

gems = [onyx,diamond,ruby,sapphire,emerald]
myGems = [onyx1,diamond1,ruby1,sapphire1,emerald1]
for i in range(5):
    gems[i].locate(scene,610+140*i,620)
    gems[i].show()
    gems[i].num = 4
    gems[i].click = 0
    gems[i].onMouseAction = lambda mx, my, action, ix = i, iy = 0:gem_onMouseAction(ix,iy, action)

    myGems[i].locate(scene, 475, 510-100*i)
    myGems[i].show()

gemSelecting = False
clickedKind = 0
def gem_onMouseAction(x, y, action):
    global turn, clickedKind, gemSelecting, checking_yours
    if checking_yours == False:
        temp = [0,0,0,0,0]
        gemSelecting = True
        sum = 0
        player = player1
        if turn == Turn.PLAYER1:
            for i in range(5):
                sum += player1.gem[i]
        else:
            player = player2
            for i in range(5):
                sum += player2.gem[i]

        isPossible = 0
        if gems[x].num > 0:
            if gems[x].click == 0:
                gems[x].click += 1
                gems[x].setScale(1.2)
                clickedKind += 1
                if clickedKind == 3:
                    isPossible = 1
                    if sum >= 8:
                        isPossible = -1

            else:
                if clickedKind == 1 and gems[x].num == 4 and sum < 9:
                    gems[x].click += 1
                    gems[x].setScale(1.2)
                    isPossible = 1
                elif clickedKind > 1 or gems[x].num < 4 or sum >= 9:
                    isPossible = -1
            if isPossible == 1:
                for i in range(5):
                    player.gem[i] += gems[i].click
                    gems[i].num -= gems[i].click
                    gems[i].click = 0
                    clickedKind = 0
                    isPossible = 0
                    gemSetting()

                gemSelecting = False
                for i in range(5):
                    gems[i].setScale(1)
                changeTurn()
            
            elif isPossible == -1:
                for i in range(5):
                        gems[i].click = 0
                        clickedKind = 0
                        isPossible = 0
                gemSelecting = False
                showMessage("다시 선택해주세요.")
                for i in range(5):
                    gems[i].setScale(1)

gemNum = []
for i in range(5):
    gemNum.append(Object("Images/empty.png"))
    
def gemSetting():
    global gemNum
    for i in range(5):
        gemNum[i].hide()
    gemNum.clear()
    for i in range(5):
        gemNum.append(setNumber(gems[i].num))
        gemNum[i].locate(scene, 670+140*i, 610)
        gemNum[i].setScale(0.5)
        gemNum[i].show()
        
p1_gem = []
p2_gem = []
ai_gem = []
for i in range(5):
    p1_gem.append(setNumber(0))
    p2_gem.append(setNumber(0))
    ai_gem.append(setNumber(0))

def updateMyGem():
    for i in range(5):
        p1_gem[i].hide()
        p2_gem[i].hide()
        ai_gem[i].hide()
    p1_gem.clear()
    p2_gem.clear()
    ai_gem.clear()
    for i in range(5):
        p1_gem.append(setNumber(player1.gem[i]))
        p2_gem.append(setNumber(player2.gem[i]))
        ai_gem.append(setNumber(aiPlayer.gem[i]))

    if turn == Turn.PLAYER1:
        if checking_yours == False:
            for i in range(5):
                p1_gem[i].locate(scene, 540, 505-100*i)  
                p1_gem[i].setScale(0.45)
                p1_gem[i].show()
        else:
            if withAI == False:
                for i in range(5):
                    p2_gem[i].locate(scene, 540, 505-100*i)  
                    p2_gem[i].setScale(0.45)
                    p2_gem[i].show()
            else:
                for i in range(5):
                    ai_gem[i].locate(scene, 540, 505-100*i)  
                    ai_gem[i].setScale(0.45)
                    ai_gem[i].show()
    else:
        if checking_yours == False:
            for i in range(5):
                p2_gem[i].locate(scene, 540, 505-100*i)  
                p2_gem[i].setScale(0.45)
                p2_gem[i].show()
        else:
            for i in range(5):
                p1_gem[i].locate(scene, 540, 505-100*i)  
                p1_gem[i].setScale(0.45)
                p1_gem[i].show()

def checkGem(x):
    if x == 'O':
        object = Object("Images/onyx.png")
    elif x == 'D':
        object = Object("Images/diamond.png")
    elif x == 'R':
        object = Object("Images/ruby.png")
    elif x == 'S':
        object = Object("Images/sapphire.png")
    elif x == 'E':
        object = Object("Images/emerald.png")
    return object

def cardInfo():
    for level in range(3):
        field = field1
        if level == 1:
            field = field2
        elif level == 2:
            field = field3
        
        for i in range(4):
            if(field[i][0] != 0):
                gem = checkGem(field[i][0])
                gem.locate(scene, 810+140*i, 150+200*level)
                gem.setScale(0.6)
                gem.show()

                point = setNumber(field[i][1])
                point.locate(scene, 740+140*i, 140+200*level)
                point.setScale(0.33)
                point.show()

                for j in range(2,7):
                    gemNum = setNumber(field[i][j])
                    if j < 5:
                        gemNum.locate(scene, 765+140*i, 125-25*j+200*level)
                    else:
                        gemNum.locate(scene, 815+140*i, 188-25*j+200*level)
                    gemNum.setScale(0.15)
                    gemNum.show()

def myCardInfo():
    global checking_yours, withAI
    if turn == Turn.PLAYER1:
        if checking_yours == False:
            player = player1
        else:
            player = player2
            if withAI == True:
                player = aiPlayer
    elif turn == Turn.PLAYER2:
        if checking_yours == False:
            player = player2
        else:
            player = player1
    box = Object("Images/box.png")
    box.locate(scene,0,90)
    box.show()
    for i in range(len(player.onyx)):
        onyx_card = Object("Images/blank.png")
        onyx_card.locate(scene, 12, 500-30*i)
        onyx_card.setScale(0.36)
        onyx_card.show()

        p_gem = checkGem('O')
        p_gem.locate(scene, 20, 600-30*i)
        p_gem.setScale(0.4)
        p_gem.show()

        p_point = setNumber(player.onyx[i][1])
        p_point.locate(scene, 70, 592-30*i)
        p_point.setScale(0.23)
        p_point.show()
        
    for i in range(len(player.diamond)):
        diamond_card = Object("Images/blank.png")
        diamond_card.locate(scene, 102, 500-30*i)
        diamond_card.setScale(0.36)
        diamond_card.show()

        p_gem = checkGem('D')
        p_gem.locate(scene, 110, 600-30*i)
        p_gem.setScale(0.4)
        p_gem.show()

        p_point = setNumber(player.diamond[i][1])
        p_point.locate(scene, 160, 592-30*i)
        p_point.setScale(0.23)
        p_point.show()
    for i in range(len(player.ruby)):
        ruby_card = Object("Images/blank.png")
        ruby_card.locate(scene, 192, 500-30*i)
        ruby_card.setScale(0.36)
        ruby_card.show()

        p_gem = checkGem('R')
        p_gem.locate(scene, 200, 600-30*i)
        p_gem.setScale(0.4)
        p_gem.show()

        p_point = setNumber(player.ruby[i][1])
        p_point.locate(scene, 250, 592-30*i)
        p_point.setScale(0.23)
        p_point.show()
    for i in range(len(player.sapphire)):
        sapphire_card = Object("Images/blank.png")
        sapphire_card.locate(scene, 282, 500-30*i)
        sapphire_card.setScale(0.36)
        sapphire_card.show()

        p_gem = checkGem('S')
        p_gem.locate(scene, 290, 600-30*i)
        p_gem.setScale(0.4)
        p_gem.show()

        p_point = setNumber(player.sapphire[i][1])
        p_point.locate(scene, 340, 592-30*i)
        p_point.setScale(0.23)
        p_point.show()
    for i in range(len(player.emerald)):
        emerald_card = Object("Images/blank.png")
        emerald_card.locate(scene, 372, 500-30*i)
        emerald_card.setScale(0.36)
        emerald_card.show()

        p_gem = checkGem('E')
        p_gem.locate(scene, 380, 600-30*i)
        p_gem.setScale(0.4)
        p_gem.show()

        p_point = setNumber(player.emerald[i][1])
        p_point.locate(scene, 430, 592-30*i)
        p_point.setScale(0.23)
        p_point.show()

p1_score = []
p2_score = []
ai_score = []
p1_score.append(setNumber(0))
p1_score.append(setNumber(0))
p2_score.append(setNumber(0))
p2_score.append(setNumber(0))
ai_score.append(setNumber(0))
ai_score.append(setNumber(0))

def updateScore():
    global turn, p1_score, p2_score, ai_score, checking_yours, withAI
    if turn == Turn.PLAYER1:
        if withAI == False:
            p_score = p2_score
            e_score = p1_score
            e2_score = ai_score
            player = player2
            if checking_yours == False:
                p_score = p1_score
                e_score = p2_score
                e2_score = ai_score
                player = player1
        else:
            if checking_yours == False:
                p_score = p1_score
                e_score = ai_score
                e2_score = p2_score
                player = player1
            else:
                p_score = ai_score
                e_score = p1_score
                e2_score = p2_score
                player = aiPlayer
    if turn == Turn.PLAYER2:
        p_score = p1_score
        e_score = p2_score
        e2_score = ai_score
        player = player1
        if checking_yours == False:
            p_score = p2_score
            e_score = p1_score
            e2_score = ai_score
            player = player2
   
    for i in range(2):
        p1_score[i].hide()
        p2_score[i].hide()
        ai_score[i].hide()
    p1_score.clear()
    p2_score.clear()
    ai_score.clear()

    p_score.append(setNumber(int(player.score/10)))
    p_score.append(setNumber(int(player.score%10)))
    e_score.append(setNumber(0))
    e_score.append(setNumber(0))
    e2_score.append(setNumber(0))
    e2_score.append(setNumber(0))

    p_score[0].locate(scene, 470, 637)  
    p_score[0].setScale(0.45)
    p_score[0].show()
    p_score[1].locate(scene, 510, 637)  
    p_score[1].setScale(0.45)
    p_score[1].show()

def ai():
    global gemNum, cardCount1, cardCount2, cardCount3 
    sum = 0
    count = 0
    getCard = True
    getGem = False
    max = 0
    level = 0
    maxIndex = 0
    for i in range(4):
        if field1[i][0]!=0:
            getCard = True
            for j in range(2,7):
                if aiPlayer.gem[j-2]<field1[i][j]-aiPlayer.dc[j-2]:
                    getCard = False
            if getCard == True:
                if field1[i][1] >= max:
                    max = field1[i][1]
                    level = 1
                    maxIndex = i
        else:
            getCard = False
    for i in range(4):
        if field2[i][0]!=0:
            for j in range(2,7):
                if aiPlayer.gem[j-2]<field2[i][j]-aiPlayer.dc[j-2]:
                    getCard = False
            if getCard == True:
                if field2[i][1] >= max:
                    max = field2[i][1]
                    level = 2
                    maxIndex = i
        else:
            getCard = False
    for i in range(4):
        if field3[i][0]!=0:
            for j in range(2,7):
                if aiPlayer.gem[j-2]<field3[i][j]-aiPlayer.dc[j-2]:
                    getCard = False
            if getCard == True:
                if field3[i][1] >= max:
                    max = field3[i][1]
                    level = 3
                    maxIndex = i
        else:
            getCard = False
    if level > 0:
        if level == 1:
            highScoreCard = field1[maxIndex]
        elif level == 2:
            highScoreCard = field2[maxIndex]
        else:
            highScoreCard = field3[maxIndex]
            
        if highScoreCard[0] == 'O':
            aiPlayer.onyx.append(highScoreCard)
        elif highScoreCard[0] == 'D':
            aiPlayer.diamond.append(highScoreCard)
        elif highScoreCard[0] == 'R':
            aiPlayer.ruby.append(highScoreCard)
        elif highScoreCard[0] == 'S':
            aiPlayer.sapphire.append(highScoreCard)
        elif highScoreCard[0] == 'E':
            aiPlayer.emerald.append(highScoreCard)

        aiPlayer.score += max
        for i in range(2,7):
            price = highScoreCard[i] - aiPlayer.dc[i-2]
            if(price < 0):
                price = 0
            aiPlayer.gem[i-2] -= price
            gems[i-2].num += price
        aiPlayer.dc[checkDC(highScoreCard[0])] += 1

        if level == 1:
            if(cardCount1 < 40):
                field1[maxIndex] = step1_r[cardCount1]
                cardCount1 += 1
            else:
                field1[maxIndex][0] = 0
        elif level == 2:
            if(cardCount2 < 30):
                field2[maxIndex] = step2_r[cardCount2]
                cardCount2 += 1
            else:
                field2[maxIndex][0] = 0
        else:
            if(cardCount3 < 20):
                field3[maxIndex] = step3_r[cardCount3]
                cardCount3 += 1
            else:
                field3[maxIndex][0] = 0

    else:
        for i in range(5):
            sum += aiPlayer.gem[i]

        gemTemp = [0,0,0,0,0]
        if sum < 8:
            for i in range(4,0,-1):
                for j in range(5):
                    if gems[j].num == i:    
                        gemTemp[j] += 1
                        count += 1
                    if count == 3:
                        getGem = True
                        break
                if getGem == True:
                    break
            if getGem == True:
                for i in range(5):
                    aiPlayer.gem[i] += gemTemp[i]
                    gems[i].num -= gemTemp[i]
        if sum == 8:
            for i in range(5):
                if gems[i].num == 4:
                    aiPlayer.gem[i] += 2
                    gems[i].num -= 2
                    getGem = True
                    break

startGame(mainScene)
