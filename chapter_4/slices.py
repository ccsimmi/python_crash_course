players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[:2])
# print(players[-2:])

for player in players[:3]:
    print(player.title())


# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]