import turtle as t


def house(m, n, x):
    # TODO: Ilya
    t.up()
    t.goto(m, n)
    t.fd(2 * x)
    t.down()
    t.right(120)
    t.fd(2 * x)
    t.left(120)
    t.fd(2 * x)
    t.left(120)
    t.fd(2 * x)
    t.left(180)
    t.fd(2 * x)
    t.right(30)
    t.fd(2 * x)
    t.right(90)
    t.fd(2 * x)
    t.right(90)
    t.fd(2 * x)
    t.up()
    t.right(180)
    t.fd(x // 3)
    t.left(90)
    t.fd(x // 3)
    t.down()
    y = x // 3 * 2
    t.fd(2 * y)
    t.right(90)
    t.fd(2 * y)
    t.right(90)
    t.fd(2 * y)
    t.right(90)
    t.fd(2 * y)
    t.right(90)
    t.fd(y)
    t.right(90)
    t.fd(y)
    t.right(90)
    t.fd(y)
    t.right(180)
    t.fd(2 * y)
    t.right(180)
    t.fd(y)
    t.right(90)
    t.fd(y)
    t.right(180)
    t.fd(2 * y)
    t.left(90)
 

def rect(x1, y1, x2, y2, cl):
    t.color(cl)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.begin_fill()
    t.goto(x1, y2)
    t.goto(x2, y2)
    t.goto(x2, y1)
    t.goto(x1, y1)
    t.end_fill()
    t.color('black')


def triangle(x1, y1, x2, y2, x3, y3, cl):
    t.color(cl)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.end_fill()
    t.color('black')


def el(m, n, x):
    t.up()
    t.goto(m, n)
    t.fd(x / 2)
    t.down()
    for i in range(3):
        t.right(120)
        t.fd(x)
        t.left(120)
        t.fd(x)
        t.left(120)
        t.fd(x)
        t.left(120)
        t.fd(x)
        t.left(120)
        t.fd(x / 2)
        x += x / 2
    t.fd(x / 16)
    t.right(90)
    t.fd(x / 4)
    t.right(90)
    t.fd(x / 8)
    t.right(90)
    t.fd(x / 4)
    t.right(90)


def dog(m, n, x):
    # TODO: Platon
    t.up()
    t.goto(m, n)
    t.fd(4 * x)
    t.down()
    t.right(90)
    t.fd(2 * x)
    t.right(90)
    t.fd(2 * x)
    t.left(90)
    t.fd(2 * x)
    t.left(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.left(90)
    t.fd(x * 2)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)


def machine(m, n, x):
    # TODO: Platon
    t.up()
    t.goto(m, n)
    t.fd(4 * x)
    t.down()
    t.right(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(3 * x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)


def snk(m, n, y, x):
    # TODO: Nadia
    t.up()
    t.goto(m, n)
    t.left(180)
    t.down()
    t.fd(2 * y)
    t.left(90)
    t.fd(y)
    t.left(90)
    t.fd(3 * y)
    t.left(90)
    t.fd(4 * y)
    t.right(90)
    t.fd(4 * y)
    t.left(90)
    t.fd(3 * y)
    t.left(90)
    t.fd(7 * y)
    t.left(90)
    t.fd(7 * x)
    t.right(220)
    t.fd(3 * x)
    t.left(40)
    t.fd(3 * x)
    t.right(90)
    t.fd(10 * x)
    t.right(90)
    t.fd(2 * x)
    t.right(90)
    t.fd(8 * x)
    t.left(90)
    t.fd(x * 8)
    t.fd(x // 5)


def snk_1(m, n, y, x):
    # TODO: Nadia
    t.up()
    t.goto(m, n)
    t.right(90)
    t.down()
    t.fd(2 * y)
    t.left(90)
    t.fd(y)
    t.left(90)
    t.fd(3 * y)
    t.left(90)
    t.fd(4 * y)
    t.right(90)
    t.fd(6 * y)
    t.right(90)
    t.fd(5 * x)
    t.right(90)
    t.fd(3 * x)
    t.right(90)
    t.fd(3 * x)
    t.left(120)
    t.fd(2 * x)
    t.left(60)
    t.fd(2 * y)
    t.left(90)
    t.fd(7 * x)
    t.left(90)
    t.fd(9 * x)
    t.left(90)
    t.fd(16 * x)
    t.fd(x // 5)
    t.left(90)
    t.fd(8 * x)


t.speed(100)
house(-800, 350, 50)
el(-725, 100, 50)
machine(-550, 250, 30)
dog(-650, 100, 30)
snk(-100, 300, 30, 15)
snk_1(-100, -100, 30, 15)

# machine(100, 100, 100)

t.mainloop()

