"""Randomly pick customer and print customer info"""

from random import choice
from customers import get_customers_from_file

# need to get better at modularity (my first solution below):

# customers = get_customers_from_file(file_path)
# winner = random.choice(customers)
# print(f"Tell {winner} they won")

# from peeking at solution, it's better to copy over the existing functions 
# from V1 of raffle and edit

def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    print("Tell {name} at {email} that they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        ))


def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)


if __name__ == "__main__":
    # to run if the file is called as a script
    run_raffle()

# seems like I got the import correct but just need to consider the value of
# multiple functions / files for modularity



