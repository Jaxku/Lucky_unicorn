"""Component 3 (random tokens) v2
Calculate user valance based on random selection of tokens """

import random

balance = 100  # How much the user has when in the actual program the balance will equal how much the user is going to use.

# Testing loop to generate 100 tokens
for item in range(500):
    number = random.randint(1, 100)

    # adjust Balance
    # if the random number is between 1 and 5
    # user gets a unicorn (add $4 to balance)

    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50

    # Output
print(f"Token: {token}, Balance: ${balance}")
print(f"Final balance = ${balance: ,2f}")
