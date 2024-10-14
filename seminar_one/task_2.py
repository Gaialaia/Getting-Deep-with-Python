
# Задача 2. Треугольник
# Треугольник существует только тогда, когда сумма любых двух его сторон
# больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если
# хотя бы в одном случае отрезок окажется больше суммы двух других, то
# треугольника с такими сторонами не существует. Отдельно сообщить является
# ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input(" Enter a: "))
b = int(input(" Enter b: "))
c = int(input(" Enter c: "))

if b + c > a and c + a > b and b + a > c:
    print('Triangle exists')
    if a == b > c or a == c > b or b == c > a:
        print('It is an isosceles triangle! 𓇮')
    elif a == b == c:
        print('It is an equilateral triangle!')
    elif a != b != c:
        print('It is a versatile triangle!')
else:
    print('No such triangle')
