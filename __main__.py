#

import classes as cl
import menu as menu

functions = {'Main menu': menu.mainmenu, 'Exit': menu.exit}

teste = cl.NPC('Testinho', 100)
teste.set_friendly(False)


testinho = cl.Enemy('Doente', 50)
testinho.set_drop(drop=['espada', 'bosta'], drop_rate=[0.01, 0.5])


def create_character():
	name = input('Nome: ')
	hp = int(input('HP: '))
	c = cl.NPC(name, hp)

	return c


def main():
	menu.show_menu(functions)

main()
