menu = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
prices = [3, 2.25, 2.50, 2.50]

gst = float(0.1)
takeAway = float(0.05)

x = 0

orderItems = []
orderPrice = []

nextItem = True

choice = input("Hi, welcome to Cafe au Lait\nWould you like takeaway [T] or Dine in [D]? ")
print("Here is the menu:\n ")

print("$3.00    " + menu[0])
print("$2.25    " + menu[1])
print("$2.50    " + menu[2])
print("$2.50    " + menu[3])

print("\nTo complete order, enter [Done] ")


def order_func():
    count = 0
    while nextItem:
        order = input("Enter Item: ")
        if order == "Cappuccino":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[0] + " * " + str(qty))
            orderPrice.append(prices[0] * qty)
            count = count + 1
        elif order == "Espresso":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[1] + " * " + str(qty))
            orderPrice.append(prices[1] * qty)
            count = count + 1
        elif order == "Latte":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[2] + " * " + str(qty))
            orderPrice.append(prices[2] * qty)
            count = count + 1
        elif order == "Iced Coffee":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[3] + " * " + str(qty))
            orderPrice.append(prices[3] * qty)
            count = count + 1
        elif order == "Done":
            print("Here is your order summary:")
            a = 0
            sub_total = sum(orderPrice)
            while a < count:
                print("Item:  " + orderItems[a])
                print("Price: $" + str(orderPrice[a]))
                a = a + 1
            print("\nSubtotal: $" + str(sum(orderPrice)))
            print("GST: $" + str(sub_total * gst))
            print("Surcharge: $" + str(sub_total * takeAway))
            if choice == "T":
                print("The total price of your order is: $" + str(sub_total + sub_total * takeAway))
            else:
                print("The total price of your order is: $" + str(sub_total + sub_total * gst))
            next_item = False
            return next_item
        else:
            print("Invalid input / item not on menu")


order_func()

def summary_func():
