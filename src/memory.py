#-*- encoding=utf-8 -*-

from avrexcep import *
from bitvec import *
from math import *			#Només necessari si el nombre de dígits en els bolcats és variable

class OutOfMemError(AVRException):
	"""
	Denota un accés a un banc de memòria amb una adreca inexistent.
	"""
	pass

class Memory(object):
	"""
	Classe abstracta que representa bancs de memòria.
	"""
	def __init__(self):
		"""
		Assigna False a _trace
		"""
		self._m = []
		self._trace = False

	def trace_on(self):
		"""
		Activa la funcionalitat de trace.
		"""
		Debug(success("Activada la funcionalitat de trace"))
		self._trace = True

	def trace_off(self):
		"""
		Desactiva la funcionalitat de trace.
		"""
		self._trace = False

	def __len__(self):
		"""
		Retorna el nombre de cel·les de la memòria.
		"""
		return len(self._m)

	def __repr__(self):
		"""
		Retorna un str que conté un bolcat del banc de memòria.
		"""
		infolist = []
		for k, v in enumerate(self._m):
			key = '0' * (int(ceil(log(len(self), 16))) - len(hex(k)[2:])) + hex(k)[2:].upper()     #El nombre necessari de dígits en hexadecimal
			#key = '0' * (4 - len(hex(k)[2:])) + hex(k)[2:].upper()                                #4 dígits en hexadecimal
			value = repr(v)
			infolist += [key + ': ' + value]
		return '\n'.join(infolist)

	def dump(self, f = 0, t = 5):
		"""
		Retorna un str que conté un bolcat del banc de memòria de les cel·les
		que estan en l’interval d’adreces [f, t).
		"""
		infolist = []
		for k, v in enumerate(self._m[f:t]):
			key = '0' * (int(ceil(log(len(self), 16))) - len(hex(k)[2:])) + hex(k)[2:].upper()     #El nombre necessari de dígits en hexadecimal
			#key = '0' * (4 - len(hex(k + f)[2:])) + hex(k + f)[2:].upper()                        #4 dígits en hexadecimal
			value = repr(v)
			infolist += [key + ': ' + value]
		if len(infolist) == 0:
			Debug(warning("El bolcat del banc de memoria ha resultat buit"))
		return '\n'.join(infolist)

	def __getitem__(self, addr):
		"""
		Retorna el contingut de la memòria a l'adreça addr.
		"""
		adr = '0' * (int(ceil(log(len(self), 16))) - len(hex(int(addr))[2:])) + hex(int(addr))[2:].upper()     #El nombre necessari de dígits en hexadecimal
		#adr = '0' * (4 - len(hex(int(addr))[2:])) + hex(int(addr))[2:].upper()								   #4 dígits en hexadecimal
		if int(addr) >= len(self):
			if self._trace:
				print 'Readfrom' + adr + 'outofrange'
			Debug(error("La lectura de la memoria no ha estat possible"))
			raise OutOfMemError
		valor = repr(self._m[addr])
		if self._trace:
			#adreça = '0' * (int(ceil(log(len(self), 16))) - len(hex(addr)[2:]))     #El nombre necessari de dígits en hexadecimal
			print 'Read  ' + valor + ' from ' + adr
		return self._m[addr]

	def __setitem__(self, addr, val):
		"""
		Modifica el contingut de la memòria a l'adreça addr.
		"""
		adr = '0' * (int(ceil(log(len(self), 16))) - len(hex(int(addr))[2:])) + hex(int(addr))[2:].upper()     #El nombre necessari de dígits en hexadecimal
		#adr = '0' * (4 - len(hex(int(addr))[2:])) + hex(int(addr))[2:].upper()								   #4 dígits en hexadecimal
		if int(addr) >= len(self):
			if self._trace:
				print 'Writeto' + adr + 'outofrange'
			Debug(error("L'escriptura de la memoria no ha estat possible"))
			raise OutOfMemError
		valor = repr(val)
		if self._trace:
			print 'Write ' + valor + ' to   ' + adr
		self._m[addr] = val

class ProgramMemory(Memory):
	"""
	Classe que representa bancs de memòria per emmagatzemar programes.
	"""
	def __init__(self, ncells = 1024):
		"""
		Inicialitza un objecte de la classe ProgramMemory amb ncells cel·les de mida Word.
		"""
		super(ProgramMemory, self).__init__()
		self._m = [Word() for i in range(ncells)]

class DataMemory(Memory):
	"""
	Classe que representa bancs de memòria per emmagatzemar dades.
	"""
	def __init__(self, ncells = 1024):
		"""
		Inicialitza un objecte de la classe DataMemory amb ncells cel·les de mida Byte.
		Si ncells és menor a 32, l'objecte tindrà 32 cel·les.
		"""
		super(DataMemory, self).__init__()
		if ncells < 32:
			ncells = 32
		self._m = [Byte() for i in range(ncells)]

	def dump_reg(self):
		"""
		Retorna un str que representa els registres continguts en el banc de memòria.
		"""
		infolist = []
		for k, v in enumerate(self._m[:32]):
			key = '0' * (2 - len(str(k))) + str(k)
			value = repr(v)
			infolist += ['R' + key + ': ' + value]
		valuex = repr(self._m[27]) + repr(self._m[26])
		valuey = repr(self._m[29]) + repr(self._m[28])
		valuez = repr(self._m[31]) + repr(self._m[30])
		infolist += ['X(R27:R26): ' + valuex]
		infolist += ['Y(R29:R28): ' + valuey]
		infolist += ['Z(R31:R30): ' + valuez]
		return '\n'.join(infolist)


if __name__ == '__main__':
	#Joc de proves de la subclasse DataMemory
	dmem = DataMemory(40)
	dmem.trace_on()
	print dmem
	print '----------------'
	print dmem.dump(20, 25)
	print '----------------'
	dmem[1023]
	dmem[1023] = Byte(8)
	dmem[5] = Byte(0xA)
	print dmem[5][3]
	print dmem[5][2]
	print '----------------'
	print dmem.dump(1020, 1024)
	print '----------------'
	print dmem.dump(0, 5)
	print '----------------'
	print dmem.dump_reg()
	print '----------------'
	print dmem.dump(999, 1005)
	print '----------------'
	Debug()
