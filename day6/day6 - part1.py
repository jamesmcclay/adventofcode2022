from pathlib import Path

message = Path('input.txt').read_text().strip()
bstart = 0
bend = 4
mstart = 0
mend = 14
p1done = False
p2done = False
for count,char in enumerate(message):
    buffer = message[bstart:bend]
    mbuffer = message[mstart:mend]
    marker = set(buffer)
    mmarker = set(mbuffer)
    if len(marker) == 4 and not p1done:
        n1 = bend
        p1done = True
    if len(mmarker) == 14 and not p2done:
        n2 = mend
        p2done = True
    bstart +=1
    bend +=1
    mstart += 1
    mend += 1
    if p1done and p2done:
        break

print(f"Packet Marker at {n1}, message marker at {n2}")
