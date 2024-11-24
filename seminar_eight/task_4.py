import csv
from csv import DictWriter
from itertools import product
from os import write

def count_total(input_file, output_file):
    revenue = {}
    with open(input_file, 'r', newline='') as csv_read:
        csv_to_read = csv.DictReader(csv_read)
        for row in csv_to_read:
            product = row['product']
            quantity = int(row['quantity'])
            price = float(row['price'])
            total = quantity * price
            if product in revenue:
                revenue[product] += total
            else:
                revenue[product] = total

                with open(output_file,'w', newline='') as csv_write:
                    writer = csv.DictWriter(csv_write, fieldnames=['product', 'total'])
                    writer.writeheader()

                    for product, total in revenue.items():
                        writer.writerow({'product': product, 'total': total})




if __name__ == "__main__":
    count_total('sales.csv','total_sales.csv')


