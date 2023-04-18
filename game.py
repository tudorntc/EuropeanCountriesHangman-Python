import random

# List of European countries
countries = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Vatican City']

def play_hangman():
    # Select a random country from the list
    word = random.choice(countries)
    # Convert the word to lowercase
    word = word.lower()
    # Create a set of unique letters in the word
    letters = set(word)
    # Initialize the number of incorrect guesses
    wrong_guesses = 0
    # Initialize the set of correct guesses
    correct_guesses = set()
    
    # Loop until the player guesses the word or runs out of guesses
    while len(letters) > 0 and wrong_guesses < 6:
        # Display the current state of the word
        print('Word:', end=' ')
        for letter in word:
            if letter in correct_guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()
        
        # Display the letters the player has already guessed
        print('Guesses:', ', '.join(sorted(correct_guesses)))
        
        # Prompt the player for a guess
        guess = input('Guess a letter: ').lower()
        
        # Check if the guess is valid (a single letter)
        if len(guess) != 1:
            print('Please enter a single letter.')
            continue
        
        # Check if the guess is a new letter
        if guess in correct_guesses or guess in letters:
            print('You already guessed that letter.')
            continue
        
        # Check if the guess is in the word
        if guess in letters:
            letters.remove(guess)
            correct_guesses.add(guess)
            print('Correct!')
        else:
            wrong_guesses += 1
            print('Incorrect...')
    
    # Display the result of the game
    if wrong_guesses < 6:
        print('Congratulations, you guessed the word:', word.capitalize())
    else:
        print('Sorry, you ran out of guesses. The word was:', word.capitalize())

# Play the game
play_hangman()
