import Generator as tg

locked_symbol = '\u25A0'
heart_symbol = '\u2764'


def lock_word(word):
    word_list = [a for a in word]
    output = ''

    for i in range(0, len(word)):
        word_list[i] = locked_symbol

    return output.join(word_list)


def unlock_part_of_word(unlocked_word, locked_word, part):
    all_part_indexs = []

    locked_word_list = [a for a in locked_word]
    output = ''

    for i in range(0, len(unlocked_word)):
        if unlocked_word[i] == part:
            all_part_indexs.append(i)

    for j in all_part_indexs:
        locked_word_list[j] = part

    return output.join(locked_word_list)


def start_game():
    lifes_count = 3
    current_word = tg.get_word()
    locked_word = lock_word(current_word)

    while True:
        print(f'{locked_word} | {heart_symbol}x{lifes_count}')
        player_answer = input('Назовите букву или слово целиком: ')

        if player_answer == current_word:
            print('Вы выиграли! Приз в студию!')
            break
        elif player_answer in current_word:
            if player_answer in locked_word:
                print('Эта буква уже открыта')
            else:
                print('Правильно!')
                locked_word = unlock_part_of_word(current_word, locked_word, player_answer)

            if locked_symbol not in locked_word:
                print('Вы выиграли! Приз в студию!')
                break
        else:
            print('Неправильно. Вы теряете жизнь')
            lifes_count -= 1

        if lifes_count == 0:
            print('Жизни закончились. Вы проиграли')
            break