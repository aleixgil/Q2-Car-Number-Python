#-*- encoding=utf-8 -*-

from state import *
from avrexcep import *
from bitvec import *

class BreakException(AVRException):
    """
    S'utilitza per a aturar la simulació.
    """
    pass

class InstRunner(object):
    """
    Superclasse abstracta de totes les classes lligades a instruccions del simulador.
    """
    def __repr__(self):
        """
        Mètode abstracte redefinit a cada subclasse que retorna una cadena
        que representa la instrucció.
        """
    	pass

    def match(self, instr):
        """
        Mètode abstracte redefi nit a cada subclasse que retorna True si la classe
        de la instrucció pot executar l'ordre corresponent.
        """
    	pass

    def execute(self, instr, state):
        """
        Mètode abstracte redefinit a cada subclasse que executa l'ordre corresponent
        i modifica l'estat del MCU segons les especificacions de la instrucció.
        """
    	pass

class Add(InstRunner):
    """
    Suma registre-registre sense carry.
    """
    def __repr__(self):
        return 'ADD'

    def match(self, instr):
        opcode = instr.extract_field_u(0b1111110000000000)
        return opcode == 0b000011

    def execute(self, instr, state):
        r = instr.extract_field_u(0b1000001111)
        d = instr.extract_field_u(0b111110000)
        word = Word(int(state.data[d]) + int(state.data[r]))
        state.data[d] = word.lsb()
        state.flags[zero] = not int(state.data[d])
        state.flags[carry] = word[8]
        state.flags[neg] = state.data[d][7]
        state.pc += 1
        Debug(info('Instruccio ADD executada correctament'))

class Adc(InstRunner):
    """
    Suma registre-registre amb carry.
    """
    def __repr__(self):
    	return 'ADC'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111110000000000)
    	return opcode == 0b000111

    def execute(self, instr, state):
    	r = instr.extract_field_u(0b1000001111)
    	d = instr.extract_field_u(0b111110000)
    	word = Word(int(state.data[d]) + int(state.data[r]) + int(state.flags[carry]))
    	state.data[d] = word.lsb()
    	state.flags[zero] = not int(state.data[d])
    	state.flags[carry] = word[8]
    	state.flags[neg] = state.data[d][7]
    	state.pc += 1
        Debug(info('Instruccio ADC executada correctament'))

class Sub(InstRunner):
    """
    Resta registre-registre sense carry.
    """
    def __repr__(self):
    	return 'SUB'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111110000000000)
    	return opcode == 0b000110

    def execute(self, instr, state):
    	r = instr.extract_field_u(0b1000001111)
    	d = instr.extract_field_u(0b111110000)
        state.flags[carry] = (abs(int(state.data[d]) < abs(int(state.data[r]))))
    	word = Word(int(state.data[d]) - int(state.data[r]))
    	state.data[d] = word.lsb()
    	state.flags[zero] = not int(state.data[d])
    	state.flags[neg] = state.data[d][7]
    	state.pc += 1
        Debug(info('Instruccio SUB executada correctament'))

class Subi(InstRunner):
    """
    Resta registre-constant sense carry.
    """
    def __repr__(self):
    	return 'SUBI'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111000000000000)
    	return opcode == 0b0101

    def execute(self, instr, state):
    	k = instr.extract_field_u(0b111100001111)
    	d = instr.extract_field_u(0b11110000)
    	state.flags[carry] = (abs(int(state.data[d + 16]) < k))
    	word = Word(int(state.data[d + 16]) - k)
    	state.data[d + 16] = word.lsb()
    	state.flags[zero] = not int(state.data[d + 16])
    	state.flags[neg] = state.data[d + 16][7]
    	state.pc += 1
        Debug(info('Instruccio SUBI executada correctament'))

class And(InstRunner):
    """
    And registre-registre.
    """
    def __repr__(self):
    	return 'AND'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111110000000000)
    	return opcode == 0b001000

    def execute(self, instr, state):
    	r = instr.extract_field_u(0b1000001111)
    	d = instr.extract_field_u(0b111110000)
    	byte = state.data[d] & state.data[r]
    	state.data[d] = byte
    	state.flags[zero] = not int(state.data[d])
    	state.flags[neg] = state.data[d][7]
    	state.pc += 1
        Debug(info('Instruccio AND executada correctament'))

class Or(InstRunner):
    """
    Or registre-registre.
    """
    def __repr__(self):
    	return 'OR'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111110000000000)
    	return opcode == 0b001010

    def execute(self, instr, state):
    	r = instr.extract_field_u(0b1000001111)
    	d = instr.extract_field_u(0b111110000)
    	byte = state.data[d] | state.data[r]
    	state.data[d] = byte
    	state.flags[zero] = not int(state.data[d])
    	state.flags[neg] = state.data[d][7]
    	state.pc += 1
        Debug(info('Instruccio OR executada correctament'))

class Eor(InstRunner):
    """
    Or exclusiva registre-registre.
    """
    def __repr__(self):
    	return 'EOR'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111110000000000)
    	return opcode == 0b001001

    def execute(self, instr, state):
    	r = instr.extract_field_u(0b1000001111)
    	d = instr.extract_field_u(0b111110000)
    	byte = state.data[d] ^ state.data[r]
    	state.data[d] = byte
    	state.flags[zero] = not int(state.data[d])
    	state.flags[neg] = state.data[d][7]
    	state.pc += 1
        Debug(info('Instruccio EOR executada correctament'))

class Lsr(InstRunner):
    """
    Desplaçament dreta registre.
    """
    def __repr__(self):
    	return 'LSR'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111111000001111)
    	return opcode == 0b10010100110

    def execute(self, instr, state):
    	d = instr.extract_field_u(0b111110000)
    	state.flags[carry] = state.data[d][0]
    	state.data[d] = state.data[d] >> 1
    	state.flags[zero] = not int(state.data[d])
    	state.flags[neg] = 0
    	state.pc += 1
        Debug(info('Instruccio LSR executada correctament'))

class Mov(InstRunner):
    """
    Còpia registre-registre.
    """
    def __repr__(self):
    	return 'MOV'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111110000000000)
    	return opcode == 0b001011

    def execute(self, instr, state):
    	r = instr.extract_field_u(0b1000001111)
    	d = instr.extract_field_u(0b111110000)
    	byte = Byte(int(state.data[r]))
    	state.data[d] =  byte
    	state.pc += 1
        Debug(info('Instruccio MOV executada correctament'))

class Ldi(InstRunner):
    """
    Assigna valor a registre.
    """
    def __repr__(self):
    	return 'LDI'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111000000000000)
    	return opcode == 0b1110

    def execute(self, instr, state):
    	k = instr.extract_field_u(0b111100001111)
    	d = instr.extract_field_u(0b11110000)
    	byte = Byte(k)
    	state.data[d + 16] = byte
    	state.pc += 1
        Debug(info('Instruccio LDI executada correctament'))

class Sts(InstRunner):
    """
    Còpia registre a memòria.
    """
    def __repr__(self):
    	return 'STS'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111111000001111)
    	return opcode == 0b10010010000

    def execute(self, instr, instr2, state):
    	k = instr2.extract_field_u(0b1111111111111111)
    	addr = k
    	r = instr.extract_field_u(0b111110000)
    	byte = Byte(int(state.data[r]))
    	state.data[addr] = byte
    	state.pc += 2
        Debug(info('Instruccio STS executada correctament'))

class Lds(InstRunner):
    """
    Còpia memòria a registre.
    """
    def __repr__(self):
    	return 'LDS'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111111000001111)
    	return opcode == 0b10010000000

    def execute(self, instr, instr2, state):
    	k = instr2.extract_field_u(0b1111111111111111)
        addr = k
    	d = instr.extract_field_u(0b111110000)
    	byte = Byte(int(state.data[addr]))
    	state.data[d] = byte
    	state.pc += 2
        Debug(info('Instruccio LDS executada correctament'))

class Rjmp(InstRunner):
    """
    Salt relatiu a una nova instrucció.
    """
    def __repr__(self):
    	return 'RJMP'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111000000000000)
    	return opcode == 0b1100

    def execute(self, instr, state):
    	k = instr.extract_field_s(0b111111111111)
    	state.pc += k + 1
        Debug(info('Instruccio RJMP executada correctament'))

class Brbs(InstRunner):
    """
    Salta a adreça de programa si cert bit de FLAGS és 1.
    """
    def __repr__(self):
    	return 'BRBS'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111110000000000)
    	return opcode == 0b111100

    def execute(self, instr, state):
    	k = instr.extract_field_s(0b0000001111111000)
    	s = instr.extract_field_u(0b0000000000000111)
    	if state.flags[s]:
    		state.pc += k
    	state.pc += 1
        Debug(info('Instruccio BRBS executada correctament'))

class Brbc(InstRunner):
    """
    Salta a adreça de programa si cert bit de FLAGS és 0.
    """
    def __repr__(self):
    	return 'BRBC'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111110000000000)
    	return opcode == 0b111101

    def execute(self, instr, state):
    	k = instr.extract_field_s(0b0000001111111000)
    	s = instr.extract_field_u(0b0000000000000111)
    	if not state.flags[s]:
    		state.pc += k
    	state.pc += 1
        Debug(info('Instruccio BRBC executada correctament'))

class Nop(InstRunner):
    """
    No fa res. És la instrucció nul·la.
    """
    def __repr__(self):
    	return 'NOP'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111111111111111)
    	return opcode == 0

    def execute(self, instr, state):
    	state.pc += 1
        Debug(info('Instruccio NOP executada correctament'))

class Break(InstRunner):
    """
    Atura la simulació i acaba l'execució del programa simulador.
    """
    def __repr__(self):
    	return 'BREAK'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111111111111111)
    	return opcode == 0b1001010110011000

    def execute(self, instr, state):
        Debug(info('Instruccio BREAK executada correctament'))
    	raise BreakException

class In(InstRunner):
    """
    Quan s'aplica al port 0x0, llegeix un caràcter del teclat.
    """
    def __repr__(self):
    	return 'IN'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111100000000000)
    	return opcode == 0b10110

    def execute(self, instr, state):
    	a = instr.extract_field_u(0b11000001111)
    	d = instr.extract_field_u(0b111110000)
    	if a == 0:
    		try:
    			byte = Byte(ord(raw_input('Introdueix un caràcter: ')))
    			state.data[d] = byte
    		except:
    			pass
    	state.pc += 1
        Debug(info('Instruccio IN executada correctament'))

class Out(InstRunner):
    """
    S'usa per escriure per la pantalla. Quan el port és:
    0x0: Escriu el valor del registre corresponent pel terminal en base 10.
    0x1: Escriu el valor del registre corresponent pel terminal en base 16.
    0x2: Escriu el valor del registre assumint que correspon a la codificació UTF d'un caràcter.
    """
    def __repr__(self):
    	return 'OUT'

    def match(self, instr):
    	opcode = instr.extract_field_u(0b1111100000000000)
    	return opcode == 0b10111

    def execute(self, instr, state):
    	a = instr.extract_field_u(0b11000001111)
    	r = instr.extract_field_u(0b111110000)
    	if a == 0:
    		print int(state.data[r])
    	elif a == 1:
    		print state.data[r]
    	elif a == 2:
    		print chr(int(state.data[r]))
    	state.pc += 1
        Debug(info('Instruccio OUT executada correctament'))

if __name__ == '__main__':
    estat = State()
    estat.data[3] = Byte(1)
    estat.data[10] = Byte(3)
    estat.data[26] = Byte(250)
    estat.data[27] = Byte(6)
    print estat.dump_reg()
    print '------------'
    instrun = Add()
    instruccio = Word(0b0000110000111010)
    print instrun.match(instruccio)
    print '------------'
    instrun.execute(instruccio, estat)
    print estat.dump_reg()
    print '------------'
    instruccio = Word(0b0000110000000000)
    instrun.execute(instruccio, estat)
    print estat.dump_reg()
    print '------------'
    instruccio = Word(0b0000111110111010)
    instrun.execute(instruccio, estat)
    print estat.dump_reg()
    print '------------'
    instrun2 = Adc()
    instruccio = Word(0b0001110010101010)
    instrun2.execute(instruccio, estat)
    print estat.dump_reg()
