import sys
import random
import string
import re

def scramble_word(word):
    """This function takes in a word and returns a new word with randomly replaced characters if the word contains only lowercase letters"""
    if word.islower():  
        return ''.join(random.choice(string.ascii_lowercase) for _ in word)
    else:
        return word

def scramble_input(f):
    """This function takes a stream, breaks it into words, and applies the scramble_word function to each word"""
    for line in f:
        leading_whitespace = ''
        trailing_whitepace = ''
        t = re.search(r'^\s*', line)
        if t:
            leading_whitespace = t.group(0)
        t = re.search(r'\s*$', line)
        if t:
            trailing_whitepace = t.group(0)
        words = line.split()
        scrambled_words = [scramble_word(word) for word in words]
        result = leading_whitespace + ' '.join(scrambled_words) + trailing_whitepace
        print(result)


def main():
    scramble_input(sys.stdin)


if __name__ == "__main__":
    main()

