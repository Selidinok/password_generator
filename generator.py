import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

class PasswordGenerator():
    def __init__(self):
        self.english_words = self.load_words()
        self.use_valid_words = False
        self.use_numbers = False
        self.use_symbols = False
        self.use_uppercase = False
    
    def set_use_numbers(self, use):
        self.use_numbers = use

    def set_use_symbols(self, use):
        self.use_symbols = use

    def set_use_uppercase(self, use):
        self.use_uppercase = use
    
    def set_use_valid_words(self, use):
        self.use_valid_words = use

    def generate(self):
        if self.use_valid_words:
            word = self.generate_valid_word()
        else:
            word = self.generate_random_word()
        return word

    def generate_valid_word(self):
        word = random.sample(self.english_words, 1)
        numbers = []
        symb = []
        if self.use_uppercase:
            word[0] = word[0].capitalize()
        if self.use_numbers:
            numbers = random.sample(num, 2)
        if self.use_symbols:
            symb = random.sample(symbols, 2)

        combine = word + numbers + symb
        random.shuffle(combine)
        print(combine)
        
        return ''.join(combine)

    def generate_random_word(self):
        low = random.sample(lower, 8)
        up = []
        numbers = []
        symb = []
        if self.use_uppercase:
            up = random.sample(upper, 2)
            print(up)
        if self.use_numbers:
            numbers = random.sample(num, 2)
        if self.use_symbols:
            symb = random.sample(symbols, 2)
        
        combine = low + up + numbers + symb
        random.shuffle(combine)
        print(combine)

        return ''.join(combine)

        

    def load_words(self):
        with open('words_alpha.txt') as word_file:
            valid_words = set(word_file.read().split())

        return valid_words