import csv

with open("C:\Max\Code\supermarket_sales.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("C:\Max\Code\supermarket_sales_new.csv", 'w', newline='') as new_csv_file:
        fieldnames = ['City', 'Unit price']
        csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, extrasaction='ignore')

        csv_writer.writeheader()

        # sukuriau nauja faila tik su city ir unit prices laukais
        for line in csv_reader:
            csv_writer.writerow(line)