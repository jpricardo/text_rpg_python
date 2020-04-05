#



class Character():

	def __init__(self, name, hp, alive=True):
		self.name = name
		self.hp = int(hp)
		self.alive = alive

	def kill(self):
		self.hp = 0
		self.alive = False

	def set_drop(self, drop=[], drop_rate=[]):
	
		self.drop = []
		for i in range(len(drop)):
			self.drop.append([drop[i], drop_rate[i]])

	def drop_loot(self):
		pass


class NPC(Character):
	
	def set_friendly(self, friendly):
		self.friendly = friendly


class Enemy(Character):
	pass
	


