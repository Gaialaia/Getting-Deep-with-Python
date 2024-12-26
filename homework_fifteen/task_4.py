# Задача 4. Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе


import argparse

parser = (argparse.ArgumentParser
          (description='Program takes a number and a '
                       'line and prints them'))  # --help
parser.add_argument('-v', '--verbose',
                    help='wtf', action='store_true')
parser.add_argument('number', type=float,
                    help='insert number')
parser.add_argument('line', type=str,
                    help='insert string')
parser.add_argument('--repeat',
                    type=int, default=23)  # on default repeat=23 (--repeat)
args = parser.parse_args()

print(f'{args}')
if args.verbose:
    print(f" Verbose is on, number = {args.number}, "
          f"line = {args.line}, repeat={args.repeat}")
