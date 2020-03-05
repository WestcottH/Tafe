 

#I'm thinking of a number 
print('Guess the Number Game')

#Generate random number 
import random
num = random.randint (1, 100)

guessesTaken = 0

#Tell user to guess a number, anywhere between 1 – 100 
guess = int(input("enter a number between 1 and 100: "))
while guess != num:
    guessesTaken = guessesTaken + 1

    #Compare input to random number 


    # if not, print too high or too low 
    if guess < num:
        print('Your guess is too low.')
        guess = int(input("enter a number between 1 and 100: "))
     
    if guess > num:
        print('Your guess is too high.')
        guess = int(input("enter a number between 1 and 100: "))  

    #if correct, print congratulations 

    if guess == num:
        print('Congratulations')
 



 

#Hangman 

#Generate Random word 

#tell the user number of letters 

#ask the user for his guess 

# check to see if the letter is in the word 

#if exist show the letter on the word 

#if not draw part of the hangman 

#check if the word is complete --> user wins 

# 

# if the hangman complete --> user loses 