; Carrega el valor 1 al registre 17 i el 254 al registre 16
LDI R17, 1
LDI R16, 254
LAB1:
; Suma al valor del registre 16 el del registre 17
ADC R16, R17
; Fins que el resultat de la suma no és zero (per tant quan la suma és 255 + 1 = 0x100) es repeteix
; el procés, ja que s'ignora el primer salt condicional i es compleix el segon.
BRBS 1, LAB2
RJMP LAB1
LAB2:
; Els registres queden de la següent manera: r16:0, r17:1, carry:1, zero:1
BREAK
