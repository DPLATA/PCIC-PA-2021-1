import turtle

"""
referencias: Andrews, R. (2020). 
    Python Recursion - Fun with Fractals. 31 de octubre de 2020,
        de Codementor community Sitio web: 
            https://www.codementor.io/@info658/python-recursion-fun-with-fractals-19ha74wokh
"""
#velocidad del dibujo
SPEED = 6
#color de fondo y del trazo
BG_COLOR = "black"
PEN_COLOR = "white"
#dimensiones de la ventana en px
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
#dimensiones del trazo en px
DRAWING_WIDTH = 800
DRAWING_HEIGHT = 800
#grosor del trazo
PEN_WIDTH = 3
#titulo de la ventana
TITLE = "H Tree"
#numero de llamadas recursivas
RECURSIVE_CALLS = 3

#coordenadas del centro
x = - DRAWING_WIDTH / 2
y = - DRAWING_HEIGHT / 2
#coordenadas finales de alto y ancho
width = DRAWING_WIDTH
height = DRAWING_HEIGHT
count = RECURSIVE_CALLS

# recibe el objeto turtle y dos posiciones de donde a donde va a dibujar
def draw_line(tur, pos1, pos2):
    tur.penup()
    tur.goto(pos1[0], pos1[1])
    tur.pendown()
    tur.goto(pos2[0], pos2[1])

# Screen setup
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title(TITLE)
screen.bgcolor(BG_COLOR)
# Turtle artist (pen) setup
artist = turtle.Turtle()
artist.hideturtle()
artist.pensize(PEN_WIDTH)
artist.color(PEN_COLOR)
artist.speed(SPEED)

def recursive_draw(tur, x, y, width, height, count):
    #dibuja una H con tres lineas
    #linea transversal
    draw_line(artist,[x + width * 0.25, height // 2 + y],[x + width * 0.75, height // 2 + y],)
    #linea izquierda
    draw_line(artist,[x + width * 0.25, (height * 0.5) // 2 + y],[x + width * 0.25, (height * 1.5) // 2 + y],)
    #linea derecha
    draw_line(artist,[x + width * 0.75, (height * 0.5) // 2 + y],[x + width * 0.75, (height * 1.5) // 2 + y],)
    if count <= 0:
        #si el contador es 0 se detiene
        return
    else:
        #mientras el contador no sea 0 hace la llamada recursiva sobre la esquina en la que le toque dibujar
        #decrece el contador
        count = count - 1
        
        #dibuja en sentido contrario de las manecillas del reloj empezando desde la esquina inferior derecha
        recursive_draw(tur, x + width // 2, y, width // 2, height // 2, count) #abajo derecha
        recursive_draw(tur, x + width // 2, y + width // 2, width // 2, height // 2, count) #arriba derecha
        recursive_draw(tur, x, y + width // 2, width // 2, height // 2, count) #arriba izquierda
        recursive_draw(tur, x, y, width // 2, height // 2, count) #abajo izquierda

#driver code
recursive_draw(artist, - DRAWING_WIDTH / 2, - DRAWING_HEIGHT / 2, DRAWING_WIDTH, DRAWING_HEIGHT, RECURSIVE_CALLS)

turtle.done()