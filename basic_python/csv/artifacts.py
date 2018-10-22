import csv


with open('fin.csv',newline='') as csvfile:
    # artreader = csv.reader(csvfile)
    # rows  = list(artreader)
    # for row in rows[:1]:
    #     print(','.join(row))

    artreader = csv.DictReader(csvfile)

    rows  = list(artreader)
    for row in rows:
        print(row)
