import random
name = input("User pls enter you name to play the game = ")
print()
# Here the user is asked to enter the name first
print("Good Luck ! ", name)
students = ['ajay', 'satvika', 'mohan', 'pradeep', 'althaf']
students = random.choice(students).lower()  # this select a random object from students [] list 
guessed_correctly = []
guessed_incorrectly = []
choice = 6  # count of choice is decrased if user guesses in corct choice only 
while (choice != 0):
    ans = ''
    for char in students:
        if char in guessed_correctly:
            ans += char
        else:
            ans += ' _ '
    if ans == students: # char guessed should match chars in word 
        break
    print("Guess the word: ",ans)
    print("You have ",choice," chances left")
    guess = input().lower()
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("Already guessed", guess)
    elif guess in students:
        print("Good Job! You guessed the correct letter!")
        guessed_correctly.append(guess)
    else:
        print("Sorry! You have guessed a wrong letter!")
        #hangman_count = hangman_count + 1
        choice=choice-1
        guessed_incorrectly.append(guess)
       # print(hangman1[hangman_count])
if choice>0:
    print("Congaratulations You guessed it right and you win !")
else:
    print("Sorry you guessed the wrong letter. Try again.")