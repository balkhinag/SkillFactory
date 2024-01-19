"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = np.random.randint(1, 101)) -> int:  
    """Угадываем число, учитывая, больше или меньше случайное число нужного нам числа

    Args:
        number (int, optional): Загаданное число. Defaults to np.random.randint(1, 101).

    Returns:
        int: количество попыток
    """
    left = 0
    right = 100
    count = 0
    predict_number = np.random.randint(1, 101) #
    while predict_number != number: #выполняем цикл, пока не угадаем число 
        count += 1
        predict_number = (left+right) // 2
        if number > predict_number:
            left = predict_number + 1
        elif number < predict_number:
            right = predict_number - 1
        else:
            break
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

score_game(random_predict)