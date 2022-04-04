"""Component 3 (random tokens) v2
Calculate user valance based on random selection of tokens """

import random

token = ["unicorn", "horse", "donkey", "zebra"]
balance = 100  # How much the user has when in the actual program the balance will equal how much the user is going to use.
# Testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(token)
    print(token, end='\t')  # can wrap output making it easier to screenshot


# Balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    elif token == "horse" or "zebra":  # could just use a normal else statement instead which would be better if more tokens took off 50 cents, but I kept it like this, so I am able to see which ones are taking money off.
        balance -= .50

    # Output
    print(f"Token: {token}, Balance: ${balance}")
