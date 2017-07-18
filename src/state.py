#-*- encoding=utf-8 -*-

from memory import *

carry = 0
zero = 1
neg = 2

class State(object):
    """
    Classe que representa l'estat d'una MCU.
    """
    def __init__(self, data = 128, prog = 128):
        """
        Inicialitza l'estat d'una MCU amb les mides de les memòries indicades.
        """
        self.prog = ProgramMemory(prog)
        self.data = DataMemory(data)
        self.pc = Word()
        self.flags = Byte()

    def dump_dat(self):
        """
        Retorna un str que conté un bolcat de la memòria de dades.
        """
        r = repr(self.data)
        return r

    def dump_prog(self):
        """
        Retorna un str que conté un bolcat de la memòria de programa.
        """
        r = repr(self.prog)
        return r

    def dump_reg(self):
        """
        Retorna un str que conté els registres de l'estat, el PC i els flags.
        """
        infolist = [self.data.dump_reg()]
        infolist += ['PC: ' + repr(self.pc)]
        infolist += ['CARRY: ' + str(int(self.flags[carry])) + ' | ZERO: ' + str(int(self.flags[zero])) + ' | NEG: ' + str(int(self.flags[neg]))]
        return '\n'.join(infolist)

if __name__ == '__main__':
    estat = State()
    print estat.dump_dat()
    print '----------'
    print estat.dump_prog()
    print '----------'
    print estat.dump_reg()
    print '----------'
    estat.data[126] = Byte(255)
    estat.flags[carry] = True
    print estat.dump_reg()
    print '----------'
    Debug()
