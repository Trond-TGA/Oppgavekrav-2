# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:23:45 2024

@author: Trond G
"""
"""
Oppg 6) Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10].
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet
[-10,10].
Selv om Arbeidskrav 2 er en individuell innlevering kan du selvsagt diskutere med kollegaer
og søke hjelp fra våre studentassistenter underveis.
"""
#%% Henter inn nødvendige grunnprogrammer og biblioteker
import numpy as np
import matplotlib.pyplot as plt



#%% Definisjopn av formel og rammer for plott

def f(x):
    return -x**2 - 5

x = np.linspace(-10, 10, 200)




#%% Plotting ar resultat

plt.close('all')
fig = plt.figure()
plt.plot(x,f(x), color = 'red')
plt.legend(labels =('f(x)'))
plt.xlabel('x akse')
plt.plot()

#%% legger til rutenett på plott
plt.grid()
plt.show()

