#!/usr/bin/python
#-*- encoding=utf-8 -*-

import easygui
import os
from simavr import *
from debug import *

def menu():
    Debug(green("Initializing Program..."))
    image = "logo.png"
    choices = ["Executar Programa", "Sortir"]
    title = "Mini AVR - TecPro - iTIC"
    while True:
        reply = easygui.buttonbox(image=image, choices=choices, title=title)
        accio(reply)

def accio(r):
    if r == 'Sortir':
        msg ="Vols Debug?"
        title = "Opcions AVR"
        choices = ["Si", "No"]
        reply = easygui.buttonbox(msg=msg, choices=choices, title=title)
        if reply == 'Si':
            Debug(yellow("Stopping Program..."))
            Debug()
        quit()
    elif r == "Executar Programa":
        f = ""
        wd = os.getcwd()
        while wd not in f:
            easygui.msgbox("Seleccioneu la localització del fitxer. El fitxer ha d'estar dins el directori actual.")
            try:
                f = easygui.fileopenbox()
            except:
                pass
        f = f.replace(wd, "")[1:]
        msg ="Seleccioni les opcions del AVR:"
        title = "Opcions AVR"
        choices = ["ProgramDump", "RegisterDump", "DataDump", "Trace"]
        choices_a = easygui.multchoicebox(msg, title, choices)
        dic = {}
        for i in choices:
            dic[i] = i in choices_a
        try:
            rom = generaROM(f)
            simulacio(rom, dic)
            easygui.msgbox("El programa s'ha executat correctament")
        except:
            easygui.exceptionbox()

if __name__ == '__main__':
    try:
        menu()
    except:
        quit()
