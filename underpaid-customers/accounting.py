
def check_payment(path, melon_cost = 1.00):
    """ processes an input order log to check if customer's have properly paid
    
    allows for setting of a singular meon price but defaults to $1.00 if none
    is given

    """
    
    order_log = open(path) # took this from the previous hw, opens the input file!
    for line in order_log:
        line = line.strip() # strips any leading white space
        customer_info = line.split('|') # splits entry into a list
        customer_name = customer_info[1] # [0] contains the customer #
        customer_melons = float(customer_info[2]) # use float in case item is str
        customer_paid = float(customer_info[3])

        payment_expected = customer_melons * melon_cost
        # calculates what the customer should have paid

        if payment_expected != customer_paid:
            print("{0} paid ${1:.2f} expected ${2:.2f}.".format(customer_name, customer_paid, payment_expected))
            #print(f"{customer_name} paid ${customer_paid:2f} expected ${payment_expected:2f}")
            # ^ was having trouble formatting as above

            # with more time I would include some logic to check if customer
            # over or under paid (although looking over the output it appears 
            # all the differences were situations where customer underpaid)

    order_log.close() # closes files

check_payment('customer-orders.txt') 
# calls the function with the input file we were given 
# could also ask for an input file path! (would need to be in the same folder)


""" Reflection from Soln:

solution decided to go further with customer name to esp save the first name

also implemented what I was thinking about : under and over paying

"""