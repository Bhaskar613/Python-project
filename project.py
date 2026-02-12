menu = {"Pizza": 50, "Salad": 30, "Burger": 100, "Pop corn": 150, "Chicken puff": 100}
print("Welcome to our Coder Cafe")
print("Pizza:50\nSalad:30\nBurger:100\nPop corn:150\nChicken puff:100S")
order_item = input("Enter your item: ")

order_total = 0
if order_item in menu:
    order_total += menu[order_item]
    order = input("Do you want anything else(Yes/No): ")
    if order == "Yes":
        order_item2 = input("Enter Your Second Item: ")
        if order_item2 in menu:
            order_total += menu[order_item2]
            print(f"Your Order Value : {order_total}")
    else:
        print(f"Your Order Value : {order_total}")

else:
    print("You Entered a Wrong Item")
