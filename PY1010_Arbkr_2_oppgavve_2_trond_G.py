# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:06:13 2024

@author: Trond G
"""

"""Oppg 2) Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et
program som tar inn antall elever fra konsollen ved
antall_elever = int(input('Skriv inn antall elever:' ))
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive
svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe
5).
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan
sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?"""

#%%
import numpy as np
import math
Antall_pizza = int
Antall_pizza_kjop = int
Antall_pizza_hent = int


#%%
"""Hvor mange skal spise pizza?"""
antall_elever = int(input('Skriv inn antall elever:' ))
""""Hvor mye pizza spiser gjestene?"""
pizza_forbruk = 0.25

Antall_pizza = antall_elever*pizza_forbruk
Antall_pizza_kjop = round(Antall_pizza, 2)
Antall_pizza_hent = math.ceil(Antall_pizza)

#%%
if antall_elever <= 0:
    print("Det blir ingen fest, men du kan jo kjøpe 1 pizza til deg selv.")
else:
  print("Du trenger",Antall_pizza_kjop,"pizzaer til klassefesten din")
  print(",men du må kjøpe",Antall_pizza_hent,",og spise restene til lunsj i morgen.")