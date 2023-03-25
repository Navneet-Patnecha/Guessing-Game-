import random
name = input("Enter your Name : ")
print(f"Welcome {name} to this number guessing game")
play = "yes"
number = random.randint(1,101)
chances =10
def playagain():
    global play
    play = input("do you want to playagain : ")
    if play == "yes":
        global chances,number
        chances =10
        number = random.randint(1,101)

while play=="yes":
    
    while chances>0:
        guess=int(input("guess a number between 1 and 100 : "))
        if guess == number:
            print("!!!! YOU WON !!!!")
            playagain()
            break
        
        
        elif guess < number:
            print("your guess is less than the actual answer!!")
            chances -=1
            print(f"you are left with {chances} chances")
        
        
        else:
            print("your guess is more than actual number")
            chances -=1
            print(f"you are left with {chances} chances")
        
        
        if chances == 0:
            print("!!!! YOU LOSE !!!!")
            print("Actual answer is {number} ")
            playagain()
            break

print("THANKS FOR PLAYING")
        
    
    