from rich.console import Console #type:ignore
console = Console()
import requests #type:ignore

WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE[/]\n'
GUESSES = 6
PLAYER_INSTRUCTIONS = f'You may start guessing, the word is 5 letters long. You have {GUESSES} chances to guess the word. Good luck!'

def correct_place(letter):
    return f'[black on green]{letter}[/]'

def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'

def incorrect_letter(letter):
    return f'[black on red]{letter}[/]'

chosen_word = ''
player_guess = ''

while chosen_word == '':
    chosen_word = requests.get('https://random-word-api.herokuapp.com/word?length=5')
    if chosen_word.status_code == 200:
        chosen_word = chosen_word.json()[0]
    else: continue

if __name__ == '__main__':
    console.print(WELCOME_MESSAGE)
    console.print(PLAYER_INSTRUCTIONS)
    while GUESSES > 0:
        
