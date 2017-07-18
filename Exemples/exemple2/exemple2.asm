; Carrega dos valors als registres 16 i 17, amb una instrucció nul·la entremig
LDI R16, 0xff
NOP
LDI R17, 1
; Suma el valor guardat al registre 17 amb ell mateix
ADD R17, R17
; Copia el valor del registre 17 al registre 0
MOV R0, R17
; Fa una AND entre el valor del registre 0 i el 16
AND R0, R16
; Els registres queden de la següent manera: r0:2, r16:0xff i r17:2
BREAK
