"""Component 3 (random tokens) v3
Format currency
Ensure odds favour the house - 10% chance of unicorn and 3-% chance for each of
donkey, zebra, or house"""

import random

token = ["unicorn", "horse", "horse", "horse", "donkey", "donkey", "donkey", "zebra", "zebra", "zebra"]
STARTING_BALANCE = 100
balance = STARTING_BALANCE  # How much the user has when in the actual program the balance will equal how much the user is going to use.

# Testing loop to generate 20 tokens
for item in range(500):
    token = random.choice(token)

# Adjusting Balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50

    # Output
print(f"Starting balance = ${STARTING_BALANCE:.2F}")
print(F"Final balance = ${balance:.2f}")
