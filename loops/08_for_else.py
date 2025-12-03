staff = [("Amit",17),("Zara",16),("Akshay",17)]

for name,age in staff:
    if age>= 18:
        print(f"{name} is eligible")
        break
else:
    print(f"No one is eligible in the list")    