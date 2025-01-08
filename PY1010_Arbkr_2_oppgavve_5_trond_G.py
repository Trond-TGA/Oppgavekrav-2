# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:23:22 2024

@author: Trond G
"""
"""
Oppg 5) Lag et program med en funksjon som tar a og b som inn-argumenter og som så
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en
halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
tekst.
"""

import numpy as np
from numpy import radians,sin,cos,pi,linspace
import matplotlib.pyplot as plt
import math
#%% Konstanter og variabler

side_a = float()
side_b = float()
Arealhelsirkel = float()
Omkrsirkel = float()

#%% Henter nn side a og side b

side_a = float(input("Skriv inn lengden på side a:", ))
side_b = float(input("Skriv in lengden på side b:", ))

#%% Finner lengden på hypotinusen til trekanten
Hypotinus = math.sqrt((side_a)**2+(side_b)**2)



#%% beregner areal og omkrets av trekant og sirkel

Omkr_sirkel = 2*pi*(side_a/2)

Areal_helsirkel = (side_a**2)*pi

Areal_trekant = side_a*side_b/2




#beregner samme som v_grad men nå som liste -(forsøk på ekte brøk)


plt.close('all')

v_rad = 180*np.pi/180

Vinkel = math.tan( side_a / side_b )


arc_angles = linspace(0 * pi, v_rad, 180)
arc_xs =side_a/2 * cos(arc_angles)
arc_ys =side_a/2 * sin(arc_angles)
plt.plot(arc_xs, arc_ys, color = 'red', lw = 1)


# tegner diameter blå horisontalt
plt.plot( side_a/2, 0, marker= 'o', color = 'blue')
plt.plot(-side_a/2, 0, marker= 'o', color = 'blue')

# plotter blå strek som er diameter
plt.plot([-side_a/2,side_a/2],[0,0], marker= 'o', color = 'blue', lw = 1)

# plotter line fra høyre side av sirkel og ned til bunnpunkt trekant
plt.plot([-side_a/2,-side_a/2],[0,-side_b], marker= 'o', color = 'yellow', lw = 1)

#plotter line fra bunnpunkt og opp til høyre side av sirkelen
plt.plot([side_a/2,-side_a/2],[0,-side_b], marker= 'o', color = 'green', lw = 1)
# plotter inn tekst på hypotinusen

plt.gca().annotate('Hypotinus', xy =(-0.3,-side_b/2), xycoords= 'data',rotation = Vinkel, fontsize = 8)


plt.gca().set_aspect('equal')
plt.show()
