#!/bin/env python3
import time 
import turtle

"""Comentarios escritos sin acentos
La funciona arbolH pinta en pantalla primero la 
parte de izquierda de la H y regrea a la posicion
inicial y luego la parte derecha. 

Recibe como parametros: 
tam: tamaño de arbol H
xpos: coordenada X para inciar la pintar H
ypos: coordenada Y para inciar la pintar H
niveles: variable para controla nivel de recursividad
"""

def arbolH(tam,xpos,ypos,niveles):
    if niveles == 0 :
        return
    if niveles > 100 :
        return

    t = turtle.Turtle()
#Establecemos velocida de dibujo a nivel maximo
    t.speed(9)
#Cada nivel de recursion se pinta de un color diferente
    t.pencolor("blue")
    if niveles % 2 == 0:
        t.pencolor("red")
#No se muestra la pluma de dibujo hasta que no se coloca en 
#las coordenadas xpos, ypos
    t.hideturtle()
    t.penup()
    t.setx(xpos)
    t.sety(ypos)
    t.pendown()

#Se pinta cuadrante superior izquierdo del arbol H
    t.backward(tam/2)
    t.left(90)
    t.forward(tam)
    arbolH(tam/2,t.xcor(),t.ycor(),niveles-1)

#Se pinta cuadrante inferior izquierdo del arbol H
    t.left(180)
    t.forward(tam*2)
    arbolH(tam/2,t.xcor(),t.ycor(),niveles-1)

#Regresamos a la posicion original xpos,ypos
    t.left(180)
    t.forward(tam)
    t.right(90)
    t.forward(tam/2)

#Se pinta cuadrante superior derecho del arbol H
    t.forward(tam/2)
    t.left(90)
    t.forward(tam)
    arbolH(tam/2,t.xcor(),t.ycor(),niveles-1)

#Se pinta cuadrante inferior derecho del arbol H
    t.left(180)
    t.forward(tam*2)
    arbolH(tam/2,t.xcor(),t.ycor(),niveles-1)

#Regresamos a la posicion original xpos,ypos
    t.left(180)
    t.forward(tam)
    t.right(90)
    t.backward(tam/2)

arbolH(200,0,0,5) 
time.sleep(10)

