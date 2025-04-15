# проверяет вхождение в словарь d ключа key
# еслт ключ существует, то в список со значением добавляет value
# если такого ключа нет, то значение value добавляется в ключ 2*key
# если ключ 2*key не существует, то создается такой ключ и в него записывается value

dictionary = {1: 0, 2: 1}


def update_dictionary(d, key, value) -> None:
    if key in d:
        if isinstance(d[key], list):
            d[key].append(value)
        else:
            d[key] = [d[key], value]
    else:
        if 2 * key in d:
            if isinstance(d[2 * key], list):
                d[2 * key].append(value)
            else:
                d[2 * key] = [d[2 * key], value]
        else:
            d[2 * key] = [value]


update_dictionary(dictionary, 3, 1)
print(dictionary)

# print(dictionary.get(1))
