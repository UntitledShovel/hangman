# https://random-word-api.herokuapp.com/all
# Import dependencies
import random, requests, json

# Get a random word
response = json.loads(requests.get('https://random-word-api.herokuapp.com/all').text)
word = random.choice(response)

# print "Welcome to Hangman" in big text
print("░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░")
print("░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗")
print("░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║")
print("░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║")
print("░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝")
print(" ")
print("██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗")
print("██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║")
print("███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║")
print("██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║")
print("██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║")
print("╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝")

guessesLeft = 6

def main():
    running = True
    display = []
    guessedLetters = []
    global word, guessesLeft
    for x in range(len(word)):
        display.append("_")
    while running:
        if guessesLeft < 1 or guessedLetters == 0:
            print(f"You ran out of guesses, the word was {word}")
            running = False
            break
        
        print("===========================================================================================")
        for f in range(len(display)):
            print(display[f], end="")
        print(" ")
        x = input(f"Guess a letter, you have {guessesLeft} guesses left.\nIf you feel like you know the word, type in 'I know the word' to see if your word is correct.\n> ").lower()
        
        if len(x) > 1 and not x == "i know the word":
            print("Invalid response")
            continue
        
        if x == "i know the word":
            y = input("What do you think the word is?\n> ").lower()
            if y.lower() == word:
                running = False
                break
            else:
                print("That is not the word...")
                guessesLeft -= 1
                continue
        
        if x in word and x not in guessedLetters:
            for z in range(len(word)):
                if word[z] == x:
                    display[z] = x
            guessedLetters.append(x)
            continue
        elif not x in word:
            guessedLetters.append(x)
            guessesLeft -= 1
            print("That is not in the word")
            continue

if __name__ == '__main__':
    main()