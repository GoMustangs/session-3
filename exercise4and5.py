groceriesItems=[]
groceryQuantity=[]
finalList=[]

moneySpent = float(0)

item=''

while item != 'none':

    print('what do you want to get at the grocery store?')

    item = input("item: ")

    if item != 'none':
    
        quantity = float(input("quantity: "))

        price = float(input("price: "))

        groceriesItems.append(item)

        finalList.append(item)
        
        groceryQuantity.append(quantity)

        moneySpent= (price*quantity) + moneySpent
        
else:
    print("here's what you put on the list: ", groceriesItems, 'quantity', groceryQuantity)

print("now go to the grocercy store")

while groceriesItems:
    pickUp = input('what items from the list have you found at the store?: ')
    if pickUp in groceriesItems:
        groceriesItems.remove(pickUp)
    print(groceriesItems)

if not groceriesItems:
    print("you picked up everything. here's your receipt: ", finalList, "here's how much you got of each item", groceryQuantity, "here's how much you spent in total: $", moneySpent)