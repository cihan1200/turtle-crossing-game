from turtle import Turtle, Screen
from cars import Cars
from scoreboard import Scoreboard
import time

# Screen setup
s = Screen()
s.setup(width=600, height=600)
s.title("Turtle Crossing Game")
s.tracer(0)

# Turtle setup
t = Turtle("turtle")
t.penup()
t.goto(x=0, y=-280)
t.setheading(90)

# Scoreboard setup
scoreboard = Scoreboard()
scoreboard.write_score()


# Adding event listeners
def move():
    t.forward(10)


s.listen()
s.onkeypress(fun=move, key="Up")
s.onkeypress(fun=move, key="w")

# Main game loop
cars = []
spawn_timer = 0
game_is_on = True
while game_is_on:
    # Update the screen every 0.1 seconds
    time.sleep(0.1)
    s.update()

    # Increment the spawn timer and add a new car every 5 iterations
    spawn_timer += 1
    if spawn_timer == 5:
        car = Cars()
        cars.append(car)
        spawn_timer = 0

    # Move all cars, remove those that are off the screen and detect collision with player
    for car in cars:
        car.move()
        if car.xcor() < -320:
            car.hideturtle()
            cars.remove(car)
        if car.distance(t) <= 25:
            scoreboard.game_over_message()
            game_is_on = False

    # Detect if player crossed
    if t.ycor() == 290:
        t.goto(x=0, y=-280)
        Cars.car_speed += 5
        scoreboard.level += 1
        scoreboard.clean_scoreboard()
        scoreboard.write_score()

s.mainloop()
