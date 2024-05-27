from turtle import*
speed(20)
#start build castle
width(7)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of spuare

#drawing a door
begin_fill()
forward(70)
color('red')
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of door
#draw to 2and "spuare"
penup()
goto(100,50)
pendown()

color("black")

penup()
goto(-200,200)
pendown()

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)
#end to 2and spuare
#draw third spuare

penup()
goto(0,200)
pendown()

right(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)

penup()
goto(-400,200)
pendown()

left(30)
forward(120)
#end of third spuare
#draw fourse spuare
penup()
goto(200,200)
pendown()

left(120)
forward(120)

penup()
goto(-200,200)
pendown()

left(360)
forward(120)

penup()
goto(0,200)
pendown()

right(120)
forward(120)
#end forses spuare
#draw 1st tower
penup()
goto(-200,200)
pendown()

right(300)
forward(150)

right(-270)
forward(200)

right(90)
forward(150)
#end draw 1st tower
# draw a tower roof

penup()
goto(-200,200)
pendown()

right(180)
forward(150)

right(50)
forward(100)

right(65)
forward(140)
#end draw tower roof
#draw 2st tower
penup()
goto(400,400)
pendown()

left(25)
forward(200)


right(90)
forward(400)


right(90)
forward(200)

right(90)
forward(400)

right(45)
forward(150)
#end 2st tower
#draw a 2st tower roof
penup()
goto(600,400)
pendown()

right(-80)
forward(200)

penup()
goto(-590,0)
pendown()

left(-35)
forward(400)

left(90)
forward(200)

left(90)
forward(400)

left(90)
forward(200)

left(90)
forward(400)


left(40)
forward(150)
#end a 2st tower roof
#I connect with each other
penup()
goto(-790,405)
pendown()

left(-85)
forward(150)


penup()
goto(-115,405)
pendown()

left(135)
forward(480)

right(180)
forward(1000)


penup()
goto(400,0)
pendown()

right(180)
forward(1000)

#end of biuild tower






























































exitonclick()