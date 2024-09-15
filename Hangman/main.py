import random
from os import system

class Hangman:

    HANGMAN_STAGES = {
                0:r'''
            ___
        ''',
                1:r'''
            |
            |
            |
            |
            ___
        ''',
                2:r'''
            _______
            |
            |
            |
            |
            ___
        ''',
                3:r'''
            _______
            |      |
            |      
            |
            |
            ___
        ''',
                4:r'''
            _______
            |      |
            |      0
            |
            |
            ___
        ''',
                5:r'''
            _______
            |      |
            |      0
            |      |
            |
            ___
        ''',
                6:r'''
            _______
            |      |
            |      0
            |     /|
            |
            ___
        ''',
                7:r'''
            _______
            |      |
            |      0
            |     /|\
            |
            ___
        ''',
                8:r'''
            _______
            |      |
            |      0
            |     /|\
            |     /
            ___
        ''',
                9:r'''
            _______
            |      |
            |      0
            |     /|\
            |     / \
            ___
        ''',


    }

    def __init__(self, word: str):
        self._word: str = word.lower()
        self.place: list = [char if char == ' ' else '_' for char in self.word]
        self.mistakes: int = 0

    @property
    def word(self):
        """The word property."""
        return self._word

    def guess_a_latter(self, letter: str):
        letter = letter.lower()
        if letter in self.word:
            list_of_index = Hangman._find_nums(self.word, letter)
            for i in list_of_index:
                self.place[i] = letter
        else:
            self.mistakes += 1

    def print_hangman(self):
        return Hangman.HANGMAN_STAGES[self.mistakes] if self.mistakes >=0 and self.mistakes <= 9 else False


    def show_place(self):
        return ''.join(_ for _ in self.place)

    @staticmethod
    def _find_nums(word: str, letter: str):
        return [i for i, x in enumerate(word) if letter == x]

    @staticmethod
    def one_char_input(char: str): 
        if len(char) > 1:
            raise ValueError(f'Only one char!')
        else:
            return char


#sample words
words = [
    'gra', 'kameleon', 'zenit', 'ironia', 'pianino',
    'mapa', 'komputer', 'obraz', 'człowiek',
    'drzewo', 'kwiat', 'ocean', 'góra', 'rzeka', 'słońce', 'księżyc', 'las', 'zwierzę', 'ptak',
    'telefon', 'tablet', 'internet', 'aplikacja', 'robot', 'programista', 
    'kod', 'sztuczna inteligencja', 'drukarka 3D', 'satelita',
    'książka', 'film', 'muzyka', 'teatr', 'rzeźba', 'taniec', 'poeta', 'malarz', 'architekt', 'historia',
    'dom', 'praca', 'rodzina', 'przyjaciel', 'miłość', 'szczęście', 'smutek', 'nadzieja', 'marzenie', 'podróż',
    'czas', 'przestrzeń', 'myślenie', 'uczucie', 'świadomość', 'prawda', 'piękno', 'dobro', 'zło', 'wolność',
    'piłka nożna', 'koszykówka', 'tenis', 'siatkówka', 'pływanie',
    'fizyka', 'chemia', 'biologia', 'matematyka', 'astronomia',
    'zupa', 'obiad', 'deser', 'przyprawa', 'przepis'
]

h = Hangman(random.choice(words))

while True:
    if h.mistakes < 9:
        system('cls')
        current_place = h.show_place()

        if not '_' in current_place:
            system('cls')
            print(f'password: {current_place}')
            print("You Win!!!!")
            break
        print(f'password: {current_place}')
        print(f'\nhangman lvl: {h.print_hangman()}')
        try:
            letter = Hangman.one_char_input(input('Write letter: '))
            h.guess_a_latter(letter)
        except ValueError as e:
            print(e)
    
    else:
        system('cls')
        print(f'\nhangman lvl: {h.print_hangman()}')
        print(f'password is: {h.word}')
        print("You lose!")
        break