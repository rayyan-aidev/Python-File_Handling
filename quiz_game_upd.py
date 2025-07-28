score = 0
total_score = 5
guess = ""


def take_ans(question, ans):
    global score
    global correct_ans
    guess = input(question)
    correct_ans = ans
    score = ans_check(guess, score)


def ans_check(guess, score):
    if guess.lower().replace(" ", "") == correct_ans:
        print("Correct answer")
        score += 1
    else:
        print("Uh oh! Answer is wrong")
    return score


Q1 = "What is the tallest builing in the world? "
Q2 = "What is the largest country in the world? "
Q3 = "Who was the leader of USSR during WW2(full name)? "
Q4 = "What is the answer of 14+4(8/2)? "
Q5 = "What is the square root of 144? "
while True:
    print("Welcome! You have enetered the ultimate quiz. Get ready for some amazing trivia!")
    take_ans(Q1, "burjkhalifa")
    take_ans(Q2, "russia")
    take_ans(Q3, "josephstalin")
    take_ans(Q4, str(30))
    take_ans(Q5, str(12))
    try:
        with open("Beginner useful/highscore.txt", "r") as f:
            highscore = f.read()
        if highscore == "":
            with open("Beginner useful/highscore.txt", "w") as f:
                f.write(str(score))
            print(f"New highscore! {score}")
            break
        else:
            highscore = int(highscore)
            if score > highscore:
                print(f"New High score! {score}")
                with open("Beginner useful/highscore.txt", "w") as f:
                    f.write(str(score))
            else:
                print(f"Score: {score} out of {total_score}")
                print("Try to beat your high score next time.")
            break
    except FileNotFoundError:
        print("File not found")
        with open("Beginner useful/highscore.txt", "w") as f:
            f.write(str(score))
        print(f"New highscore! {score}")
        print("New file created")
        break
