.. Projecte TeProg: SimulAVR documentation master file, created by
   sphinx-quickstart on Wed Jun  1 11:08:50 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Simulador AVR - TecPro - UPC
=====================================================

Simulador AVR de Tecnologia de Programació realitzat per:

-   Èrik Campobadal Forés
-   Pau De Las Heras
-   Aleix Gil
-   Gemma Rosell
-   Roger Solans

==========
Comentaris
==========

A continuació tenim la documentació del projecte de curs consistent en un simulador
d'AVR des del punt de vista del software, el desenvolupament del qual s'ha dut a terme
seguint el guió proporcionat a l'assignatura de Tecnologia de Programació.

Cal indicar que pel que fa als doctests dels mètodes corresponents, que hem optat per
només incloure aquells que pertanyen al mòdul BitVec, ja que per la seva naturalesa
resulten molt més il·lustratius i rellevants que en la resta de mòduls, on els mètodes
comporten un major grau de complexitat i interrelació, així com el retorn d'objectes
que fan de mal mostrar, ja sigui pel seu tipus o per la seva extensió.

Hem considerat, per tant, que la millor manera de mostrar el funcionament correcte de
la resta de mòduls és adjuntant a la documentació un seguit d'arxius que inclouen
diversos programes que el simulador pot executar degudament, demostrant que aquest
és capaç de dur a terme totes les accions detallades en l'enunciat del projecte.


.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: Simulador AVR

    Introducció <self>
    BitVec
    BitVecTest
    Memory
    State
    Instruction
    Repertoir
    AvrMcu
    AVRException
    SimAvr
