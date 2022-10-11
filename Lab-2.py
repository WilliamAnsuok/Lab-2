import csv

def esc(code):
    return f'\u001b[{code}m'

def flag_finland():
    for i in range(4):
        print(WHITE + '   ' * 4 + BLUE + '   ' * 2 + WHITE + '   ' * 10 + END)

    for i in range(2):
        print(BLUE + '   ' * 16 + END)

    for i in range(4):
        print(WHITE + '   ' * 4 + BLUE + '   ' * 2 + WHITE + '   ' * 10 + END)
    print('')


def flag_Israel():
    print(WHITE + '   ' * 19 + END)
    print(BLUE + '   ' * 19 + END)
    print(WHITE + '   ' * 19 + END)
    print(WHITE + '   ' * 9 + BLUE + '   ' + WHITE + '   ' * 9 + END)
    print(WHITE + '   ' * 8 + BLUE + '   ' + WHITE + '   ' + BLUE + '   ' + WHITE + '   ' * 8 + END)
    print(WHITE + '   ' * 8 + BLUE + '   ' + WHITE + '   ' + BLUE + '   ' + WHITE + '   ' * 8 + END)
    print(WHITE + '   ' * 4 + BLUE + '   ' * 11 + WHITE + '   ' * 4 + END)
    print(
        WHITE + '   ' * 5 + BLUE + '   ' + WHITE + '   ' + BLUE + '   ' + WHITE + '   ' * 3 + BLUE + '   ' + WHITE + '   ' + BLUE + '   ' + WHITE + '   ' * 5 + END)
    print(WHITE + '   ' * 6 + BLUE + '   ' + WHITE + '   ' * 5 + BLUE + '   ' + WHITE + '   ' * 6 + END)
    print(WHITE + '   ' * 6 + BLUE + '   ' + WHITE + '   ' * 5 + BLUE + '   ' + WHITE + '   ' * 6 + END)
    print(
        WHITE + '   ' * 5 + BLUE + '   ' + WHITE + '   ' + BLUE + '   ' + WHITE + '   ' * 3 + BLUE + '   ' + WHITE + '   ' + BLUE + '   ' + WHITE + '   ' * 5 + END)
    print(WHITE + '   ' * 4 + BLUE + '   ' * 11 + WHITE + '   ' * 4 + END)
    print(WHITE + '   ' * 8 + BLUE + '   ' + WHITE + '   ' + BLUE + '   ' + WHITE + '   ' * 8 + END)
    print(WHITE + '   ' * 8 + BLUE + '   ' + WHITE + '   ' + BLUE + '   ' + WHITE + '   ' * 8 + END)
    print(WHITE + '   ' * 9 + BLUE + '   ' + WHITE + '   ' * 9 + END)
    print(WHITE + '   ' * 19 + END)
    print(BLUE + '   ' * 19 + END)
    print(WHITE + '   ' * 19 + END)
    print('')


def pattern(n):
    n *= 2
    print((WHITE + '   ' * 2 + RED + '   ' * 2 + WHITE + '   ' * 2 + END) * n)
    print((WHITE + '   ' + RED + '   ' * 4 + WHITE + '   ' + END) * n)
    print((RED + '   ' * 6 + END) * n)
    print((RED + '   ' * 6 + END) * n)
    print((WHITE + '   ' + RED + '   ' * 4 + WHITE + '   ' + END) * n)
    print((WHITE + '   ' * 2 + RED + '   ' * 2 + WHITE + '   ' * 2 + END) * n)
    print('')


def bar_chart(ex, ch):
    if ex > ch:
        maxz = ex
        minz = ch
        flag = 0
    else:
        maxz = ch
        minz = ex
        flag = 1
    for i in range(100, 0, -10):
        if i != 100:
            if maxz == i and minz == i:
                print(' ' + str(i) + BLACK + ' ' + WHITE + '   ' + RED + '   ' + WHITE + '   ' + BLUE + '   ' + WHITE + '   ' + END)
                maxz -= 10
                minz -= 10
            elif maxz == i:
                print(' ' + str(i) + BLACK + ' ' + WHITE + '   ' * 3 + BLUE + '   ' + WHITE + '   ' + END)
                maxz -= 10
            else:
                print(' ' + str(i) + BLACK + ' ' + WHITE + '   ' * 5 + END)
        else:
            if maxz == i and minz == i:
                print(str(i) + BLACK + ' ' + WHITE + '   ' + RED + '   ' + WHITE + '   ' + BLUE + '   ' + WHITE + '   ' + END)                                                                                                                                                                                                                                                                                      #Written by Khafizov Rodion
                maxz -= 10
                minz -= 10
            elif maxz == i:
                print(str(i) + BLACK + ' ' + WHITE + '   ' * 3 + BLUE + '   ' + WHITE + '   ' + END)
                maxz -= 10
            else:
                print(str(i) + BLACK + ' ' + WHITE + '   ' * 5 + END)
    if flag == 0:
        print('      <=200  >200   ')
    else:
        print('      >200  <=200   ')

RED = esc(41)
BLUE = esc(44)
WHITE = esc(107)
END = esc(0)
BLACK = esc(40)

chip = 0
counter = -1
expensive = 0

with open('books.csv', 'r', encoding='cp1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:
        counter += 1
        if counter > 0:
            if int(row[7][:-3]) > 200:
                expensive += 1
            else:
                chip += 1


check = '1234'
pers_ch = chip / counter * 100
pers_ex = expensive / counter * 100

if str(pers_ex)[-1] in check:
    pers_ex = (pers_ex // 10) * 10
    pers_ch = (pers_ch // 10 + 1) * 10
else:
    pers_ex = (pers_ex // 10 + 1) * 10
    pers_ch = (pers_ch // 10) * 10

flag_finland()
flag_Israel()
pattern(int(input('Введите количество повторений орнамента: ')))
bar_chart(pers_ex, pers_ch)
print('  5' + BLACK + ' ' + WHITE + '   ' * 9 + BLUE + '   ' + END)
print('4.5' + BLACK + ' ' + WHITE + '   ' * 8 + BLUE + '   ' + WHITE + '   ' + END)
print('  4' + BLACK + ' ' + WHITE + '   ' * 7 + BLUE + '   ' + WHITE + '   ' * 2 + END)
print('3.5' + BLACK + ' ' + WHITE + '   ' * 6 + BLUE + '   ' + WHITE + '   ' * 3 + END)
print('  3' + BLACK + ' ' + WHITE + '   ' * 5 + BLUE + '   ' + WHITE + '   ' * 4 + END)
print('2.5' + BLACK + ' ' + WHITE + '   ' * 4 + BLUE + '   ' + WHITE + '   ' * 5 + END)
print('  2' + BLACK + ' ' + WHITE + '   ' * 3 + BLUE + '   ' + WHITE + '   ' * 6 + END)
print('1.5' + BLACK + ' ' + WHITE + '   ' * 2 + BLUE + '   ' + WHITE + '   ' * 7 + END)
print('  1' + BLACK + ' ' + WHITE + '   ' * 1 + BLUE + '   ' + WHITE + '   ' * 8 + END)
print('0.5' + BLACK + ' ' + BLUE + '   ' + WHITE + '   ' * 9 + END)
print('  0   1  2  3  4  5  6  7  8  9  10')
