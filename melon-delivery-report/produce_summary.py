
def cleanup_melon_report(melon_delivery_info):
    """ processes melon delivery information into a desired format for review
    """

    the_file = open(melon_delivery_info) # opens the delivery input file
    for line in the_file: # loops through each line in the delivery info
        line = line.rstrip() # removes the whitespace at the start of every line
        words = line.split('|') # breaks line into a list of words at each '|'

        melon = words[0] # stores the name of the melon
        count = words[1] # stores the number of melon sold
        amount = words[2] # stores the amount the melons sold for

        # prints the delievery information in a readable format
        print(f"Delivered {count} {melon} for a total of ${amount}")
    the_file.close() # closes the file after looping through all the lines

print("Day 1")
cleanup_melon_report("um-deliveries-20140519.txt")

print("Day 2")
cleanup_melon_report("um-deliveries-20140520.txt")

print("Day 3")
cleanup_melon_report("um-deliveries-20140521.txt")
