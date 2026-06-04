Rect(0,0,400,400,fill='skyblue')
Coin = Group(
    Circle(200, 200, 70, fill = 'gray'),
    Circle(200, 200, 65, fill='darkgray'),
    Circle(200, 200, 70, fill =None, border ='lightgray', dashes =True),
    Circle(200, 200, 65, fill =None, border ='lightgray'), visible = False
    )
 
    
Coin2 = Group(
    Oval(200, 200, 70, 50, fill = 'gray'),
    Oval(200, 200, 65,50, fill='darkgray'),
    Oval(200, 200, 70,50, fill =None, border ='lightGray', dashes =True),
    Oval(200, 200, 65, 50, fill =None, border ='lightgray'), visible = False
    )
#app.Head=(Circle(200,200, 30, fill='lightgray')), Polygon(174,200, 168,246,188,249,205,250,218,250,214,241,218,223,fill='lightgray'), 
#Polygon(240, 214,230,215,234,198, fill='lightgray'),Polygon(218,223,227,222,230,215, fill='lightgray'), Polygon(234,198, 217,198, 218,223,230,215,fill='lightgray')
#Polygon(233,198,233,185,222,185, fill ='lightgray'), Circle(216,183,17, fill='lightgray'), Circle(200,190, 30, fill='lightgray'),
#Polygon(163,238,158,232,170,200,180,204, fill='lightgray'), 
Button = Group(Rect(150, 300, 100, 50, fill='yellow'), Label('Flip',200,325),visible=False)
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
        Coin.visible=True
        Button.visible=True
        Tally.visible = True
        NumberHeads.visible = True
        NumberTails.visible=True
        app.Begin.visible = False
        Title.visible = False
        GameOn = True
    if(Button.hits(mouseX,mouseY) and GameOn ==True):
        Coinflip() 
        
        

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
    
def onStep():
    
    pass

def onAppstart(app):
    Begin()

def Begin():
    Coin.visible=False
        
