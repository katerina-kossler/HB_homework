"""Generate sales report showing total melons each salesperson sold."""

def generate_number_sales(filepath):
    """ Generates a report of number melons sold by salesperson
        
        Input: filepath in same directory with sales data
            '(Salesperson)|(Revenue Generated)|(Melons Sold)'

        Output: Printed statements of each salesperson adn the number of
        melons they have sold
            '(Salesperson) sold (Melons Sold)'
        
        Assumptions: Assumes only one entry is given per salesperson
        Assumes revenue data is not needed for presentation
    """

    melons_by_salesperson = {}
    # opens data sheet and processes each line 
    file = open(filepath)
    for line in file:
        line = line.rstrip()
        entries = line.split('|')
        salesperson = entries[0]
        melons = int(entries[2])
        # processes each salespersons melon sales into a dictionary
        # this has much faster look up time than two lists
        if salesperson not in melons_by_salesperson:
            melons_by_salesperson[salesperson] = melons
    # looks up each salesperson and prints a statement with number of melons
    # they were able to sell in given time period
    for person in melons_by_salesperson.keys():
        num_melons = melons_by_salesperson[person]
        print(f'{person} sold {num_melons} melons')


generate_number_sales('sales-report.txt')