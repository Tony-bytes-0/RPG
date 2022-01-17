from  data import itemList, preClass
import time
class character():
	def __init__(self,na,li,att,de,sp):#atributos base de cada personaje, contruidos al momento de creacion del objeto
		self.name = na
		self.life = li
		self.maxLife = li
		self.attack = att
		self.defence = de
		self.speed = sp
		self.exp = 0 
		self.maxExp = 5
		self.lvl = 0
		self.items = itemList
		
	def status(self):
		print(self.name,'--> Puntos de Vida:',round(self.life,2),'/',self.maxLife ,
		'Ataque:',self.attack,'Defensa :',self.defence,'Velocidad:',
		self.speed,'Nivel:', self.calculateLvL())

	def basicAttack(self, defender):
		damage=(self.attack*0.5) - (defender.defence*0.5) + 1
		if damage <0:
			damage=damage*-1
		defender.life-=damage
		print(f'{self.name}  ataca a {defender.name} y este recibe {round(damage,2)} de daño!')
		time.sleep(0.3)

	def calculateLvL(self):
		return round((self.maxLife+self.attack+self.defence+self.speed)/4)

	def useItem(self,itemName):#funcionara usando solamente el nombre del item, posteriormente se comprueba su cantidad
		if itemName == 'pocion de vida':
			self.life = self.life + 10
			if self.life > self.maxLife:#si la curacion sobrepasa, ajustar con la salud maxima
				self.life = self.maxLife

		elif itemName  == 'pocion de resistencia':
			self.energy = self.energy + 10
			if self.energy > self.maxEnergy:
				self.energy = self.maxEnergy

		self.items[itemName] = self.items[itemName] - 1
		print(itemName, 'utilizado')


			
class mainCharacter(character):#mc personaje principal
	def __init__(self,na,li,att,de,sp,chClass):
		super().__init__(na,li,att,de,sp)
		self.chClass = chClass
		self.maxLife = li 
		self.energy = 15
		self.maxEnergy = 15

	def status(self):#estado_mc
		print(self.name,'--> Puntos de Vida:',round(self.life,2),'/',self.maxLife,
		'\nNivel:' ,self.calculateLvL(), 'experiencia:',self.exp,'/',self.maxExp,
		'\nClase:',self.chClass,'----- energia :' ,self.energy,'/',self.maxEnergy,
		'\nAtaque:',self.attack,'\nDefensa :',self.defence,
		'\nVelocidad:',self.speed
		)

	def gainExp(self, amount):#ganar experiencia
		self.exp = self.exp + amount
		print('has ganado', amount , ' puntos de experiencia')

		if self.exp >= self.maxExp:#subir de nivel
			print('------------------- Subes de Nivel! -------------------')
			self.addStat( 2 )#trabajando aqui
			self.maxExp = self.maxExp + (self.maxExp * 0.30)
			self.exp = 0

	def addStat(self, amount):#aqui es donde cambio las estadisticas
		def changueAtt(self, attribute, skillPoints):
 			if attribute == 0:
 				self.life = self.life +  skillPoints
 				self.maxLife = self.maxLife +  skillPoints
 			elif attribute == 1:
 				self.attack = self.attack +  skillPoints
 			elif atttibute == 2:
 				self.defence =self.defence +  skillPoints
 			elif attribute == 3:
 				self.speed =self.speed + skillPoints 

		while amount > 0:#bucle para agregar puntos
	 		stats = [ 'Vida', 'Ataque', 'Defensa', 'Velocidad']
	 		i = 0
	 		for stat in stats:#mensaje en pantalla
	 			print(i,'._ ' , stat)
	 			i = i+1

	 		try:
	 			attribute = int(input('caracteristica a mejorar? -->'))
	 			print('puntos disponibles: ', amount)
	 			skillPoints = int(input('cantidad a agregar? -->'))

	 			if skillPoints <= amount:#agregar skillPoints
	 				changueAtt(self, attribute, skillPoints)
	 				amount = amount - skillPoints
	 				#self.status()

	 			else:
	 				print('introduzca un numero entre 0 y ', amount)

	 		except NameError:
	 			print(' algo salio mal :( ')
 		
	def inventory(self):
		avalibleItems = []
		i=0
		for item, cuantity in self.items.items():#lee cada clave y valor por separado del objeto en cuestion
			add=[]
			if cuantity > 0 :#mientras halla existencias del item, se mostrara en pantalla
				add.extend([i, item, cuantity])
				avalibleItems.append(add)
				i = i + 1
		j = 0
		for i in avalibleItems:
			print(avalibleItems[j][0], avalibleItems[j][1], ' x ', avalibleItems[j][2])
			j = j + 1

		try:
			op = int(input('usar objeto nº -->'))
			selectedItem = avalibleItems[op]
			self.useItem(selectedItem[1])
		except:
			print('valor invalido')

	def energy(self,amount):
		self.energy += amount

	def turn(self,enemy):#------------------------------------aqui esta el menu del turno del personaje------------------
		loop=True
		while loop:
			op=input('\nAcciones disponibles de %s 1._ Atacar: 2._Estado ---> '%self.name)
			if     op=='1':
				self.basicAttack(enemy)
				loop=False

			elif op == '2':
				self.status()

			else:
				print('\n opcion invalida. papuh')

class enemy(character):
	def reStat(self,na,li,att,de,sp):
		self.name = na
		self.life = li
		self.maxLife = li
		self.attack = att
		self.defence = de
		self.speed = sp

	def turn(self,player):
		op = random.randint(0,0)
		if op == 0:
			self.basicAttack(player)