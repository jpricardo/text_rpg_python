#



class Character():


	def __init__(self, name, hp, alive=True):
		self.name = name
		self.hp = int(hp)
		self.alive = alive

	def kill(self):
		self.hp = 0
		self.alive = False






class NPC(Character):
	

	def set_friendly(self, friendly):
		self.friendly = friendly
