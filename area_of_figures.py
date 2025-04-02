# Считает площадь треугольника, прямоугольника или круга по выбору
type_figure = input()

if type_figure == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    
elif type_figure == "прямоугольник":
    a = int(input())
    b = int(input())
    print(a * b)
    
elif type_figure == "круг":
    r = int(input())
    print(3.14 * (r ** 2))
    
    