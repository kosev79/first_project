# ВАРИАНТ 1
#
# def connect_db(connect: dict) -> str:
#     match connect:
#         case {"server": host, "login": login, "password": psw, "port": port}:
#             pass
#         case {"server": host, "login": login, "password": psw}:
#             port = 22
#         case _:  # wildcard
#             return "error connection"

#     return f"connection: {host}@{login}.{psw}:{port}"


# request = {"server": "89.169.11.5", "login": "root", "password": "1234"}

# result = connect_db(request)
# print(result)

# ВАРИАНТ 2


def book_to_tuple(
    data: dict | tuple | list, min_year=1800, max_year=3000
) -> tuple | None:
    price = None
    match data:
        case author, title, int(year):
            pass
        case author, title, int(year), price, *_:
            pass
        case {"author": author, "title": title, "year": int(year), "price": price}:
            pass
        case {"author": aythor, "title": title, "year": int(year)}:
            pass
        case _:
            return None

    if not (min_year < year < max_year):
        return None

    return author, title, year, price


book_1 = ("Balakirev", "Python", 2022)
book_2 = ["Balakirev", "Python OOP", 2022, 3245.34, "35 str"]

result = book_to_tuple(book_1)
print(result)
