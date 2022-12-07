from pathlib import Path

lines = Path('input.txt').read_text().split('\n')[:-1]

class A:
    meaning = 'rock'
    win_value = 1
    beats = 'scissors'
    

class B:
    meaning = 'paper'
    win_value = 2
    beats = 'rock'

class C:
    meaning = 'scissors'
    win_value = 3
    beats = 'paper'

outcomes = {
    'win': 6,
    'draw': 3,
    'lose': 0,
    }

items = {
    'A': A,
    'X': A,
    'B': B,
    'Y': B,
    'C': C,
    'Z': C,
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
    me = items[me]()
    them = items[them]()
    score = me.win_value + outcomes[compare(me,them)]
    total += score
print(f'total is {total}')





    
