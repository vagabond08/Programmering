# For dette program, laver jeg en spiral fraktal ved brug af Turtle
import turtle
import math

def fiboPlot(n):
    a = 0
    b = 1
    kasse_a = a
    kasse_b = b

    # Her definerer vi farven som Turtle skal anvende
    x.pencolor("black")
    # For kassen til at ligge ned (Smagsbehag)
    x.setheading(90)

    # Her laver vi kassen 
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    # Vi fortsætter i Fibonacci serien
    temp = kasse_b
    kasse_b = kasse_b + kasse_a
    kasse_a = temp
    
    # Her tegner vi resten af kasserne.
    for i in range(1, n):
        x.backward(kasse_a * factor)
        x.right(90)
        x.forward(kasse_b * factor)
        x.left(90)
        x.forward(kasse_b * factor)
        x.left(90)
        x.forward(kasse_b * factor)


        temp = kasse_b
        kasse_b = kasse_b + kasse_a
        kasse_a = temp

    # Vi angiver startpositionen for tegningen
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # Her angiver vi farven som spiralen skal tegnes med
    x.pencolor("red")

    # Fibonacci Spiral Plot
    x.left(180)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b

# Her betegner 'factor' den multiplikative faktor, der udvider eller formindsker plottets skala med en bestemt faktor
factor = 1

# Vi tager inputtet for antallet af iterationer som programmet skal køre 
n = int(input('Indtast antallet af iterationer (skal være > 1): '))

# Her plotter vi Fibonacci Spiral Fraktalen & giver de tilsvarende Fibonacci-tal 
if n > 0:
    print("Fibonacci series for", n, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    fiboPlot(n)
    turtle.done()
else:
    print("Antallet af iterationer skal være > 0")