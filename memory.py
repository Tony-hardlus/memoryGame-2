from random import *
from turtle import *
from freegames import path


car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
#ARCR: Se inicializo variable para mensaje de victoria
numTiles = 0

# VRDL: Se crea variable para contar no. de taps
np = 0


#ARCR: Se creo Array para los indices como letras y simbolos, por si acaso las letras no bastan.

otherind =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
'X', 'Y', 'Z''*','?','¿','!','+','-','$']

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    # VRDL. Se define np como global para funcionamiento del contador
    global np
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    #ARCR: Se añadio metodo para mensaje de ganaste
        global numTiles
        numTiles+=1
        if numTiles == 32:
            print("Ganaste :D")
    # VRDL. Se crea contador de taps
    np+=1
    # VRDL. Se despliega número de taps en terminal
    print("Number of taps: "+str(np))


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # VRDL. Se centran números modificando valores sumados a x y y
        goto(x + 25, y + 2)
        color('black')
        tilmark = tiles[mark]
        #VRDL. Se añadió "align = "center""
        write(otherind[tilmark], font=('Arial', 30, 'normal'), align = "center")
        #ARCR: Se cambio para que las letras aparezcan.

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
