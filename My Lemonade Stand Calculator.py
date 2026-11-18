def greet():
    print("Good Morning...")
    print("Welcome to the my lemonade stand!")
greet()
price_per_cup=float(input("Enter the price:"))
num_cup=int(input("How many cups do you want?"))

def calculate(price,cup):
    total=price * cup
    return total
total_price=calculate(price_per_cup,num_cup)
print("Total is ",total_price)

amount_paid=float(input("Enter the amount that you gave/paid: "))
def change(amount_paid,total_price):
    change_due=amount_paid-total_price
    return change_due
change_due=change(amount_paid,total_price)
print("Change due is ",change_due )
    