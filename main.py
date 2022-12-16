game_on = True
playing_field = [['-', '-', '-'],
                 ['-', '-', '-'],
                 ['-', '-', '-']]
player_sign = 'x'


def print_field(mas):
    print('   0  1  2')
    for i in range(3):
        print(i, ' ', end='')
        for j in range(3):
            print(mas[i][j], end='  ')
        print('\n', end='')


def players_move():
    global player_sign
    coordinates = list(map(int, input(f'Введите координаты хода через пробел, ход игрока {player_sign}:').split(' ')))
    if -1 < coordinates[0] < 3 and -1 < coordinates[1] < 3:
        if playing_field[coordinates[0]][coordinates[1]] == '-':
            playing_field[coordinates[0]][coordinates[1]] = player_sign
            if player_sign == 'x':
                player_sign = 'o'
            else:
                player_sign = 'x'
        else:
            print('Введенная клетка уже заполнена!')
            players_move()
    else:
        print('Вы вышли за пределы поля!')
        players_move()


def is_it_win():
    def game_over(sign):
        global player_sign
        print_field(playing_field)
        print(f'Победил игрок {sign}')
        print('Игра окончена')
        for i in range(3):
            for j in range(3):
                playing_field[i][j] = '-'
        player_sign = 'x'

    for i in range(3):
        if playing_field[i][0] == playing_field[i][1] == playing_field[i][2] and playing_field[i][0] != '-':
            game_over(playing_field[i][0])
            return True
        elif playing_field[0][i] == playing_field[1][i] == playing_field[2][i] and playing_field[0][i] != '-':
            game_over(playing_field[0][i])
            return True
        elif playing_field[0][0] == playing_field[1][1] == playing_field[2][2] and playing_field[0][0] != '-':
            game_over(playing_field[0][0])
            return True
        elif playing_field[0][2] == playing_field[1][1] == playing_field[2][0] and playing_field[0][2] != '-':
            game_over(playing_field[0][2])
            return True
        else:
            return False

def start_game():
    global game_on
    answ = input('Начать игру? Введите "Y", чтобы начать или "N", чтобы закончить. ')
    if answ == 'Y':
        game_on = True
    elif answ == 'N':
        print('Спасибо за игру!')
        game_on = False
    else:
        print('Некорректное значение!')
        start_game()


while game_on:
    print_field(playing_field)
    players_move()
    if is_it_win():
        game_on = False
        start_game()

