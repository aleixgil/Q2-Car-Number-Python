#-*- encoding=utf-8 -*-

from time import *
from state import *
from repertoir import *

class AvrMcu(object):
    """
    Les instàncies de la classe AvrMcu són simuladors de l'MCU AVR.
    Executa un programa escrit en assemblador de l'AVR.
    """
    def __init__(self):
        """
        Inicialitza el simulador, fent un reset de l'estat i inicialitzant el repertori d'instruccions amb les
        instàncies d'InstRunner corresponents.
        """
        self._s = State()
        self._rep = Repertoir([Add(), Adc(), Sub(), Subi(), And(), Or(), Eor(), Lsr(), Mov(), Ldi(), Sts(), Lds(), Rjmp(), Brbs(), Brbc(), Nop(), Break(), In(), Out()])

    def reset(self):
        """
        Fa un reset de l'estat deixant-lo de la mateixa forma que el mètode constructor.
        """
        self._s = State()

    def set_prog(self,p):
        """
        El mètode instal·la el programa p, que és una llista d'enters que representen un programa
        en llenguatge màquina de l’AVR, en la memòria de programa del simulador a partir
        de l'adreça 0000.
        """
        self._s.prog = p

    def dump_reg(self):
        """
        Retorna un string que correspon amb un bolcat dels registres del simulador.
        """
        return self._s.dump_reg()

    def dump_dat(self):
        """
        Retorna un str que representa un bolcat de la memòria de dades del simulador.
        """
        return self._s.dump_dat()

    def dump_prog(self):
        """
        Retorna un str que representa un bolcat de la memòria de programa del simulador.
        """
        return self._s.dump_prog()

    def run(self):
        """
        És el mètode principal del simulador.
        Obté la instrucció indicada pel PC, busca un InstRunner que pugui executar
        aquesta instrucció i l'executa.
        """
        try:
            while True:
                try:
                    instruction = self._s.prog[self._s.pc]
                    instruction2 = Word()
                except OutOfMemError:
                    Debug(warning('El programa ha arribat al seu final sense una instruccio BREAK, es torna a comencar'))
                    self._s.pc = Word()
                    instruction = self._s.prog[self._s.pc]
                try:
                    runner = self._rep.find(instruction)
                    if type(runner) == type(Lds()) or type(runner) == type(Sts()):
                        instruction2 = self._s.prog[self._s.pc + 1]
                        runner.execute(instruction, instruction2, self._s)
                    else:
                        runner.execute(instruction, self._s)
                except UnknownCodeError:
                    Debug(error('La instruccio a executar es desconeguda'))
                    self._s.pc += 1
        except BreakException:
            Debug(success("Fi de la simulacio"))

    def set_trace(self, t):
        """
        Quan s'invoca amb t = True activa el mode trace de la memòria de dades. Si s'activa
        amb t = False es desactiva el mode.
        """
        if t:
            self._s.data.trace_on()
        else:
            self._s.data.trace_off()

if __name__ == '__main__':
    simulador = AvrMcu()
    Debug()
