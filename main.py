print('Введите число:')
user_input = input()
print('Вы ввели - ' + user_input)

# Все числа, заканчивающиеся на 1, кроме 10-19:
if (len(user_input) == 1 or user_input[-2] != '1') and user_input[-1] == '1':
    print(user_input + ' компьютер')

# Все числа, заканчивающиеся на 2-4, кроме 10-19:
elif (len(user_input) == 1 or user_input[-2] != '1') and '2' <= user_input[-1] <= '4':
    print(user_input + ' компьютера')

else:
    print(user_input + ' компьютеров')
