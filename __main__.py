#

import classes as cl



teste = cl.NPC('Testinho', 100)
teste.set_friendly(False)
print(teste.__dict__)

testinho = cl.Enemy('Doente', 50)
testinho.set_drop(drop=['espada', 'bosta'], drop_rate=[0.01, 0.5])
print(testinho.__dict__)

def create_character():
	name = input('Nome: ')
	hp = int(input('HP: '))
	c = cl.NPC(name, hp)

	return c





test = create_character()
print(test.__dict__)
