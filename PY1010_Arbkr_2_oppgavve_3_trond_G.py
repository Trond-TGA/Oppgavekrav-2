# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:47:39 2024

@author: Trond G
Oppg 3) Lag et program med en funksjon som regner om fra grader til radianer.
Programmet skal starte med:
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180
Resultatet v_rad skrives til skjerm med passende tekst og verdi.
Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....

"""
# henter inn moduler

import numpy as np
from numpy import radians,sin,cos,pi,linspace
import matplotlib.pyplot as plt
import math

y_komponent_vinkel = float
x_komponent_vinkel = float

#beregner radianer fra grader - ut kommer integer
v_grad = float(input('Skriv inn gradtallet:' ))
v_rad = v_grad*np.pi/180
radians(v_grad)
#beregner samme som v_grad men nå som liste -(forsøk på ekte brøk)
gradvinkler = [v_grad]
radianvinkler = [v*pi/180 for v in gradvinkler]
print(v_grad, "grader tilsvarer", round( v_rad, 4) ,"radianer, og se gjerne på plott av vinkelen.")

plt.close('all')
#tegner et punkt i punktet (0,0)

plt.plot(0,0, color ='red', marker ='o')
plt.gca().annotate('Origo (0,0)', xy = (0 + 0.1, 0 + 0.1), xycoords= 'data', fontsize = 8)

#tegner sirkelen grønn
angles = linspace(0 * pi, 2 * pi, 100)
xs = cos(angles)
ys = sin(angles)
plt.plot(xs ,ys, color = 'green' )
r = 1


# tegner diameter blå vertikal 
plt.plot( 0, 1, marker= 'o', color = 'blue')
plt.plot(0, -1, marker= 'o', color = 'blue')
plt.plot([0, 0],[1, -1], marker= 'o', color = 'blue')

plt.gca().annotate('Diameter', xy = (-0.2,0), xycoords= 'data',rotation = 90, fontsize = 8)

# tegner radius lilla
plt.plot([0, 1], [0, 0] , marker= 'o', color = 'red')
plt.gca().annotate('Radius', xy = (0.3,-0.2), xycoords= 'data', fontsize = 8)

#tegne buen som er rød langs sirkel
arc_angles = linspace(0 * pi, v_rad, 100)
arc_xs =r * cos(arc_angles)
arc_ys =r * sin(arc_angles)
plt.plot(arc_xs, arc_ys, color = 'red', lw = 2)

#tegner strek fra 0,0 til P
y_komponent_vinkel = arc_ys[99]
x_komponent_vinkel = arc_xs[99]
# tegner inn radianer i punktet tilpasset plassering
if 89 < v_grad < 269:
  plt.plot([0, x_komponent_vinkel], [0, y_komponent_vinkel] , marker= 'o', color = 'red')
  plt.gca().annotate( round(v_rad, 4), xy = (x_komponent_vinkel + 0.1 , y_komponent_vinkel + 0.3), horizontalalignment='right',xycoords= 'data', fontsize = 8)
else:
  plt.plot([0, x_komponent_vinkel], [0, y_komponent_vinkel] , marker= 'o', color = 'red')
  plt.gca().annotate( round(v_rad, 4), xy = (x_komponent_vinkel + 0.1 , y_komponent_vinkel + 0.3), horizontalalignment='left',xycoords= 'data', fontsize = 8)

#finner rammene for plottet
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

#passer på at X og Y skala er like lang med Equal
plt.gca().set_aspect('equal')
plt.show()



