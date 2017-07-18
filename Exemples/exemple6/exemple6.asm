; Imprimeix per pantalla la paraula OK
; Per a dos registres consecutius i dues posicions de memòria consecutives, es carrega el
; valor del registre a la posició de memòria corresponent
LDI r20, 79
STS 0x50, r20
LDI r21, 75
STS 0x51, r21
; Per a les dues posicions de memòria ocupades, es copia el seu valor a dos altres registres
; consecutius i s'imprimeix el caràcter de codi ASCII corresponent al valor
LDS r22, 0x50
OUT 2, r22
LDS r23, 0x51
OUT 2, r23
; Els registres queden de la següent manera: r20:79, r21:75, r22: 79, r23:75
BREAK


