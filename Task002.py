# 2. Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint, choice
import random

greeting = ('Start game')

messages = ['Никому не говори, но я болею за тебя', 'Ты на первом месте, так держать!',
            'А я эти конфеты везде искал', 'Публика от тебя без ума', 'Чудесное представление']

def introduce_players():
    player1 = input('Как Вас зовут?\n')
    player2 = 'The Chosen One'
    print(f'Привет, я {player2}')
    return [player1, player2]

def get_rules(players):
    n = 150
    m = 28
    first = int(input(f'{players[0]}, чтобы ходить первым введите 1, иначе введите любое значение\n'))
    print('Играем на 150 конфет. В ход можно брать не больше 28. Удачи!')
    if first != 1:
        first = 0
    return [n, m, int(first)]

def play_game(rules, players, messages):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'Я беру {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуй ещё раз, у тебя {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Не справился с управлением. GG')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Конфеты кончились')
        count += 1
    return players[count % 2]


print(greeting)


players = introduce_players()
rules = get_rules(players)

winner = play_game(rules, players, messages)
if not winner:
    print('У нас нет победителя.')
else:
    print(f'Победил {winner}! ')