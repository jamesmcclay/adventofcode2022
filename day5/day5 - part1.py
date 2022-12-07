from pathlib import Path

lines = Path('input.txt').read_text().split('\n')[:-1]

crates = [[] for x in range(0,9)]

def crate_line(line):
    spaces = 0
    mylist = []
    for char in line:
        if spaces == 4:
            mylist.append('*')
            spaces = 0
            continue           
        if char is '[' or char is ']' or char is ' ':
            spaces += 1
        else:
            mylist.append(char)
            spaces = 0
    return mylist

count = 7
while count >= 0:
    line_list = crate_line(lines[count])
    for scount, crate in enumerate(line_list):
        if crate == '*':
            continue
        crates[scount].append(crate)     
    count -=1
   
for line in lines[10:]:
    linespl = line.split()
    num1,num2,num3 = int(linespl[1]),int(linespl[3])-1,int(linespl[5])-1
    for item in range(0,num1):
        crates[num3].append(crates[num2].pop())

message = ''
for x in crates: message += x.pop()
print(f'{message}')
        
    
