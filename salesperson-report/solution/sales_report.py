"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

# Loop over each line in file object
f = open('sales-report.txt')
for line in f:
    line = line.rstrip()  # Remove trailing whitespace
    entries = line.split('|')  # Create a list of data

    # Get name of salesperson and no. of melons they've sold
    salesperson = entries[0]
    melons = int(entries[2])

    # If the salesperson is already in `salespeople`, increment the no. of
    # melons they've sold.
    #
    # Otherwise, add the salesperson's name to `salespeople` and
    # `melons` to `melons_sold`
    if salesperson in salespeople:
        # Find the position where `salesperson` is stored in `salespeople`
        position = salespeople.index(salesperson)
        # Use that position to index into `melons_sold`
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Loop over indices of `salespeople` and use it to index into `salespeople` and
# `melons_sold`.
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
