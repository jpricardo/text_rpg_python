#

import classes as cl



teste = cl.NPC('Testinho', 100)
print(teste.__dict__)
teste.set_friendly(False)
print(teste.__dict__)
teste.kill()
print(teste.__dict__)
