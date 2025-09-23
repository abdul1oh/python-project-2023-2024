# import turtle
# import turtle as t

# 1) activity
# turtle.home()
# turtle.shape("turtle")
# turtle.pendown()
# turtle.forward(100)
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# turtle.forward(100)

# 2) activity
# turtle.home()
# turtle.shape("turtle")
# t.pendown()
# t.forward(100)
# t.right(90)
# t.forward(100)
# turtle.left(90)
# t.forward(100)

# 3) activity
# turtle.home()
# turtle.shape("turtle")
# t.pendown()
# t.begin_fill()
# t.forward(100)
# t.right(90)
# t.forward(100)
# turtle.left(90)
# t.forward(100)
# t.end_fill()

# 4) activity
# turtle.home()
# turtle.shape("turtle")
# t.pendown()
# t.begin_fill()
# t.forward(200)
# t.right(90)
# t.forward(200)
# t.right(90)
# t.forward(200)
# t.right(90)
# t.forward(200)
# t.end_fill()

# 5) activity
# turtle.home()
# turtle.shape("turtle")
# t.pendown()
# t.begin_fill()
# t.circle(radius=100,extent=360, steps=40)
# t.end_fill()

# turtle.mainloop()



# 2)Circles
# import turtle
# import turtle as t
#
# turtle.home()
# turtle.shape("turtle")
# turtle.pendown()
#
# turtle.color("red")
# t.begin_fill()
# t.circle(radius=100)
# t.end_fill()
# t.right(90)
#
# turtle.color("blue")
# t.begin_fill()
# t.circle(radius=100)
# t.end_fill()
# t.right(90)
#
# turtle.color("green")
# t.begin_fill()
# t.circle(radius=100)
# t.end_fill()
# t.right(90)
#
# turtle.color("yellow")
# t.begin_fill()
# t.circle(radius=100)
# t.end_fill()
# t.right(90)
#
# turtle.mainloop()




# !) O`zbekiston bayrog`i
import turtle
import turtle as t
turtle.home()
turtle.shape("turtle")
turtle.pendown()

t.color("green")
t.begin_fill()
t.forward(250)
t.right(90)
t.forward(100)
t.right(90)
t.forward(500)
t.right(90)
t.forward(100)
t.right(90)
t.forward(250)
t.end_fill()

t.penup()
t.forward(250)
t.pendown()
t.back(500)

t.color("white")
t.begin_fill()
t.left(90)
t.forward(100)
t.right(90)
t.forward(500)
t.right(90)
t.forward(100)
t.end_fill()

t.penup()
t.back(100)
t.pendown()
t.color("blue")
t.begin_fill()
t.back(100)
t.right(90)
t.forward(500)
t.left(90)
t.forward(100)
t.left(90)
t.forward(500)
t.end_fill()

t.color("red")
t.pensize(10)
t.back(500)
t.penup()
t.right(90)
t.forward(100)
t.left(90)
t.pendown()
t.forward(500)




t.color("white")
t.penup()
t.pensize(2)
t.left(90)
t.forward(200)
t.left(90)
t.forward(280)
t.left(90)
t.forward(70)

turtle.penup()
turtle.goto(-230, 150)  # Move the turtle to the desired position
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(radius=40)  # Draw a circle (moon)
turtle.end_fill()

# Draw another overlapping circle to create a shadow effect
turtle.penup()
turtle.goto(-210, 150)  # Move the turtle slightly to the right
turtle.pendown()
turtle.color("blue")  # Color the overlapping part black to create a moon shadow
turtle.begin_fill()
turtle.circle(radius=35)  # Draw a smaller circle (shadow)
turtle.end_fill()

t.color("white")
for i in range(5):
    t.penup()
    t.goto(-147 + (i * 35),135)  # Har bir yulduz uchun yangi joylashuv
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(18)
        t.right(144)
    t.end_fill()

for i in range(4):
    t.penup()
    t.goto(-112 + (i * 35),160)  # Har bir yulduz uchun yangi joylashuv
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(18)
        t.right(144)
    t.end_fill()

for i in range(3):
    t.penup()
    t.goto(-77 + (i * 35),185)  # Har bir yulduz uchun yangi joylashuv
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(18)
        t.right(144)
    t.end_fill()


turtle.hideturtle()
turtle.mainloop()

