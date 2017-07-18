; Compta fins al nombre corresponent al codi del caràcter ASCII introduït
; LLegeix un caràcter del teclat i en guarda el codi al registre 16
EOR r17, r17
IN r16, 0
REPEAT1:
; Augmenta el valor del registre 17 en una unitat	
SUBI r17, -1
; Imprimeix per pantalla el valor decimal contingut al registre 17
OUT 0, r17
; Copia el valor del registre 17 al registre 18 i li resta el valor del codi
MOV r18, r17
SUB r18, r16
; Mentre el valor del registre 18 (o del 17) sigui diferent del codi, continua comptant
BRBC 1, REPEAT1
; Els registres queden de la següent manera: r16:x, r17:x, r18:0
; On x és el codi ASCII del caràcter introduït
BREAK
	
	
