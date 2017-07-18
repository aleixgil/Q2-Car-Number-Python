Mòdul BitVec
============

class BitVector(object):
    """
	  Classe abstracta que representa paraules binàries
    """
    def __init__(self, w = 0):
        """
        Permet inicialitzar una paraula a partir d'un enter amb signe.
        """

    def extract_field_u(self, mask):
        """
        Permet l'extracció d'un camp de la paraula com a enter sense signe.
        >>> Byte(166).extract_field_u(51)
        10
        """


    def extract_field_s(self, mask):
        """
        Permet l'extracció d'un camp de la paraula com a enter amb signe.
        >>> Byte(-166).extract_field_s(51)
        6
        >>> Byte(166).extract_field_s(51)
        -6
        """


    def __int__(self):
        """
        Retorna el valor corresponent a la paraula com a enter sense signe.
        >>> int(Byte(7))
        7
        >>> int(Byte(0b1011))
        11
        >>> int(Word(403))
        403
        """

    def __index__(self):
        """
        Retorna l'índex correspont al valor de la paraula com a enter sense signe.
        """


    def __repr__(self):
        """
        Retorna la representació en hexadecimal del valor de la paraula en els dígits corresponents.
        >>> print Byte(10)
        0A
        >>> print Word(10)
        000A
        >>> print Byte(1)
        01
        >>> print Byte(15)
        0F
        >>> print Byte(-1)
        FF
        >>> print Byte(403)
        93
        """

    def __add__(self, o):
        """
        Permet la suma de paraules.
        >>> Byte(2) + Byte(12)
        0E
        >>> Byte(12) + 2
        0E
        """

    def __sub__(self, o):
        """
        Permet la resta de paraules.
        >>> Byte(12) - Byte(2)
        0A
        >>> Byte(12) - 2
        0A
        """


    def __and__(self, o):
        """
        Permet l'AND lògic bit a bit de paraules.
        >>> Byte(8) & Byte(8)
        08
        >>> Byte(7) & Byte(0b0010)
        02
        >>> Byte(0xff) & Byte(0b1011)
        0B
        """

    def __or__(self, o):
        """
        Permet l'OR lògic bit a bit de paraules.
        >>> Byte(24) | Byte(8)
        18
        >>> Byte(7) | Byte(0b0010)
        07
        >>> Byte(3) | Byte(4)
        07
        """


    def __xor__(self, o):
        """
        Permet l'XOR lògic bit a bit de paraules.
        >>> Byte(24) ^ Byte(8)
        10
        >>> Byte(0xff) ^ Byte(0b1011)
        F4
        """

    def __invert__(self):
        """
        Permet la inversió lògica bit a bit de paraules.
        >>> ~ Byte(24)
        E7
        >>> ~ Byte(0xf0)
        0F
        >>> print ~ Byte(0b101010)
        D5
        """

    def __lshift__(self, i):
        """
        Permet la rotació a l'esquerra de paraules.
        >>> Byte(1) << 4
        10
        >>> Byte(0xfe) << 3
        F0
        """

    def __rshift__(self, i):
        """
        Permet la rotació a la dreta de paraules.
        >>> Byte(0xff) >> 4
        0F
        """

    def __eq__(self, o):
        """
        Permet l'operació d'igualtat de paraules.
        >>> Byte(2) == 2
        True
        >>> Byte(8) == Byte(8)
        True
        >>> Byte(12) == -12
        False
        >>> Byte(244) == -12
        True
        """

    def __ne__(self, o):
        """
        Permet l'operació de desigualtat de paraules.
        >>> Byte(2) != 2
        False
        >>> Byte(8) != Byte(8)
        False
        >>> Byte(12) != -12
        True
        >>> Byte(244) != -12
        False
        """

    def __getitem__(self, i):
        """
        Permet l'accés de lectura als bits d'una paraula individualment.
        >>> Byte(2)[0]
        False
        >>> Byte(2)[1]
        True
        >>> Byte(10)[7]
        False
        """

    def __setitem__(self, i, v):
        """
        Permet l'accés d'escriptura als bits d'una paraula individualment.
        >>> a = Byte(2)
        >>> a[1] = 0
        >>> print a
        00
        >>> b = Byte(4)
        >>> b[0] = 1
        >>> print b
        05
        """

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

    def concat(self, b):
        """
        Permet concatenar bytes per a construir paraules.
        >>> b = Byte(255)
        >>> c = Byte(0)
        >>> d = b.concat(c)
        >>> print d
        FF00
        """

class Word(BitVector):
    """
    Classe que representa paraules binàries de mida 16.
    """
    def __len__(self):
        """
        Retorna la llargada d'una paraula, 16.
        >>> print len(Word(24))
        16
        """

    def lsb(self):
        """
        Permet obtenir el byte de menor pes d'una paraula.
        >>> Word(255).lsb()
        FF
        >>> Word(65535).lsb()
        FF
        """

    def msb(self):
        """
        Permet obtenir el byte de major pes d'una paraula.
        >>> Word(255).msb()
        00
        >>> Word(65535).msb()
        FF
        """
