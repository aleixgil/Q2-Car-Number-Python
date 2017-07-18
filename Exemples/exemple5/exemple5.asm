; Compta fins a 15 en hexadecimal
; Carrega 15 al registre 20
LDI r20, 15
; Incrementa en 1 el valor del registre 17 i l'imprimeix en hexadecimal
SUBI r17, -1
OUT 1, r17
; Mentre el valor imprès és diferent a 15, el programa arriba al final i torna a començar
; Quan arriba a 15, el programa executa una ordre BREAK i s'acaba la simulació
; Els registres queden de la següent manera: r17:15, r20:0, zero:1,
; carry:1 (ja que restem tota l'estona -1, que sense signe en binari equivaldria a 255,
; de major valor absolut que els valors que pren el registre)
EOR r20, r17
BRBS 1, FINISH
BRBC 1, CONTINUE
FINISH:
BREAK
CONTINUE:
NOP
