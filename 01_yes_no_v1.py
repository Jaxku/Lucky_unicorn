# Ask the user if they have played before
show_instructions = input('Have you played this game before? (Yes/No): ').lower()

# If they say yes, output "Program Continues"
if show_instructions == 'yes':
    print("Program continues")

# If they say no, output "Display Instructions"
elif show_instructions == 'no':
    print("Instructions for program")

# Otherwise - show error
else:
    print("Error: Please put either Yes or No")
