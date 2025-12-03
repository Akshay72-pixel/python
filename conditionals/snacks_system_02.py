snack = input("Enter snack you want (samosa or cookies) = " ).lower()


if snack=='samosa' or snack=='cookies':
    print("Order conform..")
else:
    print(f"We did'nt serve {snack}")