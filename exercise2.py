team = []

player = ''
while player != 'done':
    player = input('give me a player name: ')
    if player != 'done':
        team.append(player)

print('your team is: ')
for p in team: 
    print("\t" + p)

if 'pete' in team:
    print("I can't wait to play.")
else:
    print("Put me in coach, I'm ready to play.")