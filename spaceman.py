import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    open the file words.txt in read mode and stor its content in f
    get a list, each line is an element, from the contents of f and store it in words_list
    close the file f

    grab the first element (line) of words_list, make a list of words that are separeted by spaces and store it in words_list
    randomnly choose a word from words_list and store it in secret_word.
    return secret_word
    
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    function that checks if all letters from secret_word are in letters_guessed. iterates over the string
    secret_word comparing each of its letters to the letters in the list of letters in the variable 
    letters_guessed. When there is a match then the function is going to continue iterating until all letters
    match, and in this case it will return a bool true. if there is a letter missing in the iteration/match 
    then the function is going to return false.
    '''
    # for each letter in the string secret_word
    for letter in secret_word:
    # if a letter is not in the list letters_guessed
        if(letter not in letters_guessed):
    #     return false if any letter is not guessed
            return False
    # return true if all letters are guessed
    return True
    '''
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    # pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    '''
    # Set letters_so_far to an empty string
    letters_so_far = ""
    # for each letter in secret_word
    for letter in secret_word:
    #     if a letter is in letters_guessed 
        if(letter in letters_guessed):
    #         add the letter to letters_so_far
            letters_so_far += letter 
    #     otherwise
        else:
    #         add an underscore to letters_se_far
            letters_so_far += "_" 
    # returns letters_so_far
    return letters_so_far
    '''    
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    # pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    '''
    # if the letter from guess is in secret_word
    if (guess in secret_word):
    #     return true
        return True
    # otherwise
    else:
    #     return false
        return False
    '''
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

    # pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    print all the introduction to game stating the length of the word and how many incorrect guesses the player has
    set num_guesses to 0
    set won to the bool False
    run this code while num_guesses is less than 7 and won is equal to the bool False.
        set letter equal to the string "aa" so it enters into the while code block
        run this code while the length of letter is different to 1 or letter is not a letter (not a number or anything else than a letter)
            set letter equal to the user input after "Enter a letter: " is prompted

        call the function is_guess_in_word with the letter the user inputed and secret_word as arguments
        if letter_guess is equal to the boll True
            print Your guess appears in the word!
        otherwise
            print Sorry your guess was not in the word, try again
            reduce num_gueses by 1
        
        show to the user word with underscores for the letters he/she has not guessed and letters in the word for the ones he/she has guessed so far.
        call the function is_word_guessed and store either True of False as a bool in the won var

    if won is equal to bool True
        show to the user You won!
    otherwise
        show to the user Sorry you didn't win, try again!
        show to the user what was the secret word

        
    Args:
      secret_word (string): the secret word to guess.

    '''

    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!")
    print(f"the secret word contains {len(secret_word)} letters")
    print(f"You have 7 incorrect guesses, please enter one letter per round")
    print("________________________")
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    num_guesses = 0
    won = False
    letters_guessed = []
    unselected_letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    play_again = True
    spaceman_art_count = 0
    while(play_again == True):
        while(num_guesses < 7 and not won):
            # letter = "aa"
            # while(len(letter) != 1 or not letter.isalpha()):
            #     letter = input("Enter a letter: ").lower()
            #     if (letter in letters_guessed):
            #         print("You've already guessed that letter!")
            #         continue
            #     if (len(letter) > 1):
            #         print("You should select only one letter(character)!")
            #         continue
            #     letters_guessed.append(letter)
            letter = input("Enter a letter: ").lower()
    
            if (len(letter) != 1 or not letter.isalpha()):
                print("Invalid input! Please enter a single letter.")
                continue
            
            if (letter in letters_guessed):
                print("You've already guessed that letter!")
                print("---------------------------")
                # Skips the guess penalty if the letter is repeated
                continue  

            letters_guessed.append(letter)

            #TODO: Check if the guessed letter is in the secret or not and give the player feedback
            letter_guess = is_guess_in_word(letter, secret_word)
            if(letter_guess):
                print("Your guess appears on the word!")
            else:
                print("Sorry your guess was not in the word, try again")
                num_guesses += 1
                print(f"You have {7 - num_guesses} incorrect guesses left")
                if(spaceman_art_count == 0):
                    print("   O  ")
                    spaceman_art_count += 1
                elif (spaceman_art_count == 1):
                    print("   O  ")
                    print("  /| ")
                    spaceman_art_count += 1
                elif (spaceman_art_count == 2):
                    print("   O ") 
                    print("  /|\\")
                    spaceman_art_count += 1
                elif (spaceman_art_count == 3):
                    print("   O ") 
                    print("  /|\\")
                    print("   |  ")
                    spaceman_art_count += 1
                elif (spaceman_art_count == 4):
                    print("   O ") 
                    print("  /|\\")
                    print("   |  ")
                    print("  /   ")
                    spaceman_art_count += 1
                elif (spaceman_art_count == 5):
                    print("   O ") 
                    print("  /|\\")
                    print("   |  ")
                    print("  / \    ")
                    spaceman_art_count += 1
                elif (spaceman_art_count == 6):
                    print("  .---." )
                    print("  | O |" )
                    print(" /| | |\\")
                    print("  | | |  ")
                    print("  / \\ \\")
                    print(" /   \\ \\")
            #TODO: show the guessed word so far
            print("Guessed word so far: ", get_guessed_word(secret_word, letters_guessed))
            for unselected_letter in unselected_letters:
                if(letter == unselected_letter):
                    unselected_letters.remove(letter)
            print("These letters haven't been guessed yet: ", end="")
            for letter in unselected_letters:
                print(letter, end="")
            #TODO: check if the game has been won or lost
            print("\n---------------------------")
            won = is_word_guessed(secret_word, letters_guessed)

        if (won):
            print("You won!")
        else:
            print("Sorry you didn't win, try again!")
            print(f"the word was: {secret_word}")
        
        response_play_again = (input("Do you want to play again (y/n): ")).lower()
        if (response_play_again == 'y'):
            play_again = True
            num_guesses = 0
            letters_guessed = []
            won = False
            unselected_letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            secret_word = load_word()
            print("\nWelcome to Spaceman!")
            print(f"the secret word contains {len(secret_word)} letters")
            print(f"You have 7 incorrect guesses, please enter one letter per round")
            print("________________________")       
        elif(response_play_again == 'n'):
            play_again = False

# call function load_word to get a random word and put it in secret_word
# call the function speceman with the word as an argument.

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)

