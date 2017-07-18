=========================
Doctests del Mòdul BitVec
=========================

A continuació tenim els doctests dels mètodes de les classes que corresponen
al mòdul BitVec del nostre simulador d'AVR.

Comencem amb els mètodes d'extracció de camps que podem trobar a la superclasse
BitVector:

.. code-block:: python

    >>> Byte(166).extract_field_u(51)
    10
    >>> Byte(-166).extract_field_s(51)
    6
    >>> Byte(166).extract_field_s(51)
    -6

Observem que funcionen correctament, i també que és possible inicialitzar un objecte
de la classe BitVector o les seves subclasses a partir d'un enter positiu o també negatiu.

A continuació tenim els mètodes que permeten obtenir el valor enter corresponent
a una paraula binària o la seva representació en hexadecimal:

.. code-block:: python

    >>> int(Byte(7))
    7
    >>> int(Byte(0b1011))
    11
    >>> int(Word(403))
    403

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

Seguidament tenim els mètodes que permeten operacions lògiques i matemàtiques entre objectes
de les classes amb què treballem:

.. code-block:: python

    >>> Byte(2) + Byte(12)
    0E
    >>> Byte(12) + 2
    0E

    >>> Byte(12) - Byte(2)
    0A
    >>> Byte(12) - 2
    0A

    >>> Byte(8) & Byte(8)
    08
    >>> Byte(7) & Byte(0b0010)
    02
    >>> Byte(0xff) & Byte(0b1011)
    0B

    >>> Byte(24) | Byte(8)
    18
    >>> Byte(7) | Byte(0b0010)
    07
    >>> Byte(3) | Byte(4)
    07

    >>> Byte(24) ^ Byte(8)
    10
    >>> Byte(0xff) ^ Byte(0b1011)
    F4

    >>> ~ Byte(24)
    E7
    >>> ~ Byte(0xf0)
    0F
    >>> print ~ Byte(0b101010)
    D5

    >>> Byte(1) << 4
    10
    >>> Byte(0xfe) << 3
    F0

    >>> Byte(0xff) >> 4
    0F

    >>> Byte(2) == 2
    True
    >>> Byte(8) == Byte(8)
    True
    >>> Byte(12) == -12
    False
    >>> Byte(244) == -12
    True

    >>> Byte(2) != 2
    False
    >>> Byte(8) != Byte(8)
    False
    >>> Byte(12) != -12
    True
    >>> Byte(244) != -12
    False
    """

Havent comprovat el correcte funcionament dels operadors, observem ara que els mètodes
d'accés i escriptura de bits de paraules funcionen tal i com s'espera:

.. code-block:: python

    >>> Byte(2)[0]
    False
    >>> Byte(2)[1]
    True
    >>> Byte(10)[7]
    False

    >>> a = Byte(2)
    >>> a[1] = 0
    >>> print a
    00
    >>> a[1] = True
    >>> print a
    02
    >>> b = Byte(4)
    >>> b[0] = 1
    >>> print b
    05


Finalment passem als mètodes específics de les subclasses Byte i Word per
observar que el seu funcionament és correcte:

.. code-block:: python

    >>> print len(Byte(4))
    8
    >>> print len(Word(24))
    16

    >>> b = Byte(255)
    >>> c = Byte(0)
    >>> d = b.concat(c)
    >>> print d
    FF00

    >>> Word(255).lsb()
    FF
    >>> Word(65535).lsb()
    FF

    >>> Word(255).msb()
    00
    >>> Word(65535).msb()
    FF
