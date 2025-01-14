# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:49:18 2024
Oppgave 1 arbeidskrav 2
@author: Trond G
"""

#%% """Henter inn moduler"""
import numpy as np
import time
import datetime

#%% """ utregninger"""
aarfodt = int(input("Hvilket år ble du født?", ))

#%% henter tidenstempel fra datamaskinen som brukes
referansetid = time.localtime()

AlderIaar =  referansetid.tm_year - aarfodt +1

#%% """ut på skjermen Her vil utregningene være feil hvis bruker har hatt bursdag i løpet av dette året"""

print ( "Du er ", referansetid.tm_year - aarfodt,"år gammel, og holder deg godt :-)")
print ( "Dersom alt går som planlagt, vil du bli ", AlderIaar,"i år.")




