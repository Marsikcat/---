from math import sqrt

def calc_lineal(x:float,c:float):
    '''Функция для поиска корней линейных уравнений. Возвращает float'''
    result_lineal = (-1*c)/x
    return result_lineal

def calc_quad(a:float,b:float,c:float):
    '''Функция для поиска корней квадратных уравнений. Возвращает list с корнями'''
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b+sqrt(discriminant))/(2*a)
        x2 = (-b-sqrt(discriminant))/(2*a)
        result_quad = [x1,x2]
    elif discriminant == 0:
        x = -b/(2*a)
        result_quad = [x]
    else:
        result_quad = None
    return result_quad
