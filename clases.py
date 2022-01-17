import random, time
from data import *
#----------------------------------definicion de funciones
def statusBar(player,enemy, turn):
	print(f'---------------------- Barra de Status -------------------------',
		  '\npuntos de vida de ->{}<-: {}/{}'.format(			  player.name, round(player.life,2), player.maxLife) ,
		  '\npuntos de vida de ->{}<-: {}/{}\nturno: {}\n'.format(enemy.name, round(enemy.life,  2) , enemy.maxLife,turn),
		  f'------------------------------------------------------------------')

def lifeCheck(player,enemy):
	if player.life <= 0:
		print('has muerto!\n>>>G A M E  O V E R<<<')
		return False
	elif enemy.life <= 0:
		print(f'>>>{enemy.name} ha muerto!<<<')
		return False
	else:
		return True

def whoMovesFirst(player,enemy):
	if player.speed > enemy.speed:
		return [player, enemy]
	else:
		return [enemy, player]

def battle(player,enemy):#---------------------------------menu de combate{
	keepGoing = True
	turn = 1
	time.sleep(0.3)
	print(f'comienza el combate entre >>> {player.name} y {enemy.name} <<<')

	while keepGoing:

		opponent = whoMovesFirst(player, enemy)#turno del personaje mas rapido
		opponent[0].turn(opponent[1])
		keepGoing = lifeCheck(player, enemy)
		if keepGoing:#comprobacion de vida
			opponent[1].turn(opponent[0])#turno del personaje mas lento

		if keepGoing:#mientras el combate siga, muestrame los datos
			statusBar(player, enemy, turn)
		turn = turn + 1
	
	player.gainExp( enemy.calculateLvL() )#final de la batalla
	player.energy = round(player.energy-(turn/2))
#------------------------------------------------------------}menu de combate

class adventure():#---------------------------------------weas de la aventura
	def __init__(self):
		self.level = 0
		self.world = plainsData
		self.listOfEnemys = plainsEnemys
		self.days = 0

	def advance(self):
		self.level = self.level + 1
		print('se ha avanzado un nivel')

	def status(self):
		print('estado de la aventura: --- Zona:', self.world['name'], '--- nivel:' ,self.level)

	def rest(self,player):
		player.energy = player.maxEnergy
		self.days = days + 1
		print(f'{player.name} descansa y recupera su energia a cambio de un dia')

	def randomEnemy(self, listOfEnemys):
		return random.choice(listOfEnemys)

	def export(self, player):
		return tuple([player.name, player.life, player.maxLife, player.exp, player.maxExp,
				player.attack, player.defence, player.speed, player.chClass])








