#Даны числа x, y. Проверить высказывания: "Точка с координатами (x, y) лежит в чевертой координатной четверти.
x = float(input("Введите x: "))
y = float(input("Введите y: "))
if x > 0 and y > 0:
    print("Точка с координатами ({}, {}) лежит в первой координатной четверти".format(x, y))
elif x < 0 and y > 0:
    print("Точка с координатами ({}, {}) лежит во второй координатной четверти".format(x, y))
elif x < 0 and y < 0:
    print("Точка с координатами ({}, {}) лежит в третьей координатной четверти".format(x, y))
elif x > 0 and y < 0:
    print("Точка с координатами ({}, {}) лежит в четвертой координатной четверти".format(x, y))
else:
    print("Точка с координатами ({}, {}) лежит на одной из осей или в начале координат".format(x, y))