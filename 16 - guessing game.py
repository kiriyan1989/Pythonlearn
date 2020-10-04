secret_word = "hello"
guess = ""      # empty string variable
i = 0


while guess != secret_word and i < 3:
    guess = input ("Enter a guess: ")
    i = i + 1

if guess == secret_word:
    print ("you got it, the word is " + guess + " You got at attempt " + str(i))
else:
     print ("you did not get it, out of guesses")