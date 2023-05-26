import sys
import random
import string
import re

def should_scramble_word(word: str, num_in_line: int) -> bool:
    """
    Return true if a word contains no uppercase characters or instances of '://'
    """
    if word.islower():
        return True
    elif word.find("://") > -1:
        return True
    return False

def scramble_word(word: str, num_in_line: int) -> str:
    """
    Replace the letters in a word with random characters as per `should_scramble_word()`
    """
    if should_scramble_word(word, num_in_line):
        return ''.join(c if not c.isalpha() else random.choice(string.ascii_lowercase) for c in word)
    else:
        return word

def scramble_input(f):
    """
    Apply `scramble_word` to each word in a stream, while preserving whitespace and vim modelines
    """
    for line_num, line in enumerate(f):
        if len(line.strip()) == 0:
            print()
            continue
        if line_num < 10 and line.lstrip("#/").lstrip().startswith("vim: set "):
            print(line, end="")
            continue
        leading_whitespace = ''
        trailing_whitespace = ''
        t = re.search(r'^\s*', line)
        if t:
            leading_whitespace = t.group(0)
        t = re.search(r'\s*\\n$', line)
        if t:
            trailing_whitespace = t.group(0)
        line = line.strip()
        line = line.replace("\t", "\t ")
        words = line.split(' ')
        scrambled_words = [ scramble_word(word, i) for i, word in enumerate(words) ]
        result = leading_whitespace + ' '.join(scrambled_words) + trailing_whitespace
        print(result.rstrip("\n"))


def main():
    scramble_input(sys.stdin)


if __name__ == "__main__":
    main()

