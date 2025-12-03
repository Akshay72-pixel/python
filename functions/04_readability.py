def calculate_bills(cups,per_cup_price):
    total_bill = cups * per_cup_price
    return total_bill
    
print(f"Total bill is {calculate_bills(3,45)}")