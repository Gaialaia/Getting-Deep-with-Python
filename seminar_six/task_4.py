from time import daylight

# date_str = '31.02.2024'.split('.')
# date_example = list(map(int, date_str))
# day = date_example[0]
# month = date_example[1]
# year = date_example[2]
# print(date_example)


# if g[2] in range(1, 9999):
#      print('year can exist')

# if g[1] in range (1,13):
#     print('month can exist')
#
# if g[0] in range(1,32):
#     print('day can exits')
#     if g[2] % 4 == 0:
#         g[0] = range(1, 30)

# import datetime

def is_leap(year):
    return year % 400 == 0 or year % 4 == 0 or year % 100 == 0


def is_valid_date(date):
    day, month, year = map(int, date.split('.'))

    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    elif month in (4,6,9,11):
        return day < 31
    elif month == 2:
        if is_leap(year):
            return day < 30
        else:
            return day < 29
    else:
        return True

if __name__ == '__main__':
   print(is_valid_date('17.02.1986'))
   print(is_valid_date('28.02.2024'))