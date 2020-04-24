#from player import Player

#tim = Player('Tim')

from enemy import Enemy, Troll, Vampyre, VampyreKing

# random_monster = Enemy('Small', 12, 1)
# print(random_monster)

# random_monster.take_damage(4)
# print(random_monster)

# random_monster.take_damage(8)
# print(random_monster)

# random_monster.take_damage(9)
# print(random_monster)

ugly_troll = Troll('Pug')
print('ugly troll - {}'.format(ugly_troll))

another_troll = Troll('Ug')
print('Another troll - {}'.format(another_troll))
another_troll.take_damage(18)

brother = Troll('Urg')
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vamp = Vampyre("Vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)

print('-' * 40)
another_troll.take_damage(30)
print(another_troll)

# while vamp.alive:
# 	vamp.take_damage(1)
	#print(vamp)	
print('-' * 40)
dracula = VampyreKing('Dracula')
print(dracula)
dracula.take_damage(12)
print(dracula)

# print(tim.name)
# print(tim.lives)
# tim.lives -= 1
# print(tim)

# tim.lives -= 1
# print(tim)

# tim.lives -= 1
# print(tim)

# tim.lives -= 1
# print(tim)

# tim._lives = 9
# print(tim)

# tim.level = 2
# print(tim)

# tim.level += 5
# print(tim)

# tim.level = 3
# print(tim)

# tim.score = 500
# print(tim)

