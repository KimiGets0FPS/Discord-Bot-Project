import  csv

with open('data_for_user.csv', newline='') as csvfile:
    inv_reader = csv.reader(csvfile, delimiter='.', quotechar='_')
    for row in inv_reader:
        print(' '.join(row))
