unit = input("Enter the unit for the amount to be converted: ")

amount = input("Enter the amount to be converted into the desired unit: ")

usd_amount = 73.50

inr_amount = 0.014

if unit == "usd":
    print(inr_amount * int(amount))
elif unit == "inr":
    print(usd_amount * int(amount)) 