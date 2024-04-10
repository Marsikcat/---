# pyinstaller --onefile -w --collect-data flet -n MDEE main.py
import flet as ft
import logic
import threading

def main(page: ft.Page):
    '''Главное окно'''
    alph = "qwertyuiopasdfghjklzxcvbnm йцукенгшщзхъфывапролджэячсмитьбю!@#$%^&*()_+=-';:[/,<>?`~]" #словарь исключающих символов
    limits = [int(x) for x in range(-10000,10001)] #пределы вводимых чисел        
    def lineal_window(page1: ft.Page):
        '''Окно для ввода коэффициентов линейного уравнения'''

        def solve_lineal(e):
            '''Проверка вводимых значений и вычисление результата линейного уравнения'''
            global close_flag1
            error_flag = False
            if not(x_box.value == '' or c1_box.value == '' ): 
                for x in range(len(x_box.value)):
                    if x_box.value[x] in alph or x_box.value == "0":
                        error_flag = True
                        break
                for y in range(len(c1_box.value)):
                    if c1_box.value[y] in alph :
                        error_flag = True
                        break
                if not(error_flag):
                    if int(float(x_box.value)) in limits and int(float(c1_box.value)) in limits:
                        result_label.value = (f'Результат х={logic.calc_lineal(x=float(x_box.value),c=float(c1_box.value))}')
                        page.update()
                        close_flag1 = True
                    else:
                        open_dlg(e)
                else:
                    open_dlg(e)
            else:
                open_dlg(e)

        def close_window(e):
            '''Закрытие окна'''
            while True:
                if close_flag1:
                    page1.window_close()
                    break
                else:
                    pass
        
        def open_dlg(e):
            '''Открытие окна со справкой'''
            page1.dialog = dlg
            dlg.open = True
            page1.update()

        global x_box,c1_box,close_flag1
        close_flag1 = False
        # диалоговое окно справки
        dlg = ft.AlertDialog(title = ft.Text('Выберите нужный тип уравнения, нажав на кнопку с типом уравнения.Введи коэффициенты для уравнения (только цифры, дробная часть вводится через точку;ограничение по диапазону [-10000;10000] и количеством цифр после запятой меньше 6). При вводе коэффициент линейного уравнения не равен  0 у «x». Нажмите кнопку "ок" для рассчета корней уравнения\nКорни выведутся в главное окно с выбором типа уравнения в "результат"',size=10),on_dismiss=lambda e: print())
        # кнопка для открытия диалогового окна со справкой
        open_dialog = ft.IconButton(width=100,height=35,on_click=open_dlg,icon=ft.icons.QUESTION_MARK)
        label = ft.Text(value="Введите линейное уравнение (вида ax+c=0)")
        # поле для ввода коэффициента x
        x_box = ft.TextField(width=100,height=35,text_align=ft.TextAlign.CENTER)
        x_label = ft.Text(value="x+",height=35,size=20)
        # поле для ввода коэффициента с
        c1_box = ft.TextField(width=100,height=35,text_align=ft.TextAlign.CENTER)
        c1_label = ft.Text(value="=0",height=35,size=20)
        # кнопка расчёта результата
        ok_button = ft.ElevatedButton(text="Найти х",on_click=solve_lineal)
        # параметры окна
        page1.window_focused
        page1.window_height = 230
        page1.window_width = 435
        page1.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page1.add(
            ft.Row([label,open_dialog]),
            ft.Row([x_box,x_label,c1_box,c1_label]),
            ok_button
            )
        page1.update()
        threading.Thread(target=close_window(None)).start()        

    def quad_window(page2: ft.Page):
        '''Окно для ввода коэффициентов квадратного уравнения'''
        def solve_quad(e):
            '''Проверка вводимых значений и вычисление результата квадратного уравнения'''
            global close_flag2
            error_flag = False
            if  not(a_box.value == '' or b_box.value == '' or c2_box.value == ''): 
                for x in range(len(a_box.value)):
                    if a_box.value[x] in alph or a_box == "0":
                        error_flag = True
                        break
                for y in range(len(b_box.value)):
                    if b_box.value[y] in alph :
                        error_flag = True
                        break
                for z in range(len(c2_box.value)):
                    if c2_box.value[z] in alph :
                        error_flag = True
                        break
                if not(error_flag):
                    if int(float(a_box.value)) in limits and int(float(b_box.value)) in limits and int(float(c2_box.value)) in limits:
                        results = logic.calc_quad(a=float(a_box.value),b=float(b_box.value),c=float(c2_box.value))
                        if results == None:
                            result_label.value = (f"У вашего уравнения нет действительных корней, так как его дискриминант меньше 0")
                        elif len(results) == 2:
                            result_label.value = (f"Корнями уравнения являются x1={results[0]:.6f}; x2={results[1]:.6f}")
                        elif len(results) == 1:
                            result_label.value = (f"Корнем уравнения является x={results[0]:.36}")
                        page.update()
                        close_flag2 =True
                    else:
                        open_dlg(e)
                else:
                    open_dlg(e)
            else:
                open_dlg(e)

        def close_window(e):
            '''Закрытие окна'''
            while True:
                if close_flag2:
                    page2.window_close()
                    break
                else:
                    pass
                
        def open_dlg(e):
            '''Открытие окна со справкой'''
            page2.dialog = dlg
            dlg.open = True
            page2.update()

        global a_box,b_box,c2_box,close_flag2
        close_flag2 = False
        # диалоговое окно справки
        dlg = ft.AlertDialog(title = ft.Text('Выберите нужный тип уравнения, нажав на кнопку с типом уравнения.Введи коэффициенты для уравнения (только цифры, дробная часть вводится через точку;ограничение по диапазону [-10000;10000] и количеством цифр после запятой меньше 6). При вводе коэффициент квадратного уравнения  не равен  0 у «x^2». Нажмите кнопку "ок" для рассчета корней уравнения\nКорни выведутся в главное окно с выбором типа уравнения в "результат"',size=10),on_dismiss=lambda e: print())
        # кнопка для открытия диалогового окна со справкой
        open_dialog = ft.IconButton(width=100,height=35,on_click=open_dlg,icon=ft.icons.QUESTION_MARK)
        label = ft.Text(value="Введите квадратное уравнение (вида ax^2+bx+c=0)",text_align="CENTER")
        # поле для ввода коэффициента а
        a_box = ft.TextField(width=100,height=35,text_align=ft.TextAlign.CENTER)
        a_label = ft.Text(value="x^2+",height=35,size=20)
        # поле для ввода коэффициента b
        b_box = ft.TextField(width=100,height=35,text_align=ft.TextAlign.CENTER)
        b_label = ft.Text(value="x+",height=35,size=20)
        # поле для ввода коэффициента c
        c2_box = ft.TextField(width=100,height=35,text_align=ft.TextAlign.CENTER)
        c2_label = ft.Text(value="=0",height=35,size=20)
        # кнопка расчёта результата
        ok_button = ft.ElevatedButton(text="Найти х1 и x2",on_click=solve_quad)
        # параметры окна
        page2.window_focused
        page2.window_height = 230
        page2.window_width = 500
        page2.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page2.add(
            ft.Row([label,open_dialog]),
            ft.Row([a_box,a_label,b_box,b_label,c2_box,c2_label]),
            ok_button
            )
        page2.update()
        threading.Thread(target=close_window(None)).start()

    def open_lineal_window(e):
        '''Открытие окна для ввода коэффициентов линейного уравнения'''
        ft.app(target=lineal_window)
    def open_quad_window(e):
        '''Открытие окна для ввода коэффициентов квадратного уравнения'''
        ft.app(target=quad_window)
    menu_label = ft.Text(value="Выберете тип уравнения")
    # кнопка для выбора линейного уравнения
    lineal_button = ft.ElevatedButton(text="Линейное уравнение",on_click=open_lineal_window)
    # кнопка для ввода квадратного уравнения
    quad_button = ft.ElevatedButton(text="Квадратное уравнение",on_click=open_quad_window)
    # результат расчётов
    result_label = ft.Text(value="")    
    # параметры окна
    page.window_height = 175
    page.window_width = 440
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        menu_label,
        ft.Row([lineal_button,quad_button]),
        result_label
        )
    page.update()

if __name__ == "__main__":
    ft.app(target=main,name="MDEE")