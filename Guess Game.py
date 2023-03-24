Player_name = input("Enter Your Name:  ")
print(f"Welcome!!{Player_name} to guessing word game")
word = "internship"
guesses = " "
chances = 10

while chances >0:
    for ch in word:
        won = True
        if ch in guesses:
            print(ch,end=" ")
        else:
            print("_",end=" ")
            won = False


    if won:
        print("You Won!!!")
        print(f"{Player_name} , your score is {chances*10}")
        break



    #take input from user
    guess = input("\n guess a character!!")
    guesses +=guess

    if guess not in word:
        chances -=1
        print("you guessed wrong character")
        print(f"you are left with {chances} chances")

        if chances == 0:
            print("Haar gaya bhai m toh")
            break