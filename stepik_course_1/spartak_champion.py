# Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет  n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
# table_results = {command: [games, victories, draws, defeats, scores]}
games_value = int(input())
count = 0
table_results = {}
params = 5

while count < games_value:
    team_1 = [0] * params
    team_2 = [0] * params
    game = []
    game.extend(input().split(";"))
    goals_1 = int(game[1])
    goals_2 = int(game[3])
    team_1[0] += 1
    team_2[0] += 1

    if goals_1 > goals_2:
        team_1[1] += 1
        team_1[4] += 3
        team_2[3] += 1
    elif goals_1 < goals_2:
        team_2[1] += 1
        team_2[4] += 3
        team_1[3] += 1
    else:
        team_1[2] += 1
        team_1[4] += 1
        team_2[2] += 1
        team_2[4] += 1

    if game[0] not in table_results:
        table_results[game[0]] = team_1
    else:
        last_result_1 = [a + b for a, b in zip(table_results[game[0]], team_1)]
        table_results[game[0]] = last_result_1
    if game[2] not in table_results:
        table_results[game[2]] = team_2
    else:
        last_result_2 = [a + b for a, b in zip(table_results[game[2]], team_2)]
        table_results[game[2]] = last_result_2

    count += 1

for keys, values in table_results.items():
    print((keys + ":"), *values, end="\n")
