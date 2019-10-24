MELON_COST = 1.00


def print_payment_status(payment_data_filename):
    """Calculate cost of melons and determine who has underpaid."""

    payment_data = open(payment_data_filename) # open the file

    # Iterate over lines in file
    for line in payment_data:
        # Split line by '|' to get a list of strings
        order = line.split('|')

        # Get customer's full name
        full_name = order[1]

        # Split `customer_name` by space (' ') to get
        # a list of [first_name, last_name].
        #
        # Then, assign first name (at index 0) to `customer_first`
        first_name = customer_name.split(" ")[0]

        # Get no. of melons in the order and amount customer paid
        melons_qty = float(order[2])  # also ok to typecast melons_qty as an int
        amt_paid = float(order[3])

        # Calculate expected price of customer's order
        expected_price = melons_qty * MELON_COST

        # Print general payment info
        print(f"{full_name} paid ${amt_paid:.2f}, expected",
              f"${expected_price:.2f}")

        # Print payment status
        #
        # If customer overpaid, print that they've overpaid for their melons. If
        # customer underpaid, print that they've underpaid for their melons.
        if expected_price < amt_paid:
            print(f"{first_name} has overpaid for their melons.")

        elif expected_price > amt_paid:
            print(f"{first_name} has underpaid for their melons.")

    # Close the file
    payment_data.close()


# Call the function
print_payment_status("customer-orders.txt")
