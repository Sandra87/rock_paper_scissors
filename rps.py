import random

def input_human_play(input=input):
    play = input('rock, paper or scissors? ')
    while not is_valid_play(play):
        play = input('rock, paper or scissors? ')
        return play

def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']

def generate_computer_play():
    return random.choice(['rock', 'paper', 'scissors'])

def evaluate_game(human, computer):
    if human == 'rock':
        if computer == 'rock':
            return 'tie'
        elif computer == 'scissors':
            return 'human'
        elif computer == 'paper':
            return 'computer'
    elif human == 'scissors':
        if computer == 'rock':
            return 'computer'
        elif computer == 'scissors':
            return 'tie'
        elif computer == 'paper':
            return 'human'
    elif human == 'paper':
        if computer == 'rock':
            return 'human'
        elif computer == 'scissors':
            return 'computer'
        elif computer == 'paper':
            return 'tie'
    else:
        print('Say it again, please.')

def main(input=input):
    human = input_human_play(input)
    computer=generate_computer_play()
    print(computer)


    game = evaluate_game(human, computer)
    if game == 'tie':
        print('it is a tie')
    else:
        print(f'{game} won')

if __name__ == '__main__':
    main()
