from pathlib import Path
elves = [sum([int(y) for y in x.split('\n')]) for x in Path('input.txt').read_text()[:-1].split('\n\n')]
print(f"max is: {max(elves)}, top three are: {sum(sorted(elves, reverse=True)[:3])}")
