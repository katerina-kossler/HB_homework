"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    salesperson = entries[0]
    melons = int(entries[2])

    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
