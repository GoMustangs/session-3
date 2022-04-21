# create an empty list to be filled with groceries to pick up
list = []

# ask the user for grocery items they want to pick up
# enter 'none' when complete
item = ''
while item != 'none':
    item = input('enter a grocery item, or none to exit: ')
    if item != 'none':
        list.append(item)
list.reverse()
print('your grocery list it: ')
for g in list: 
    print("\t" + g)

print("now go to the grocercy store")

while list:
    pickUp = input('what are you getting at the store: ')
    if pickUp in list:
        list.remove(pickUp)
    print(list)

if not list:
    print("you can check out now!")
