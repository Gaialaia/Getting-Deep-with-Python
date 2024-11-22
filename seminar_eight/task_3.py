import json, csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as jr:
        prod_js = json.load(jr)
        print(prod_js)
    with open(csv_file,'w', newline='') as cw:
        writer = csv.DictWriter(cw, fieldnames=prod_js[0].keys())
        writer.writeheader()
        writer.writerows(prod_js)


if __name__ == "__main__":
    json_to_csv('products.json', 'products.csv')