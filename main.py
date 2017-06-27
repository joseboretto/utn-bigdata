from pandas.plotting import scatter_matrix
import pandas as pd
import matplotlib.pyplot as plt
from plotly.offline.offline import matplotlib

#%%
from myData import Data
dataObject = Data()
from myClassifier import myClassifier
myClassifier = myClassifier()
from myPlot import myPlot
myPlotObject = myPlot()




import numpy as np
# https://www.premierleague.com/clubs/12/club/stats?se=42
season = ' \'2015/2016\' '
LeicesterCity = 8197
ManchesterCity = 8456
Barcelona = 8634
Arsenal = 9825 # Ganados: 20 Enpatados: 11 Perdidos: 7
Chelsea = 8455 # tiene las clases mas balanceadas 12,14,12

teamApiId = Arsenal

teamName = dataObject.getTeamName(teamApiId)
matches = dataObject.getMatchesFromDataBase(teamApiId , season)
numberOfMatches = len(matches)
print "Cantidad de partido: ", numberOfMatches
#%%
posPossesionAverage = dataObject.getPossesionAverage(matches, teamApiId)
print "% possesion"
print (posPossesionAverage)
print (len(posPossesionAverage))

numberOfFoulCommit = dataObject.getNumberOfFoulCommit(matches, teamApiId)
print "Cantidad de faltas"
print (numberOfFoulCommit)
print (len(numberOfFoulCommit))

numberOfShotOn = dataObject.getNumberOfShotOn(matches, teamApiId)
print "Cantidad de tiros al arco"
print (numberOfShotOn)
print (len(numberOfShotOn))

yellowCards = dataObject.getNumberOfCards(matches, teamApiId, 'y')
print "Tarjetas Amarillas"
print (yellowCards)

redCards = dataObject.getNumberOfCards(matches, teamApiId, 'r')
print "Tarjetas Rojas"
print (redCards)
#%%
corners = dataObject.getNumberOfCorner(matches, teamApiId)
print "Corners"
print (corners)
#%%
crosses = dataObject.getNumberOfCross(matches, teamApiId)
print "Cruces"
print (crosses)
#%%
matchResultColor = dataObject.getMatchResultColor(matches, teamApiId)
print "Resultado de cada partido: g=green=gano , r=red=perdio , b=blue=enpato"
print matchResultColor

matchResultNumber = dataObject.getMatchResultNumber(matches, teamApiId)
print "Resultado del partido",matchResultNumber



feature_names = ['Corners','Foules', 'Tiros al arco']
X = np.column_stack((crosses,numberOfFoulCommit, numberOfShotOn))
print feature_names
print X
print X.shape
Y = matchResultNumber
class_names = ["Perdio" ,"Empato" , "Gano"]

myClassifier.decisionTreeClassifier(X, Y, feature_names, class_names, teamName)

myClassifier.decisionTreeClassifierDesicionBoundary(X, Y, feature_names, class_names, teamName)

# myClassifier.decisionTreeClassifier(X, Y, feature_names, class_names, teamName)


numberOfWinTieLose = dataObject.getNumberOfWinTieLose(matches,teamApiId)
win = str(numberOfWinTieLose[0])
tie = str(numberOfWinTieLose[1])
lose = str(numberOfWinTieLose[2])
title = 'Equipo: ' + teamName + ' -- Temporada:' + season + ' -- Cantidad de partidos:' + str(numberOfMatches) \
        + '\n  Ganados: ' + win + ' Enpatados: ' + tie + ' Perdidos: ' + lose


df = pd.DataFrame(X, columns=feature_names)
# Doc: https://pandas.pydata.org/pandas-docs/stable/visualization.html#scatter-matrix-plot
scatter_matrix(df, figsize=(10, 10), diagonal='hist', color=matchResultColor)
plt.suptitle(title)
# plt.show()
myPlotObject.plot(X, feature_names, matchResultColor, title, teamName)
#%%


