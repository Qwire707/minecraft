# напиши код для виконання завдань тут
count = 0
with open('my_file.txt', 'r') as file:
    for line in file:
        string_lst = line.split(' ')
        for symbol in string_lst:
            if int(symbol) == 1:
                count += 1
print(count)

with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    line1 = lines[13].split(' ')
    item = int(line1[7])
    print(item)

s = 0
with open('my_file.txt', 'r') as file:
    for line in file:
        string_lst = line.split(' ')
        for symbol in string_lst:
            s += int(symbol)

print(s)

s = 0
with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    for i in range(2, 12, 3):
        line_lst = lines[i].split(' ')
        for symbol in line_lst:
            s += int(symbol)
print(s)