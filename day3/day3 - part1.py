from pathlib import Path
from string import ascii_lowercase as alpha

sacks = Path('input.txt').read_text().split('\n')[:-1]
priorities = dict([(x,count+1) for count,x in enumerate(alpha)] + [(x.upper(),count+27) for count,x in enumerate(alpha)])

total = 0
for sack in sacks:
    total += priorities[(set(sack[:int(len(sack)/2)]) & set(sack[int(len(sack)/2):])).pop()]

sacks_by_3 = [sacks[i:i + 3] for i in range(0, len(sacks), 3)]
badge_total = 0
for sacklist in sacks_by_3:
    badge_total += priorities[(set(sacklist[0]) & set(sacklist[1]) & set(sacklist[2])).pop()]

print(f'total is {total}')
print(f'badge total is {badge_total}')
