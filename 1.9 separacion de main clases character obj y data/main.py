from clases import *
from characterObjects import *

loop=[ True, True ]

mc = mainCharacter('admin!',*preClass[6])#fines depurativos

mc.status()#chequear status del personaje pricipal
main = adventure()#creacion de los datos de la aventura
enemy = enemy(*main.listOfEnemys[0])#creacion de enemigo

mainMenuOptions=['1._ Avanzar','2._ Inventario',
'3._ estado de la aventura', '4._ descansar',
'5._ luchar contra enemigo random'] 
while loop[1]:#------------------menu principal-----------------------
	print('')
	for options in mainMenuOptions:
		print('\n ',options)

	op = input('\n-->')
	if op == '1':
		main.advance()

	elif op == '2':
		mc.inventory()

	elif op == '3':
		main.status()
		mc.status()

	elif op == '4':
		main.rest(mc)

	elif op == '5':
		enemy.reStat(*main.randomEnemy(main.listOfEnemys))
		battle(mc, enemy)

	elif op == '6':# borrar luego!!
		mc.addStat(10)

	else:
		print('opcion invalida')




		'''while loop[0]:#creacion y asignacion de clases al personaje principal
	op=input('Seleccion de Clase\n1._Guerrero-\n2._Maga-\n3._Asesina-\n4._No muerto-\n5._Cazador-\nEleccion: ')
	if op=='1' or op=='2' or op=='3' or op=='4' or op=='5':
		name=input('inserte el nombre de su personaje: ')
		mc=mainCharacter(name,*PreClass[int(op)])
		loop[0]=False
	else:
		print('introduce un numero entre el 1 y el 5!\n')#fin de creacion de personaje---------------------------'''
#acabo de comentar la creacion de personaje para comenzar a testear todo mas rapido
