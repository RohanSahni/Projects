#Calculator sign how to place that next cell

Grocery = [["Puma", "Nike", "Bata", "Big Bazar"],
           ["Miniso", "AND", "Arrow", "Bose"],
           ["Central", "Titan", "COBB", "Briba"],
           ["Taco Bell", "Walk To Walk", "Punjabi By Nature", "Burger King"]]

print("Hello I am ")
a = input("What is your name \n")

print("Hello", a, "-")
print("Press 1-sarching something")
print("Press 2-want to play some games?")
print("Press 3-open calculator")


store = input()
store = store.lower()
user_result = []

if store == "1":
    print("Hello", a, "what are you finding")
    user = input()
    user = user.capitalize()
    for row_index, row_value in enumerate(Grocery):
        for col_index, col_value in enumerate(row_value):
            if user == col_value:
                user_result.append([row_index, col_index])
    if len(user_result) == 1:
        print("Yup! ",
              user,
              " is present at Floor ",
              user_result[0][0] + 1,
              " & Shop Number ",
              user_result[0][1] + 1,
              sep="")
    elif len(user_result) > 1:
        print(
            "Yes, Item ", user_result,
            " exists in the grocery tuple. These are located at cell indexes ")
        print(user_result)
    else:
        print("Sorry, we dont have", user, "store here")

elif store == "2":
    print("Which game do you want to play?")
    print("Press 1 to play-Rock,paper,scissors")
    print("Press 2 to play-Slot machine")
    print("Press 3 to play-Pong Game")

    game = input()
    if game == '1':
        print("😎😎😎😎😎😎😎😎😎😎😎ROCK-PAPER-SCISSORS😎😎😎😎😎😎😎😎😎😎😎")
        sc = 0
        su = 0
        print("welcome to the game ", a)
        b = int(
            input("Please enter the number of rounds you want to play::\n"))
        count = 0
        while count < b:
            count = count + 1
            import random
            user = int(
                input("Please enter rock(1),paper(2) or scissors(3)::\n"))
            if user == 1:
                user = 'rock'
            elif user == 2:
                user = 'paper'
            else:
                user = 'scissors'
            comp = random.randint(1, 3)
            if comp == 1:
                comp = ("rock")
            elif comp == 2:
                comp = ("scissors")
            else:
                comp = ("paper")
            print(comp)
            if user == "rock" and comp == "paper":
                print("computer wins")
                sc = sc + 1
            elif user == comp:
                print("tie")
            elif user == "scissors" and comp == "paper":
                print("user wins")
                su = su + 1
            elif user == "rock" and comp == "scissors":
                print("user wins")
                su = su + 1
            elif user == "paper" and comp == "scissors":
                print("computer wins")
                sc = sc + 1
            elif user == "scissors" and comp == "rock":
                print("computer wins")
                sc = sc + 1
            elif user == "paper" and comp == "rock":
                print("user wins")
                su = su + 1
            print("Round", count, "Score:")
            print("Computer Score", sc)
            print("user Score", su)
            print()
        if su > sc:
            print("User won")
            print("Thank you for playing", a)
        elif su == sc:
            print("Tie")
            print("Thank you for playing", a)
        else:
            print("Computer won")
            print("Thank you for playing", a)

    elif game == '2':
        import random
        print("Welcome To Slot Game")
        rules = input(
            "Do You Want To Know The Rules?\nPress Yes for Yes And N for No::\n"
        )
        rules = rules.upper()
        global credit
        credit = 10
        if rules == 'YES':
            print('''Welcome to the $$$$$$$$$$$$ Slot Machine $$$$$$$$$$$$$
                            ::::GAME RULES::::
    You'll start with Rs.10 and each turn costs Rs.2. You'll be asked if you want to quit.
    Answer with pressing q or not
    “rolls” two of the same symbol\t -\t wins\t -\t Rs. 2. 
    “rolls” three same symbols    \t -\t wins\t -\t Rs. 10. 
    “rolls” three BELLS           \t -\t wins\t -\t Rs. 50. 
    “rolls” two SKULLS            \t -\t loses\t -\t Rs. 1. 
    “rolls” three SKULLS          \t -\t loses\t -\t all of the money. 
    ''')
            a = 10
        else:
            a = 10
        g = input("Press Any Key When You Are Ready!::\n")
        b = ["Mango", "Cherry", "Apple", "Banana", "Grapes", "Bell", "Skull"]

        def symbol():
            global first, second, third
            first = random.choice(b)
            second = random.choice(b)
            third = random.choice(b)
            print(first, second, third)

        def chekpoints():
            global credit
            credit = credit - 2
            if (first == second) or (second == third) or (third == first):
                if (first == "Skull" and second == "Skull") or (
                        second == "Skull "
                        and third == "skull") or (first == "Skull"
                                                  and third == "Skull"):
                    credit += -1
                elif first == second == third:
                    if first == "Skull":
                        credit = 0
                elif first == "Bells":
                    credit = credit + 50
                else:
                    credit = credit + 10
            else:
                credit = credit + 2

        def quit():
            global credit
            while credit != 0:
                print('Youn Have Rs.', credit)
                answer = input('Do You Want To  Quit? press Q To Quit::\n')
                answer = answer.lower()
                if answer == "q":
                    print("You Are Leaving The Game With Rs.", credit)
                    print("Bye Bye ")
                    return False
                else:
                    return True

                if first != second != third:
                    credit = credit - 2
                if credit == 0:
                    answer = q

        def main():
            global credi, first, second, third
            ask = quit()
            while credit != 0 and ask == True:
                symbol()
                chekpoints()
                ask = quit()

        main()
    elif game == '3':
        import turtle
        import os

        score_a = 0
        score_b = 0

        canvas = turtle.Screen()
        canvas.title("Pingi Pongi")
        canvas.bgcolor("black")
        canvas.setup(width=800, height=600)
        #0,0 is the centre

        #PaddleA
        pa = turtle.Turtle()
        pa.goto(-350, 0)  #initial position of paddle
        pa.speed(9)
        pa.shape("square")
        pa.color("white")
        pa.shapesize(stretch_wid=5, stretch_len=1)
        pa.penup()

        #PaddleB
        pb = turtle.Turtle()
        pb.goto(350, 0)  #initial position of paddle
        pb.speed(9)
        pb.shape("square")
        pb.color("white")
        pb.shapesize(stretch_wid=5, stretch_len=1)
        pb.penup()

        #Ball
        ball = turtle.Turtle()
        ball.speed(9)
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball.dx = 1
        ball.dy = 1

        #Scores
        score = turtle.Turtle()
        score.penup()
        score.speed(9)
        score.color("white")
        score.hideturtle()
        score.goto(0, -270)
        score.pen()
        score.write("Player A: 0  Player B: 0",
                    align="center",
                    font=("Courier", 24, "normal"))

        def pa_mov_up():
            y = pa.ycor()
            y = y + 20
            pa.sety(y)

        def pa_mov_down():
            y = pa.ycor()
            y = y - 20
            pa.sety(y)

        def pb_mov_up():
            y = pb.ycor()
            y = y + 20
            pb.sety(y)

        def pb_mov_down():
            y = pb.ycor()
            y = y - 20
            pb.sety(y)

        canvas.listen()
        canvas.onkeypress(pa_mov_up, "Up")
        canvas.onkeypress(pa_mov_down, "Down")
        canvas.onkeypress(pb_mov_up, "2")
        canvas.onkeypress(pb_mov_down, "8")

        while True:
            canvas.update()  #updates screen everytime the loop runs

            #Move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            #Edges
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1  # reverse the direction
                #os.system("afplay bounce(1).wav&")
            elif ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1  # reverse the direction
                #os.system("afplay bounce(1).wav&")

            if ball.xcor() > 390:
                ball.goto(0, 0)
                score_a += 1
                score.clear()
                score.write("Player A: {}  Player B: {}".format(
                    score_a, score_b),
                            align="center",
                            font=("Courier", 24, "normal"))
                ball.dx *= -1
            elif ball.xcor() < -390:
                ball.goto(0, 0)
                score_b += 1
                score.clear()
                score.write("Player A: {}  Player B: {}".format(
                    score_a, score_b),
                            align="center",
                            font=("Courier", 24, "normal"))
                ball.dx *= -1

            #Bouncing on paddles
            if ball.xcor() > 340 and ball.ycor(
            ) < pb.ycor() + 50 and ball.ycor() > pb.ycor() - 50:
                ball.setx(340)
                ball.dx *= -1
                #os.system("afplay bounce(1).wav&")

            elif ball.xcor() < -340 and ball.ycor(
            ) < pa.ycor() + 50 and ball.ycor() > pa.ycor() - 50:
                ball.setx(-340)
                ball.dx *= -1
                #os.system("afplay bounce(1).wav&")

        turtle.done()

else:
    print("Sorry, I can't do that")
