import turtle

s = turtle.Screen()
s.title("Turtle Pattern Generator")
s.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

colors = ["red", "yellow", "cyan", "lime", "magenta"]

def spiral():
    for i in range(100):
        t.color(colors[i % 5])
        t.forward(i * 3)
        t.right(91)

def polygon():
    n = int(s.numinput("Polygon", "Enter sides:", 6))
    for i in range(n):
        t.color(colors[i % 5])
        t.forward(100)
        t.right(360 / n)

def fractal(length, level):
    if level == 0:
        t.forward(length)
    else:
        for angle in [0, 60, -120, 60]:
            fractal(length / 3, level - 1)
            t.left(angle)

def koch():
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.color("cyan")
    fractal(400, 4)

def flower():
    for i in range(36):
        t.color(colors[i % 5])
        t.circle(100)
        t.left(10)

def menu():
    t.clear()
    choice = s.textinput(
        "Pattern Generator",
        "1.Spiral  2.Polygon\n3.Koch Fractal  4.Flower"
    )
    if choice == "1": spiral()
    elif choice == "2": polygon()
    elif choice == "3": koch()
    elif choice == "4": flower()
    else: print("Invalid choice!")

    s.ontimer(menu, 100)

menu()
s.mainloop()