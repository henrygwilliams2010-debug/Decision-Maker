Rect(0,0,400,400,fill='skyblue')
Coin = Group(
    Circle(200, 200, 70, fill = 'gray'),
    Circle(200, 200, 65, fill='darkgray'),
    Circle(200, 200, 70, fill =None, border ='lightgray', dashes =True),
    Circle(200, 200, 65, fill =None, border ='lightgray'), visible = False
    )
GameOn = False
    


Button = Group(Rect(150, 300, 100, 35, fill='yellow'), Label('Flip',200,317),visible=False)
MultiButton = Group(Rect(150, 350, 100, 35, fill='yellow'), Label('Flip 10x',200,367),visible=False)
app.Begin = Group(Rect(150, 300, 100, 50, fill='yellow'), Label('Begin',200,325),)
Title =Label('Decision Maker', 200, 83, size = 50)
Rect(0,0,400,400, fill=None, border='Black')

Tally = Group(
    Line(332,24, 332,70),
    Line(300,35,363,35),
    Label('Heads', 314, 28),
    Label('Tails', 347, 28),visible = False
)
NumberHeads= Label(0, 315, 54, size=15,visible=False)
NumberTails= Label(0, 348, 54, size=15,visible=False)

Head=Label('Heads', 200, 200, size = 30, visible=False)
Tails=Label('Tails', 200, 200, size = 30, visible=False)

def onMousePress(mouseX,mouseY):
    if(app.Begin.hits(mouseX,mouseY)):
        Begin()
        GameOn = True
    if(Button.hits(mouseX,mouseY) and GameOn ==True):
        Coinflip() 
    if(MultiButton.hits(mouseX,mouseY) ):
        MultiFlip(10)
        
        

Screen = True
def Coinflip():
    Answer = randrange(1,3) 
    if (Answer == 1):

        print('Heads')
        Head.visible=True
        Tails.visible=False
        NumberHeads.value +=1
    else:
        print('tails')
        Head.visible=False
        Tails.visible=True
        NumberTails.value +=1
    print(Answer)
    
def MultiFlip(numFlips):
    for flip in range(numFlips):
        Answer =randrange(1,3)
        
        if(Answer ==1):
            NumberHeads.value+=1
            
        else:
            NumberTails.value+=1
            
    if(NumberHeads.value>NumberTails.value):
        Head.visible = True
        Tails.visible = False
    else:
        Head.visible = False
        Tails.visible = True
        


def Begin():
    
    Coin.visible=True
    Button.visible=True
    Tally.visible = True
    NumberHeads.visible = True
    NumberTails.visible=True
    app.Begin.visible = False
    Title.visible = False
    MultiButton.visible=True
    
