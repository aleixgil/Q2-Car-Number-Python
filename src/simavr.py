#!/usr/bin/python
#-*- encoding=utf-8 -*-

from intelhex import *
from avrmcu import *
from sys import *

def llegeixLiniaComandes():
	"""
	Llegeix la informació necessària per a la simulació en cas que la seva
	introducció es dugui a terme directament des de la línia de comandes.
	"""
	try:
		nomarxiuhex = argv[-1]
		arguments = []
		for i in argv[1:-1]:
			if i.startswith('-'):
				arguments += i[1:]
		dic = {}
		dic['ProgramDump'] = 'p' in arguments
		dic['RegisterDump'] = 'r' in arguments
		dic['DataDump'] = 'd' in arguments
		dic['Trace'] = 't' in arguments
		return nomarxiuhex, dic
	except:
		Debug(error('Error en la lectura del fitxer'))

def generaROM(arxiuhex):
	"""
	Utilitzant la classe IntelHex16bit del mòdul intelhex, converteix l'arxiu
	en format .hex amb el nom introduit com a argument a un objecte de la classe
	ProgramMemory que conté el programa ROM representat a l'arxiu.
	"""
	try:
		ih = IntelHex16bit()
		ih.loadhex(arxiuhex)
		l = list(ih.tobinarray())
		if len(l) == 0:
			rom = ProgramMemory(1)
			rom[0] = Word(0x9598)
		else:
			rom = ProgramMemory(len(l))
			for i in range(len(l)):
				rom[i] = Word(l[i])
		return rom
	except:
		Debug(error('Error en la lectura del fitxer'))

def simulacio(rom, opcions):
	"""
	Donada una ProgramMemory corresponent a un programa ROM i una configuració
	dels paràmetres per a la simulació, executa aquest programa i el simula.
	"""
	simulador = AvrMcu()
	simulador.set_prog(rom)
	Debug(success('Inici de la simulacio'))
	simulador.set_trace(opcions['Trace'])
	if opcions['Trace']:
		print '------'
		print 'Trace:'
		print '------'
	simulador.run()
	if opcions['ProgramDump']:
		print '--------------------'
		print 'Program memory dump:'
		print '--------------------'
		print simulador.dump_prog()
		print '--------------------'
	if opcions['RegisterDump']:
		print '--------------'
		print 'Register dump:'
		print '--------------'
		print simulador.dump_reg()
		print '--------------'
	if opcions['DataDump']:
		print '-----------------'
		print 'Data memory dump:'
		print '-----------------'
		print simulador.dump_dat()
		print '-----------------'

if __name__ == '__main__':
	arxiu, opcions = llegeixLiniaComandes()
	rom = generaROM(arxiu)
	simulacio(rom, opcions)
