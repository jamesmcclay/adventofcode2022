from pathlib import Path

lines = Path('input.txt').read_text().split('\n')[:-1]

class A:
    meaning = 'rock'
    win_value = 1
    beats = 'scissors'
    outcomes = {'lose': 'scissors','draw': 'rock','win': 'paper'} 

class B:
    meaning = 'paper'
    win_value = 2
    beats = 'rock'
    outcomes = {'lose': 'rock','draw': 'paper','win': 'scissors'}

class C:
    meaning = 'scissors'
    win_value = 3
    beats = 'paper'
    outcomes = {'lose': 'paper','draw': 'scissors','win': 'rock'}

outcomes = {
    'win': 6,
    'draw': 3,
    'lose': 0,
    }

items = {
    'A': A,
    'B': B,
    'C': C,
    'rock': A,
    'paper': B,
    'scissors': C,
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
    }

def compare(me, them):
    if me.meaning == them.meaning:
        return 'draw'
    elif me.beats == them.meaning:
        return 'win'
    else:
        return 'lose'
    
total = 0
for line in lines:
    them, me = line.split()
    them = items[them]()
    me = items[me] #win or lose
    me = them.outcomes[me] #rock paper scissors
    me = items[me] #my object
    score = me.win_value + outcomes[compare(me,them)]
    total += score
print(f'total is {total}')





    
