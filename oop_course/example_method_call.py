"""пример реализации удаления символов в начале и конце строки через КЛАСС
а не через замыкание функции"""


class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwds):
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")

        return args[0].strip(self.__chars)


s1 = StripChars("?:!.; ")
s2 = StripChars(" ")
res = s1(" ????:Hello World! ")
res2 = s2(" Hello World! ")
print(res, res2, sep="\n")
