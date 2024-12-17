# Задача 3. Планирование задач
# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD
from datetime import datetime, timedelta

def how_soon_long_ago(days):

    now = datetime.now()
    days_qnt = timedelta(days=days)
    when = now + days_qnt
    formatted_when = when.strftime('\033[1;31m \ndate: %Y-%m-%d \033[1;33m \ntime: %H:%M:%S '
                 '\033[1;34m \nweekday: %A \033[1;36m \nweek number: %W \n')
    return formatted_when


if __name__ =='__main__':
     print(how_soon_long_ago(70))