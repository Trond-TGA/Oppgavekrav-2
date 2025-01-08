# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:33:16 2024

@author: Trond G
"""
"""
Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys)
og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.
b) Lag et program som ber brukeren skrive inn et land (eksempelvis England).
Programmet skal på bakgrunn av dette skrive ut følgende setning:
London er hovedstaden i England og det er 8.982 mill. innbyggere i London

ikke allerede finnes i dictionaryen data). Videre skal brukeren oppgi hovedstad og
antall innbyggere for det «nye» landet. Programmet skal så utvide/oppdatere
dictionaryen med den nye informasjonen. Dictionaryen data skrives så til skjerm

"""

import numpy as np
import array

soke_land = str()
nytt_land = str()
svar_leggetil = str()
ny_by = str()
ant_innbyggere = int()

#dictionary av data
hovedstader =dict({ "Norge" : ["Oslo",0.634],"England" : ["London", 8.982],"Frankerike" : ["Paris", 2.169],"Italia" : ["Roma", 2.873]})

soke_land= input ( str ( print ("Hvilket land ønsker du informasjon om?" , soke_land)))



if soke_land in hovedstader:
    x = hovedstader.get(soke_land)
    hovedstad = x[0]
    ant_innbyggere = x[1]
    print(hovedstad,"er hovedstaden i",soke_land,",og det er ",ant_innbyggere,"millioner innbyggere i",hovedstad,".")

else:
   svar_leggetil = input(str(print("Landet er ikke i denne databasen. Ønsker du å legge det til? (ja/nei)",svar_leggetil)))
   if svar_leggetil == "nei" : print("Dictionary fremstår da slik:     ",hovedstader)
   
   elif svar_leggetil == "ja" :  print("ok, vi trenger noen data.")
   ny_by = input(str(print("Hva er hovedstaden i denne byen?:", ny_by)))
   ant_innbyggere = input(str(print("Hvor mange millioner innbyggere har denne byen:", ant_innbyggere)))
   hovedstader[soke_land] = ny_by, ant_innbyggere
   print(hovedstader)

