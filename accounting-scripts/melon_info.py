"""Print out all the melons in our inventory."""


from melons import melon_dictionary


def print_melon(melon_dictionary):
    """Print each melon with corresponding attribute information.

    input: dictionary of melons with a nested dictionary for each melon.
        ex:
        melon_dictionary = {
            'Honeydew': {'price': 0.99, 'seedlessness': True}, ...}

    return: print statements of the melons
    
    """
    
    for melon in melon_dictionary:
        name = melon
        price = melon_dictionary[melon]['price']
        
        seedlessness = 'have'

        if melon_dictionary[melon]['seedlessness']:
            seedlessness = 'do not have'

        print('''{}'s {} seeds and are ${:.2f}'''.format(melon, 
            seedlessness, price))

    # maybe a more efficient to just unpack from dictionary and print
    # one attribute and value at a time

print_melon(melon_dictionary)