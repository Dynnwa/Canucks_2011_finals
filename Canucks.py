#!/usr/bin/env python
# coding: utf-8

## asdjfasijdfn
import sys
#get_ipython().system('{sys.executable} -m pip install pulp ')
import pulp
from pulp import *

players = ['pae', 'pce', 'pds', 'phs', 'prk', 'pdh','pkb', 'pms', 'pss', 'dh', 'ds', 'ab'
           ,'ml', 'kb', 'rk', 'ar', 'ce', 'ae','kball', 'hs', 'ms', 'mr']

goals = {'pae': 1/6, 'pce':1/6, 'pds':11/60, 'phs':11/60, 'prk':11/60, 'pdh':1/12,'pkb':7/60,
         'pms':9/60, 'pss':9/60, 'dh':6/1451, 'ds':41/1521, 'ab':26/1226,
         'ml':1/219, 'kb':6/1483, 'rk':41/1681, 'ar':1/975, 'ce':14/1895, 'ae':8/1237,
         'kball':2/1034, 'hs':19/1579, 'ms':18/1247, 'mr':15/1106}

powerPlaypos = {'pae': 1, 'pce':1, 'pds':1, 
                'phs':1, 'prk':1, 'pdh':1,'pkb':1,
                'pms':1, 'pss':1, 'dh':0, 'ds':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}

powerPlayneg = {'pae': -1, 'pce':-1, 'pds':-1, 
                'phs':-1, 'prk':-1, 'pdh':-1,'pkb':-1,
                'pms':-1, 'pss':-1, 'dh':0, 'ds':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}

penalty = {'pae': 0, 'pce':0, 'pds':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ds':24/137, 'ab':28/131,
           'ml':12/88, 'kb':14/175, 
           'rk':35/145, 'ar':19/38, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}

blocks = {'pae': 0, 'pce':0, 'pds':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0,'ds':0,'ce':-108/1895, 'ae':-86/1239,
           'dh':-89/1451, 'kb':-93/1483, 
           'kball':-111/1034, 'hs':0, 'ms':0, 'mr':0,'ab':0,'ml':0,'rk':0,'ar':0}

hits = {'pae': 0, 'pce':0, 'pds':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0,'ds':0,'ce':-51/1895, 'ae':-83/1239,
        'dh':-76/1451, 'kb':-104/1483, 
        'kball':-99/1034, 'hs':0, 'ms':0, 'mr':0,'ab':0,'ml':0,'rk':0,'ar':0}

dsFatigue = {'ds':1, 'pds':1,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
rkFatigue = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':1, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':1, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
abFatigue = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':1,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
hsFatigue = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':1, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':1, 'ms':0, 'mr':0}
msFatigue = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':1, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':1, 'mr':0}
mrFatigue = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':1}

## new
dhFatigue = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':1, 'pss':0, 'dh':1, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
mlFatigue = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':1, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
ceFatigue = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':1, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
aeFatigue = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':1,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
kbFatigue = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':1, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
arplay = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':1, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
kballplay = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':1, 'hs':0, 'ms':0, 'mr':0}

pdsplay = {'ds':0, 'pds':1,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
paeplay = {'ds':0, 'pds':0,'pae': 1, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
pceplay = {'ds':0, 'pds':0,'pae': 0, 'pce':1, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
prkplay = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':1, 'pdh':0,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
pdhplay = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':1,'pkb':0,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
pkbplay = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':1,
                'pms':0, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
pmsplay = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':1, 'pss':0, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}
pssplay = {'ds':0, 'pds':0,'pae': 0, 'pce':0, 
                'phs':0, 'prk':0, 'pdh':0,'pkb':0,
                'pms':0, 'pss':1, 'dh':0, 'ab':0,
         'ml':0, 'kb':0, 'rk':0, 'ar':0, 'ce':0, 'ae':0,
         'kball':0, 'hs':0, 'ms':0, 'mr':0}


prob = LpProblem("Vancouver_Canucks", LpMaximize)
player_vars = LpVariable.dicts("Players", players, 0)


# # Objective function

prob += lpSum([goals[p]*player_vars[p] for p in players]), "Total points scored"   


# # Constraints

prob += lpSum([powerPlaypos[p]*player_vars[p] for p in players]) == 78, "powerPlaypos"
#prob += lpSum([powerPlayneg[p]*player_vars[p] for p in players]) <= -91, "powerPlayneg"
prob += lpSum([penalty[p]*player_vars[p] for p in players]) <= 119, "penalty"
prob += lpSum([blocks[p]*player_vars[p] for p in players]) <= -29, "blocks"
prob += lpSum([hits[p]*player_vars[p] for p in players]) <= -24.5, "hits"

prob += lpSum([dsFatigue[p]*player_vars[p] for p in players]) <= 7*18, "ds"
prob += lpSum([rkFatigue[p]*player_vars[p] for p in players]) <= 7*20, "rk"
prob += lpSum([abFatigue[p]*player_vars[p] for p in players]) <= 7*17, "ab"
prob += lpSum([hsFatigue[p]*player_vars[p] for p in players]) <= 7*19, "hs"
prob += lpSum([msFatigue[p]*player_vars[p] for p in players]) <= 7*16, "ms"
prob += lpSum([mrFatigue[p]*player_vars[p] for p in players]) <= 7*15, "mr"

## new constraints
prob += lpSum([dhFatigue[p]*player_vars[p] for p in players]) <= 7*22, "dh"
prob += lpSum([mlFatigue[p]*player_vars[p] for p in players]) <= 7*11, "ml"
prob += lpSum([ceFatigue[p]*player_vars[p] for p in players]) <= 7*24, "ce"
prob += lpSum([aeFatigue[p]*player_vars[p] for p in players]) <= 7*24, "ae"
prob += lpSum([kbFatigue[p]*player_vars[p] for p in players]) <= 7*22, "kb"

prob += lpSum([arplay[p]*player_vars[p] for p in players]) >= 10, "ar"
prob += lpSum([kballplay[p]*player_vars[p] for p in players]) >= 10, "kball"

prob += lpSum([paeplay[p]*player_vars[p] for p in players]) >= 10, "pae"
prob += lpSum([pceplay[p]*player_vars[p] for p in players]) >= 10, "pce"
prob += lpSum([pdhplay[p]*player_vars[p] for p in players]) >= 10, "pdh"
prob += lpSum([pdsplay[p]*player_vars[p] for p in players]) >= 10, "pds"
prob += lpSum([pkbplay[p]*player_vars[p] for p in players]) >= 10, "pkb"
prob += lpSum([pmsplay[p]*player_vars[p] for p in players]) >= 10, "pms"
prob += lpSum([prkplay[p]*player_vars[p] for p in players]) >= 10, "prk"
prob += lpSum([pssplay[p]*player_vars[p] for p in players]) >= 10, "pss"


print(prob)


# # Solve the LP.

prob.solve()
print("Status:", LpStatus[prob.status])


for a in prob.variables():
    print(a.name, "=", a.varValue)


print("Total Goals", value(prob.objective))


#Slack and Dual
print("powerplay")
print("Slack:", prob.constraints["powerPlaypos"].slack)
print("Shadow:", prob.constraints["powerPlaypos"].pi)

print("penalty")
print("Slack:", prob.constraints["penalty"].slack)
print("Shadow:", prob.constraints["penalty"].pi)

print("blocks")
print("Slack:", prob.constraints["blocks"].slack)
print("Shadow:", prob.constraints["blocks"].pi)

print("hits")
print("Slack:", prob.constraints["hits"].slack)
print("Shadow:", prob.constraints["hits"].pi)


