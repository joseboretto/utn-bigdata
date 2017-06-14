from numpy.matlib import randn

from data import Data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix

# Leicester City , teamApiId = 8197
# Manchester City , teamApiId =  8456
teamApiId = 9825
dataObject = Data()
matches = dataObject.getMatchesFromDataBase(teamApiId)

posPossesionAverage = dataObject.getPossesionAverage(matches, teamApiId)
print "% possesion"
print (posPossesionAverage)
print (len(posPossesionAverage))

numberOfFoulCommit = dataObject.getNumberOfFoulCommit(matches, teamApiId)
print "Cantidad de faltas"
print (numberOfFoulCommit)
print (len(numberOfFoulCommit))

numberOfShotOn = dataObject.getNumberOfShotOn(matches,teamApiId)
print "Cantidad de tiros al arco"
print (numberOfShotOn)
print (len(numberOfShotOn))

stage = dataObject.getStage(matches)
print "Stage o Fecha del torneo"
print (stage)
print (len(stage))

winnerFromTeamId =  dataObject.getWinnerFromTeamId(matches,teamApiId)
print "Resultado de cada partido: g=green=gano , r=red=perdio , b=blue=enpato"

print winnerFromTeamId

X = np.column_stack((stage, numberOfFoulCommit, posPossesionAverage, numberOfShotOn))
print X

df = pd.DataFrame(X, columns=['Stage', 'Cantidad de faltas', '% Posesion', 'Cantidad de tiros al arco'])
# Doc: https://pandas.pydata.org/pandas-docs/stable/visualization.html#scatter-matrix-plot
scatter_matrix(df, figsize=(10, 10), diagonal='kde',color=winnerFromTeamId)

plt.show()