name = "Дмитро"
surname = "Печенюк"
group = "ПЗ-25-2"

conclusion = "Індивідуальне завдання №2" + "\n" + group + "\n" + surname + " " + name
print(conclusion)

p=6
q=-1
u=7
v=-8
array=[1.1, 2.65, -0.84, -0.67, 2.07, 1.6, -3.01, 9,24, 15]

Result_1 = round((p - q) / (u + v), 2); print("Result_1 =", Result_1)
Result_2 = round((p**2 - q**2) / (u - v), 2); print("Result_2 =", Result_2)
Result_3 = round((p**3 - q**3 + u**2 - v**2), 2); print("Result_3 =", Result_3)
Result_4 = round((p + q)**2 - (u + v)**2, 2); print("Result_4 =", Result_4)
Result_5 = round(2 * (u + v)**2 + 5, 2); print("Result_5 =", Result_5)
Result_6 = round((u - q)**4 - (v + p)**2, 2); print("Result_6 =", Result_6)
Result_7 = round((u + v)**3 - (p - q)**2, 2); print("Result_7 =", Result_7)
Result_8 = round((5 + 3**2) / (3 - 2 + 4 - 1 + 2), 2); print("Result_8 =", Result_8)
Result_9 = round(array[2] * array[6] - array[4] * array[8] - array[3] * array[1], 2); print("Result_9 =", Result_9)
Result_10 = round((p + q)**3 + (v - array[3])**2 - u - array[7], 2); print("Result_10 =", Result_10)

print("Result_2 < Result_4 =", Result_2 < Result_4)
print("Result_1 > Result_10 =", Result_1 > Result_10)
print("Result_6 > Result_9 =", Result_6 > Result_9)
print("Result_7 < Result_8 =", Result_7 < Result_8)

Result_list = [
    Result_1, Result_2, Result_3, Result_4, Result_5,
    Result_6, Result_7, Result_8, Result_9, Result_10
]

print("Створений список", Result_list)

Result_list.sort(reverse=True)

print("Відсортований список", Result_list)

print("Максимальне значення", max(Result_list))

print("Мінімальне значення", min(Result_list))