from pathlib import Path

lines = Path('input.txt').read_text().split('\n')[:-1]

def process_list(mylist:str) -> list:
    mylist = mylist.split('-')
    return [x for x in range(int(mylist[0]), int(mylist[1])+1)]

def find_subset(list1:list,list2:list) -> bool:
    return set(list1).issubset(set(list2)) or set(list2).issubset(set(list1))

def find_overlap(list1:list,list2:list) -> bool:
    return set(list1) & set(list2)

total = 0
overlap_total = 0

for line in lines:
    str1,str2 = line.split(',')
    list1 = process_list(str1)
    list2 = process_list(str2)
    if find_subset(list1,list2):
        total += 1
    if find_overlap(list1,list2):
        overlap_total += 1
    

print(f'total is {total}, overlap_total is {overlap_total}')
    
