import csv
import json
books_info = [
    {'title': 'Learning Python',
     'author': 'Mark Lutz',
     'year' : 2020 },

    {'title': 'Python Crush Course',
     'author': 'Eric Matthes',
     'year': 2021},

    {'title': 'The Python Workbook',
     'author': 'Ben Stephenson',
     'year': 2021},

    {'title': 'BEGGINING C++',
     'author': 'Michael Dawson',
     'year': 2023},

    {'title': 'Программирование для начинающих на C#',
     'author': 'Васильев А.Н',
     'year': 2023},

    {'title': 'A scheme of heaven: the history of Astrology and the search our destiny in data',
     'author': 'Alexander Boxer',
     'year': 2020},

    {'title': 'Отражённые в небе мифы Земли',
     'author': 'Щеглов П.В',
     'year': 1986}
]

# with open('books.csv', 'w', newline='') as books_write:
#     writer = csv.DictWriter(books_write, fieldnames=['title', 'author', 'year'])
#     writer.writeheader()
#     writer.writerows(books_info)

def change_structure(input_file, output_file):
    books_by_autor = {}
    with open(input_file, 'r', newline='') as books_read:
        reader = csv.DictReader(books_read, fieldnames=['title', 'author','year'] )
        for lines in reader:
            key = lines['author']
            books_by_autor[key] = lines['title'], lines['year']

            with open(output_file, 'w') as js_write:
                js_write.write(json.dumps(books_by_autor, ensure_ascii=False))

if __name__ == "__main__":
    change_structure('books.csv', 'books_by_author.json')