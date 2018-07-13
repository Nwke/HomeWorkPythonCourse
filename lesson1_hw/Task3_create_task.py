"""
Напишем простой калькулятор квадратных уравнений
"""


def solve_equation():
    """Решает квадратное уравнение вида ax^2+bx+c"""

    expression = input('Введите уравнеие ввиде ax^2+bx+c: \n')
    a = expression[:expression.find('x^2')]
    b = expression[expression.find('x^2')+3:expression.rfind('x')]
    c = expression[expression.rfind('x')+1:]
    print(a, b, c)
    a, b, c = (map(int, [a, b, c]))
    D = (b**2) - 4*a*c
    if D > 0:
        print('x1 = ' + str((-b + (D ** 0.5)) / 2*a))
        print('x2 = ' + str((-b - (D ** 0.5)) / 2 * a))
    elif D == 0:
        print('x = ' + str(-b / 2 * a))
    else:
        print('Уравнение не имеет корней в действительных числах')

solve_equation()