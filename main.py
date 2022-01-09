import turtle


# TELA
wn = turtle.Screen()
wn.title("Pong by @Guilhermex2019")
wn.bgcolor("grey")
wn.setup(width=800, height=600)
wn.tracer(0)

# Barra A
barra_a = turtle.Turtle()
barra_a.speed(0)
barra_a.shape("square")
barra_a.color("white")
barra_a.shapesize(stretch_wid=5, stretch_len=1)
barra_a.penup()
barra_a.goto(-350, 0)

# Barra B
barra_b = turtle.Turtle()
barra_b.speed(0)
barra_b.shape("square")
barra_b.color("white")
barra_b.shapesize(stretch_wid=5, stretch_len=1)
barra_b.penup()
barra_b.goto(350, 0)

# scores
score_a = 0
score_b = 0

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Comic Sans", 18, "normal"))

# Bola
bola = turtle.Turtle()
bola.speed(1)
bola.shape("circle")
bola.color("red")
bola.shapesize(1, 1)
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = 0.2


#funcoes
def barra_a_up():
    y = barra_a.ycor()
    y += 20
    barra_a.sety(y)

def barra_a_down():
    y = barra_a.ycor()
    y -= 20
    barra_a.sety(y)

def barra_b_up():
    y = barra_b.ycor()
    y += 20
    barra_b.sety(y)

def barra_b_down():
    y = barra_b.ycor()
    y -= 20
    barra_b.sety(y)

def bordas(bola):

    global score_a
    global score_b

    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans", 18, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Comic Sans", 18, "normal"))


def limites(barra):
    if barra.ycor() > 260:
        barra.sety(260)

    if barra.ycor() < -260:
        barra.sety(-260)

#teclado
wn.listen()
wn.onkeypress(barra_a_up, "w")
wn.onkeypress(barra_a_down, "s")
wn.onkeypress(barra_b_up, "Up")
wn.onkeypress(barra_b_down, "Down")

#main game loop
while True:
    wn.update()

    #move the ball
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #chegando as bordas
    bordas(bola)
    limites(barra_a)
    limites(barra_b)

    #colisoes
    if bola.xcor() < -340 and bola.ycor() < barra_a.ycor() + 50 and bola.ycor() > barra_a.ycor() - 50:
        bola.dx *= -1
        #os.system("afplay bounce.wav&")

    elif bola.xcor() > 340 and bola.ycor() < barra_b.ycor() + 50 and bola.ycor() > barra_b.ycor() - 50:
        bola.dx *= -1

    if score_a == 10:
        break
    elif score_b == 10:
        break

if score_a > score_b:
    print("JOGADOR A VENCEU!")
else:
    print("JOGADOR B VENCEU!")


