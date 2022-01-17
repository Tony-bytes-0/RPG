from clases import *
from characterObjects import *
import sqlite3, os

loop=[ True, True ]#INICIO

#------------------------  base de datos-----------------
'''appPath = os.getcwd()
dbPath = appPath + '/savaData.db'
conex = sqlite3.connect(dbPath)
cursor = conex.cursor()

cursor.executemany("INSERT INTO SAVEDATA VALUES (?,?,?,?,?,?,?,?,?)", )
conex.commit()

conex.close()'''
#------------------------  base de datos-----------------

#------------------------  menu inicio  ------------------
main = adventure() 
print('1._ Nueva Partida\n2._ Continuar')
op = input('-->')

if op == '1':#crear objetos desde 0
	mc = mainCharacter('admin!',*preClass[6])#fines depurativos
	mc.status()#chequear status del personaje pricipal
	enemy = enemy(*main.listOfEnemys[0])#creacion de enemigo
			
elif op == '2':
	print('aqui se cargan los datos de la base')

else:
	print('opcion invalida')
#-----------------------------  fin de inicio  --------------

mainMenuOptions=['1._ Avanzar','2._ Inventario',
'3._ estado de la aventura', '4._ descansar',
'5._ luchar contra enemigo random','7._ exportar datos'] 
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

	elif op == '7':
		export = main.export(mc)
		for data in export:
			print(data)
		'''appPath = os.getcwd()
		dbPath = appPath + '/savaData.db'
		conex = sqlite3.connect(dbPath)
		cursor = conex.cursor()

		cursor.executemany("INSERT INTO SAVEDATA VALUES (?,?,?,?,?,?,?,?,?)", )
		conex.commit()

		conex.close()'''

	else:
		print('opcion invalida')




		'''while loop[0]:#creacion y asignacion de clases al personaje principal
	op = input('Seleccion de Clase\n1._Guerrero-\n2._Maga-\n3._Asesina-\n4._No muerto-\n5._Cazador-\nEleccion: ')
	if op=='1' or op=='2' or op=='3' or op=='4' or op=='5':
		name=input('inserte el nombre de su personaje: ')
		mc = mainCharacter(name,*PreClass[int(op)])
		loop[0]=False
	else:
		print('introduce un numero entre el 1 y el 5!\n')#fin de creacion de personaje---------------------------'''
#acabo de comentar la creacion de personaje para comenzar a testear todo mas rapido
