#-*- encoding=utf-8 -*-

from debug import *

class BitVector(object):
    """
	Classe abstracta que representa paraules binàries
    """
    def __init__(self, w = 0):
        """
        Permet inicialitzar una paraula a partir d'un enter amb signe.
        """
        if w >= 0:
            t_w = w
        else:
            aux = bin(abs(w) - 1)[2:]
            t_w = ''
            for p, i in enumerate(aux):
                t_w += str(1 - int(i))
            if len(t_w) < len(self):
                t_w = '1' * (len(self) - len(t_w)) + t_w
            t_w = int(t_w, 2)
        if len(bin(int(t_w))) >= len(self) + 2:
            integer = bin(int(t_w))[-len(self):]
        else:
            integer = bin(int(t_w))[2:]
        self._w = int(integer, 2)


    def extract_field_u(self, mask):
        """
        Permet l'extracció d'un camp de la paraula com a enter sense signe.
        """
        if len(bin(mask)) >= len(self) + 2:
            t_mask = '0b' + bin(mask)[-len(self):]
        else:
            t_mask = '0b' + '0' * (len(self) - len(bin(mask)[2:])) + bin(mask)[2:]
        if len(bin(self._w)) >= len(self) + 2:
            aux = '0b' + bin(self._w)[-len(self):]
        else:
            aux = '0b' + '0' * (len(self) - len(bin(self._w)[2:])) + bin(self._w)[2:]
        w = ''
        for index, value in enumerate(t_mask):
            if value == '1':
                w += aux[index]
        return int(w, 2)

    def extract_field_s(self, mask):
        """
        Permet l'extracció d'un camp de la paraula com a enter amb signe.
        """
        if len(bin(mask)) >= len(self) + 2:
            t_mask = '0b' + bin(mask)[-len(self):]
        else:
            t_mask = '0b' + '0' * (len(self) - len(bin(mask)[2:])) + bin(mask)[2:]
        if len(bin(self._w)) >= len(self) + 2:
            aux = '0b' + bin(self._w)[-len(self):]
        else:
            aux = '0b' + '0' * (len(self) - len(bin(self._w)[2:])) + bin(self._w)[2:]
        w = ''
        for index, value in enumerate(t_mask):
            if value == '1':
                w += aux[index]
        if w.startswith('0'):
            return int(w, 2)
        else:
            t_w = ''
            for p, i in enumerate(w):
                t_w += str(1 - int(i))
            return - (int(t_w, 2) + 1)

    def __int__(self):
        """
        Retorna el valor corresponent a la paraula com a enter sense signe.
        """
        return self._w

    def __index__(self):
        """
        Retorna l'índex correspont al valor de la paraula com a enter sense signe.
        """
        return int(self)

    def __repr__(self):
        """
        Retorna la representació en hexadecimal del valor de la paraula en els dígits corresponents.
        """
        h = hex(self._w)[2:]
        return '0' * (len(self) / 4 - len(h)) + h.upper()

    def __add__(self, o):
        """
        Permet la suma de paraules.
        """
        classe = type(self)
        return classe(int(self) + int(o))

    def __sub__(self, o):
        """
        Permet la resta de paraules.
        """
        classe = type(self)
        return classe(int(self) - int(o))

    def __and__(self, o):
        """
        Permet l'AND lògic bit a bit de paraules.
        """
        classe = type(self)
        return classe(int(self) & int(o))

    def __or__(self, o):
        """
        Permet l'OR lògic bit a bit de paraules.
        """
        classe = type(self)
        return classe(int(self) | int(o))


    def __xor__(self, o):
        """
        Permet l'XOR lògic bit a bit de paraules.
        """
        classe = type(self)
        return classe(int(self) ^ int(o))

    def __invert__(self):
        """
        Permet la inversió lògica bit a bit de paraules.
        """
        classe = type(self)
        return classe(~ int(self))

    def __lshift__(self, i):
        """
        Permet la rotació a l'esquerra de paraules.
        """
        if i >= len(self):
            raise IndexError
        else:
            classe = type(self)
            return classe(int(self) << i)


    def __rshift__(self, i):
        """
        Permet la rotació a la dreta de paraules.
        """
        if i >= len(self):
            raise IndexError
        else:
            classe = type(self)
            return classe(int(self) >> i)

    def __eq__(self, o):
        """
        Permet l'operació d'igualtat de paraules.
        """
        if isinstance(o, BitVector):
            length = min([len(self), len(o)])
            return bin(int(self))[- length:] == bin(int(o))[- length:]
        else:
            if o >= 0:
                return int(self) == o
            else:
                if len(bin(self._w)) >= len(self) + 2:
                    aux = bin(self._w)[-len(self):]
                else:
                    aux = '0' * (len(self) - len(bin(self._w)[2:])) + bin(self._w)[2:]
                t_w = ''
                for p, i in enumerate(aux):
                    t_w += str(1 - int(i))
                return - (int(t_w, 2) + 1) == o

    def __ne__(self, o):
        """
        Permet l'operació de desigualtat de paraules.
        """
        return not (self == o)

    def __getitem__(self, i):
        """
        Permet l'accés de lectura als bits d'una paraula individualment.
        """
        try:
            if len(bin(int(self))) < len(self) + 2:
                string = '0' * (len(self) - len(bin(int(self))[2:])) + bin(int(self))[2:]
            else:
                string = bin(int(self))[2:]
            if i >= len(string):
                raise IndexError
            return int(string[- (i + 1)]) == True
        except IndexError:
            Debug(error("La lectura de la paraula binaria no ha estat possible"))
            #raise KeyError

    def __setitem__(self, i, v):
        """
        Permet l'accés d'escriptura als bits d'una paraula individualment.
        """
        try:
            if len(bin(int(self))) < len(self) + 2:
                string = '0' * (len(self) - len(bin(int(self))[2:])) + bin(int(self))[2:]
            else:
                string = bin(int(self))[2:]
            if i >= len(string):
                raise IndexError
            aux = ''.join([str(c) if p != ((len(string) - (i + 1))) else str(int(v)) for p, c in enumerate(string)])
            self._w = int(aux, 2)
        except IndexError:
            Debug(error("L'escriptura de la paraula binaria no ha estat possible"))
            #raise KeyError

class Byte(BitVector):
    """
    Classe que representa paraules binàries de mida 8.
    """
    def __len__(self):
        """
        Retorna la llargada d'un byte, 8.
        >>> print len(Byte(4))
        8
        """
        return 8

    def concat(self, b):
        """
        Permet concatenar bytes per a construir paraules.
        """
        w = int(repr(self) + repr(b), 16)
        return Word(w)

class Word(BitVector):
    """
    Classe que representa paraules binàries de mida 16.
    """
    def __len__(self):
        """
        Retorna la llargada d'una paraula, 16.
        """
        return 16

    def lsb(self):
        """
        Permet obtenir el byte de menor pes d'una paraula.
        """
        w = int(repr(self)[2:], 16)
        return Byte(w)

    def msb(self):
        """
        Permet obtenir el byte de major pes d'una paraula.
        """
        w = int(repr(self)[:2], 16)
        return Byte(w)

if __name__ == "__main__":
    c = Byte(0b11000110)
    print int(c)
    print repr(c)
    print c.extract_field_u(0b00110011)
    print c.extract_field_u(0b10110011)
    print c.extract_field_s(0b10110011)
    print '----------'
    d = Word(0b11000110)
    print int(d)
    print repr(d)
    print d.extract_field_u(0b00110011)
    print d.extract_field_u(0b10110011)
    print d.extract_field_s(0b10110011)
    print '----------'
    print c == d
    print c != d
    print '----------'
    print c[100000]
    print d[0]
    print '----------'
    c[0] = 1
    print c
    d[0] = 1
    print d
    print '----------'
    print Byte(-166).extract_field_s(51)
    print Byte(-1)
    Debug()
