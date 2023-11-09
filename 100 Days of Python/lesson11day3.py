print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

price = 0 
match size:
    case "S":
        price += 15
    case "M":
        price += 20
    case "L": 
        price += 25

match add_pepperoni:
    case "Y":
        if size == "S":
            price += 2
        if size == ("M" or "L"):
            price += 3
    case "N":
        price += 0

match extra_cheese:
    case "Y":
        price += 1
    case "N":
        price += 0

print('Thank you for choosing Python Pizza Deliveries!')
print(f'Your final bill is: ${price}.')


# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

# Example Input
# L
# Y
# N
# Example Output

# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.


