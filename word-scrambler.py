import sys
import random
import string

def scramble_word(word):
    """
    This function takes in a word and returns a new word 
    with randomly replaced characters if the word contains only lowercase letters.
    """
    if word.islower():  # check if the word contains only lowercase letters
        return ''.join(random.choice(string.ascii_lowercase) for _ in word)
    else:
        return word

def main():
    """
    This function takes in standard input, 
    breaks it into words, 
    and applies the scramble_word function to each word.
    """
    for line in sys.stdin:
        words = line.split()
        scrambled_words = [scramble_word(word) for word in words]
        print(' '.join(scrambled_words))

if __name__ == "__main__":
    main()

