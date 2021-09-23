from random import randint
board = list(range(1,10))

# Рисуем игровое поле
def field(board):
    print ("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print ("-" * 13)

# Пользователь делает ход
def user_input(player_token):
    valid = False
    while not valid:
        player_step = input("Выберите поле " + player_token)
        try:
            player_step = int(player_step)
        except:
            print ("Нужны лишь цифры. От 1 до 9. Попробуйте еще раз")
            continue
        if 1 <= player_step <= 9:  #and player_step <= 9:
            if (str(board[player_step-1]) not in "XO"):
                board[player_step-1] = player_token
                valid = True
            else:
                print ("Это поле уже отмечено")
        else:
            print ("Цифры. Только цифры. От 1 до 9.")

# Компьютер наносит ответный удар
def cpu_input(cpu_token):
    valid = False
    cpu_step = randint(1,9)
    while not valid:
        if (str(board[cpu_step-1]) not in "XO"):
                board[cpu_step-1] = cpu_token
                valid = True
        else:
            cpu_step = randint(1, 9)

# Конец игры
def gameover(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

# Игра
def game(board):
    counter = 0
    win = False
    while not win:
        field(board)
        if counter % 2 == 0:
            user_input("X")
        else:
            cpu_input("O")
        counter += 1
        if counter > 4:
            tmp = gameover(board)
            if tmp:
                print (tmp, "Игра окончена")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    field(board)

game(board)