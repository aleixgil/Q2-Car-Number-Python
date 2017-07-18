; Escriu l’abecedari
; Neteja els registres 0 i 18.
EOR R0, R0 ; R0 = 0
EOR R18, R18 ; R18 = 0
LAB1:
; Carrega el nombre d'iteracions, 26, al registre 19
LDI R19, 26
; Carrega la base del codi ASCII al registre 17
LDI R17, 65
; Suma el valor del registre 0 al del registre 17
ADC R17, R0
; Escriu el caracter de codi ASCII guardat al registre 17 per pantalla
OUT 2, R17
; Augmentem en una unitat el valor guardat al registre 18 i el copiem al registre 0
SUBI R18, -1
MOV R0, R18
; Mentre el valor del registre 0 sigui diferent al nombre d'iteracions, repetim el procés
SUB R19, R0
BRBC 1, LAB1
; Els registres queden de la següent manera: r0:0x1A, r17:0x5A, r18:0x1A, r19:0, carry:0, zero:1, neg:0
BREAK
