import random 

#ask the user for a positive integer "n" and "n" should be positive, otherwise prompt again 
while True:
    try:
        n = int(input("Level: "))
        if n > 0: 
            break
    except ValueError:
        pass

#create a list from 1 to n
list = []
for i in range(n):
    list.append(i+1)

#generate an integer between 1 and n
random_num = random.choice(list)

#asks the user for their guess as a positive integer, and guess should be positive
#otherwise prompt again if negative or input is invalid
#if guess is smaller than the random_num = Too small!
#if guess is larger than that random_num = Too large!
#prompt again the guessing until you reach the right answer
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_num:
                print("Too small!")
            elif guess > random_num:
                print("Too large!")
            elif guess == random_num:
                print("Just right!")
                break
    except ValueError:
        pass

