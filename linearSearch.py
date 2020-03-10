def linearsearch():
    phrase = input("Insert text: ")
    letter = input("Insert character to be counted: ")
    number_of_letters = phrase.count(letter)
    print(f"Number of occurencer of {letter} : {number_of_letters}")
