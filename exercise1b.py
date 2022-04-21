# create an empty list
team = []

# ask the user for names.
# enter 'done' when complete
player = ''
while player != 'done':
    player = input('give me a player name: ')
    if player != 'done':
        team.append(player)

# this sorts the names starting with the name that starts with the lowest alphabetical letter
team.sort(key=str.lower)

print('your team is: ')
for p in team: 
    print("\t" + p)