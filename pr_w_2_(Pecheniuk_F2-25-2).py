from math import pi, sqrt, asin, acos, degrees

name = "Дмитро"
surname = "Печенюк"
group = "ПЗ-25-2"

""" 
тестовые данные

R   = 11
a   = 13
b   = 15
c   = 6
x_1 = 5
y_1 = -6
x_2 = 2
y_2 = 7

"""

try:
    R = float(input("Задайте радіус кола: "))
    if R <= 0:
        print("радіус має бути більше нуля")
    else:
        S_circle = pi * R**2
        L_circle = 2 * pi * R
        print("S_circle =", S_circle)
        print("L_circle =", L_circle)
except ValueError:
    print("введіть числове значення")

try:
    a = float(input("Задайте сторони трикутника: \na = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if a <= 0 or b <= 0 or c <= 0:
        print("сторони мають бути більше нуля")
    elif a + b > c and a + c > b and b + c > a:
        p_triangle  = (a + b + c) / 2
        S_triangle  = sqrt(p_triangle * (p_triangle - a) * (p_triangle - b) * (p_triangle - c))
        R_described = (a * b * c) / (4 * S_triangle)
        R_inscribed = (2 * S_triangle) / (a + b + c)

        print("P_triangle =", p_triangle * 2)
        print("S_triangle =", S_triangle)
        print("R_described =", R_described)
        print("R_inscribed =", R_inscribed)

        sin_alpha = a / (2 * R_described)
        alpha_rad = asin(max(-1, min(1, sin_alpha)))
        alpha_deg = round(degrees(alpha_rad))

        cos_gamma = (a**2 + b**2 - c**2) / (2 * a * b)
        gamma_rad = acos(max(-1, min(1, cos_gamma)))
        gamma_deg = round(degrees(gamma_rad))

        beta_deg = 180 - (alpha_deg + gamma_deg)

        print("α = %s°; β = %s°; γ = %s°" % (alpha_deg, beta_deg, gamma_deg))
    else:
        print("Такого трикутника не існує")
except ValueError:
    print("Введіть числові значення")

try:
    x_1 = float(input("Задати абсцису початкової точки вектора: "))
    y_1 = float(input("Задати ординату початкової точки вектора: "))
    x_2 = float(input("Задати абсцису кінцевої точки вектора: "))
    y_2 = float(input("Задати ординату кінцевої точки вектора: "))

    a_1 = x_2 - x_1
    a_2 = y_2 - y_1
    len_vector_a = sqrt(a_1**2 + a_2**2)

    print("Координати вектора: (%s; %s) \nДовжина вектора: %s" % (a_1, a_2, len_vector_a))
except ValueError:
    print("Помилка: введіть числові значення!")

conclusion = "Практичну роботу №2" + "\n" + "виконав студент " + group + "\n" + surname + " " + name
print(conclusion)