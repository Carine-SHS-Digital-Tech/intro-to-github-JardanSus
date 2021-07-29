menu = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
prices = [3, 2.25, 2.50, 2.50]

gst = float(0.1)
takeAway = float(0.15)

count = 0
total = 0
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

print("\nWhen you finish order enter [No] ")
while nextItem:
    if x == 0:
        order = input("What would you like to order? ")
        x = x + 1
        if order == "Cappuccino":
            qty = int(input("How many would you like? [1-10] "))
            orderItems.append(menu[0] + " * " + str(qty))
            orderPrice.append(prices[0] * qty)
            count = count + 1
            total = total + prices[0] * qty
        elif order == "Espresso":
            qty = int(input("How many would you like? [1-10] "))
            orderItems.append(menu[1] + " * " + str(qty))
            orderPrice.append(prices[1] * qty)
            count = count + 1
            total = total + prices[1] * qty
        elif order == "Latte":
            qty = int(input("How many would you like? [1-10] "))
            orderItems.append(menu[2] + " * " + str(qty))
            orderPrice.append(prices[2] * qty)
            count = count + 1
            total = total + prices[2] * qty
        elif order == "Iced Coffee":
            qty = int(input("How many would you like? [1-10] "))
            orderItems.append(menu[3] + " * " + str(qty))
            orderPrice.append(prices[3] * qty)
            count = count + 1
            total = total + prices[3] * qty
        elif order == "No":
            nextItem = False
        else:
            print("Invalid input / item not on menu")
    else:
        order = input("Anything Else? ")
        if order == "Cappuccino":
            qty = int(input("How many would you like? [1-10] "))
            orderItems.append(menu[0] + " * " + str(qty))
            orderPrice.append(prices[0] * qty)
            count = count + 1
            total = total + prices[0] * qty
        elif order == "Espresso":
            qty = int(input("How many would you like? [1-10] "))
            orderItems.append(menu[1] + " * " + str(qty))
            orderPrice.append(prices[1] * qty)
            count = count + 1
            total = total + prices[1] * qty
        elif order == "Latte":
            qty = int(input("How many would you like? [1-10] "))
            orderItems.append(menu[2] + " * " + str(qty))
            orderPrice.append(prices[2] * qty)
            count = count + 1
            total = total + prices[2] * qty
        elif order == "Iced Coffee":
            qty = int(input("How many would you like? [1-10] "))
            orderItems.append(menu[3] + " * " + str(qty))
            orderPrice.append(prices[3] * qty)
            count = count + 1
            total = total + prices[3] * qty
        elif order == "No":
            nextItem = False
        else:
            print("Invalid input / item not on menu")
if choice == "T":
    total = total + total * takeAway
else:
    total = total + total * gst
print("Here is your order summary:")

a = 0
subTotal = sum(orderPrice)

while a < count:
    print("Item:  " + orderItems[a])
    print("Price: $" + str(orderPrice[a]))
    a = a + 1
print("\nSubtotal: $" + str(sum(orderPrice)))
print("GST: $" + str(subTotal * gst))
print("The total price of your order is: $" + str(total))
