# Импорт функции получения случайных чисел из модуля random.
from random import randint

# Получаем случайное число в диапазоне от 1 до 100.
number = randint(1, 100)
print('Угадайте число от 1 до 100')

def attempt(number):
    if 10 < number < 20:
        return 'попыток!'
    elif number % 10 == 1:
        return 'попытку!'
    elif 2 <= number % 10 <= 4:
        return 'попытки!'
    else:
        return 'попыток!'

counter = 0
while True:
    # Получаем число от пользователя и сохраняем его в переменную.
    guess = int(input('Введите число: '))
    counter += 1
    # Если число меньше загаданного...
    if guess < number:
        # ...выводим сообщение.
        print('Надо больше')
    # Если число больше загаданного...
    elif guess > number:
        print('Надо меньше')
    # Если число угадано...
    else:
        # ...прерываем выполнение программы и...
        break

    # выводим сообщение.

print('Отличная интуиция! Вы угадали число за', counter, attempt(counter))
