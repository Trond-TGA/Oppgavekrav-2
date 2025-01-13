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
#%% Henter programpakker til prorgammet
import numpy as np
from numpy import radians,sin,cos,pi,linspace
import matplotlib.pyplot as plt
import math
#%% Konstanter og variabler

side_a = float()
side_b = float()
Areal_helsirkel = float()
Omkr_sirkel = float()

#%% Henter inn side a og side b

side_a = float(input("Skriv inn lengden på side A:", ))
side_b = float(input("Skriv in lengden på side B:", ))

#%% Finner lengden på hypotenusen til trekanten med Pytagoras setning a*2 +b*2 = c*2
Hypotenus = math.sqrt((side_a)**2+(side_b)**2)




#%% beregner areal og omkrets av trekant og sirkel

Omkr_sirkel = 2*pi*(side_a/2)

Areal_helsirkel = (side_a**2)*pi

Areal_trekant = (side_a*side_b)/2
# %% Vi trenger bare en halv sirkelbue og bruker derfor 180 grader
v_rad = 180*np.pi/180

Vinkel =  side_a / side_b

Vinkel_b_H = math.degrees(math.atan(Vinkel))


plt.close('all')


arc_angles = linspace(0 * pi, v_rad, 180)
arc_xs =side_a/2 * cos(arc_angles)
arc_ys =side_a/2 * sin(arc_angles)
plt.plot(arc_xs, arc_ys, color = 'red', lw = 1)



print("Samlet omkrets til trekant og halvsirkel er: ",round( Hypotenus + side_b +(Omkr_sirkel/2),3))
print("Samlet areal på tekant og halvsirkel er: ",round( Areal_helsirkel/2 + Areal_trekant ,3))
print("Vinkel melleom side B og hypotenus er:",round(Vinkel_b_H, 3),chr(176),sep='')
print("Se plot for grafisk framstilling.")

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

plt.gca().annotate('Hypotenus', xy =(0.15,-side_b/2-0.15), xycoords= 'data',rotation = 0, fontsize = 7)
plt.gca().annotate('katet A', xy =(0.15,0.15), xycoords= 'data',rotation = 0, fontsize = 7)
plt.gca().annotate('katet B', xy =(-side_a/2+0.15,-side_b/2), xycoords= 'data',rotation = 0, fontsize = 7)


plt.gca().set_aspect('equal')
plt.show()

