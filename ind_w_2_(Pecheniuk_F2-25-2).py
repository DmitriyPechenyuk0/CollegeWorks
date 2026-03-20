from math import pi, sqrt, sin, cos, tan, asin, acos

name = "Дмитро"
surname = "Печенюк"
group = "ПЗ-25-2"

g = 2
h = -3
u = 4
v = 9

try:
    Rsult_1 = ((sqrt(h**2 + 4)) / (2 * sqrt(5))) ** ((u - v) / v) + \
              (2 * sqrt(7) - pi) ** (2 / h) / (g**3 + 2*h)

    Rsult_2 = sqrt(sin(3*pi + h)**4) / sin(pi / g**2 + sqrt(5)) - \
              cos(3 / sqrt(2) - pi / h**2)**2

    Rsult_3 = sin(3*pi / (2*u) - pi)**2 - \
              sqrt(cos(sqrt(5)*pi + u**3)**2 + v**2) / abs(2*sqrt(3) - 3*u**2*v)

    Rsult_4 = (cos(sqrt(2)*pi - v**3) + u**g) / sqrt(h**(2*g) + 2) - \
              g**u * (cos(pi/4 + v**2) / sin(pi/4 + v**2))

    Rsult_5 = sin(3*pi - sqrt(u / (2*v))) / cos(5**(u/v) - pi / (2*u*v)) - \
              cos(sqrt(u / v) + 3*pi / sqrt(5))**2

    print(f"Rsult_1 = {round(Rsult_1, 2)}")
    print(f"Rsult_2 = {round(Rsult_2, 2)}")
    print(f"Rsult_3 = {round(Rsult_3, 2)}")
    print(f"Rsult_4 = {round(Rsult_4, 2)}")
    print(f"Rsult_5 = {round(Rsult_5, 2)}")

    Result_list = [round(Rsult_1, 2), round(Rsult_2, 2), round(Rsult_3, 2),
                   round(Rsult_4, 2), round(Rsult_5, 2)]
    print(f"\nResult_list = {Result_list}")
    print(f"Max = {max(Result_list)}, Min = {min(Result_list)}")

    conclusion = "Індивідуальне завдання №2" + "\n" + group + "\n" + surname + " " + name
    print(conclusion)

except ZeroDivisionError:
    print("ділення на нуль")
except ValueError as e:
    print(f"Помилка обчислення: {e}")
except Exception as e:
    print(f"помилка: {e}")