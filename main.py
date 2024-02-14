from math import sqrt

def calc_lineal(x:float,c:float):
    '''Функция для поиска корней линейных уравнений. Возвращает float'''
    result_lineal = abs(c)/x
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

def main():
    while True:
        choice = input("Выберите тип уравнения: \n1. Линейное уравнение (вида ax+c=0)\n2. Квадратное уравнение (вида ax^2+bx+c=0)\n0. Выход\n")
        if choice == "1" or choice == "2":
            if choice == "1" :
                x = float(input("Введите коэффициент при x:"))
                c = float(input("Введите свободных член c:"))
                print(f"Корнем уравнения является: {calc_lineal(x,c)}")
            if choice == "2":
                a = float(input("Введите коэффициент при x^2:"))
                b = float(input("Введите коэффициент при x:"))
                c = float(input("Введите свободных член c:"))
                results = calc_quad(a,b,c)
                if results == None:
                    print("У вашего уравнения нет действительных корней, так как его дискриминант меньше 0")
                elif len(results) == 2:
                    print(f"Корнями уравнения являются x1={results[0]}; x2={results[1]}")
                elif len(results) == 1:
                    print(f"Корнем уравнения является x={results[0]}")
        elif choice == "0":
            break
        else:
            print("Данные введены не корректно.\nПроверьте их!")

if __name__ == "__main__":
    main()