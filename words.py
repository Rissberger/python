words = ['apple', 'grape', 'nut', 'blue', 'elsa']

def print_upper_words(words):
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    for word in words:
        if word.startswith("e") or word.startswith('E'):
            print(word.upper())

def print_upper_word3(words, start_with):
    for letter in start_with:
        if word.startswith(letter):
            print(word.upper())
            