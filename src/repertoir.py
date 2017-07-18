#-*- encoding=utf-8 -*-

from avrexcep import *
from instruction import *

class UnknownCodeError(AVRException):
    """
    Denota que una ordre no pot ser exectuada per cap instrucció del repertori.
    """
    pass

class Repertoir(object):
    """
    Classe que representa el repertori d'instruccions que és capaç d'executar el simulador.
    """
    def __init__(self, li):
        """
        self._li és una llista d'instàncies d'InstRunner.
        """
        self._li = li

    def find(self, instr):
        """
        Retorna un objecte InstRunner capaç d'executar la instrucció instr(Word).
        """
        if len(self._li) == 0:
            Debug(warning("No hi ha cap InstRunner al repertori."))
        else:
            for i in self._li:
                if i.match(instr):
                    return i
            Debug(error("No hi ha cap InstRunner al repertori capac d'executar la instruccio."))
            raise UnknownCodeError

if __name__ == '__main__':
    r = Repertoir()
    Debug()
