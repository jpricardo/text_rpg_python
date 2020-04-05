#todos os menos do jogo

def show_menu(options):
	lista = list(options.keys())
	for i in range(len(options)):
		print(f'{i}: {lista[i]}')
	
	sel = int(input('Choose your option..: '))
	select_option(options, sel)

def select_option(options, option):
	lista = list(options.keys())
	options[lista[option]]()

def mainmenu():
	options = {'...': exit, 'Exit': exit}
	show_menu(options)

def exit():
	print('Saindo...')
	return False














