# Напишите программу, находящую такое значение глубины х, при котором
# уровень опасности как можно более близок к нулю. На вход программе
# подаётся максимально допустимое отклонение уровня опасности от нуля, а
# программа должна рассчитать приблизительное значение х, удовлетворяющее
# этому отклонению. Известно, что глубина точно больше нуля и меньше четырёх
# метров. Обеспечьте контроль ввода


max_danger_level = 0.01
egg_laying_safe_depth = 0.732421875

min_depth = 0
max_depth = 4

def calculate_danger():
    depth = float(input("Enter depth: "))
    danger_level = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
    return danger_level  # level of danger
print(calculate_danger())



def find_safe_path(max_danger):
    avg_depth = min_depth + max_depth//2
    avg_danger = calculate_danger(avg_depth)





# def find_safe_depth(max_danger):
#     min_depth = 0
#     max_depth = 4
#     avg_depth = (min_depth+max_depth)/2
#     calculate_danger(avg_depth)