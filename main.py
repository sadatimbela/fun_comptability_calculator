letters = "abyz"
numbers1 = []
numbers2 = []
user_name1 = str(input('What is your name?'))
user_name2 = str(input('What is another person name?'))

for letters in user_name1:
    number = ord(letters)-96
    numbers1.append(number)
for letters in user_name2:
    number = ord(letters)-96
    numbers2.append(number)
new_number = int(sum((numbers1+numbers2)))
magic_number = int(new_number % 9)
print(magic_number)


def love_check(magic_number):
    if 1 >= magic_number <= 1.9:
        return('Perfect match')
    elif 2 >= magic_number <= 2.9:
        return('Worst Match')
    elif 3 >= magic_number <= 3.9:
        return('somehow good')
    elif 4 >= magic_number <= 4.9:
        return('Worst End')
    elif 5 >= magic_number <= 5.9:
        return('Bad start,good end')
    elif 6 >= magic_number <= 6.9:
        return('bad ever')
    elif 7 >= magic_number <= 7.9:
        return('All the way to your goals')
    elif 8 >= magic_number <= 8.9:
        return('bad chemistry')
    else:
        return('till eternity')


print('Hellow, Your Love comptability is {}.'.format(love_check(magic_number)))
