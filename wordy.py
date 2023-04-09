# A few variables
guess = ""
feedback = ""
guess_list = []
allowed_characters = "g,y,w"
invalid = "Invalid information. Type it in again: "


# opens list of words
try:
    with open('my_project/words.txt') as f:
        for line in f:
            guess_list.append(line.strip())
except FileNotFoundError:
    print("file not found")


print("Ready to solve today's wordle? Start with the word 'slate'")
for guesses in range(6):
    while True:
        guess = input("type in entered word: ").lower()
        if len(guess) != 5:
            print(invalid)
            continue
        else:
            guess = guess
            break

    while True:
        information = input(
            "Type in the information about the word (g), (y), (w): ").lower()
        if len(information) != 5 or not all(char in allowed_characters for char in information):
            print(invalid)
        else:
            break

    if information == "ggggg" and guesses == 0:
        print("WOW!!! you got today's worlde in only one guess!!!!")
        exit
    elif information == "ggggg":
        print("Congrats! You got today's worlde in", guesses+1, "guesses")
        break

    temp_tuple = tuple(guess_list)
    # You can't iterate over a list you want to change, so using a tuple.
    for word in temp_tuple:
        for i in range(5):
            if information[i] == "w" and guess[i] in word:
                guess_list.remove(word)
                break
            elif information[i] == "g" and guess[i] != word[i]:
                guess_list.remove(word)
                break
            elif information[i] == "y" and guess[i] not in word:
                guess_list.remove(word)
                break
            elif information[i] == "y" and guess[i] == word[i]:
                guess_list.remove(word)
                break

    counter = 0
    for word in guess_list:
        print(word, end=", ")
        counter += 1
        if counter == 8:
            print("")
            counter = 0
