import random
words=['saravana','rihan','suhail','aslam','fashil']
word=random.choice(words)
guessed=['_']*len(word)
attempts=5o
guessed_letters=[]
while attempts>0 and '_' in guessed:
    print("\n wrord:",''.join(guessed))
    print("Attempts Left:",attempts)
    guess=input("Guess a letter:").lower()
    if not guess.isalpha() or len(guess)!=1:
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("you already guessed the letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessed[i]=guess
        print("CORRECT!!")
    else:
        attempts-=1
        print("!WRONG!")
if '_' not in guessed:
    print("\n Conguratulation! You guessed the word:",word)
else:
    print("\n Game Over!the word was:",word)
