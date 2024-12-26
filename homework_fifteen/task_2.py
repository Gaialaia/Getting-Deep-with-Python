# Задача 2. Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.


from datetime import datetime

now = datetime.now()
formatted_date = (now.strftime
                  ('\033[1;32m \ndate: %Y-%m-%d \033[1;33m \ntime: %H:%M:%S '
                   '\033[1;31m \nweekday: %A \033[1;36m \nweek number: %W \n'))

if __name__ == '__main__':
    print(formatted_date)
