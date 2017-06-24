#%%
from myData import Data
dataObject = Data()
#from myClassifier import myClassifier
#myClassifier = myClassifier()
from myPlot import myPlot
myPlotObject = myPlot()


import numpy as np
# https://www.premierleague.com/clubs/12/club/stats?se=42
season = ' \'2015/2016\' '
LeicesterCity = 8197
ManchesterCity = 8456
Barcelona = 8634
Arsenal = 9825
Chelsea = 8455 # tiene las clases mas balanceadas 12,14,12

teamApiId = Chelsea

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

stage = dataObject.getStage(matches)
print "Stage o Fecha del torneo"
print (stage)
print (len(stage))

months = dataObject.getMonth(matches)
print "Meses"
print (months)
#%%
#cardsY = dataObject.getNumberOfCardsY(matches, teamApiId)
#print "Tarjetas Amarillas"
#print (cardsY)

#cardsR = dataObject.getNumberOfCardsR(matches, teamApiId)
#print "Tarjetas Rojas"
#print (cardsR)
#%%
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



feature_names = ['Stage', 'Cantidad de faltas', '% Posesion','Cantidad de tiros al arco','Mes jugado','Corners', 'Tarjetas Amarillas', 'Tarjetas Rojas', 'Cruces efectuados']
X = np.column_stack((stage, numberOfFoulCommit, posPossesionAverage, numberOfShotOn, months, corners, yellowCards, redCards, crosses))
print feature_names
print X
print X.shape
Y = matchResultNumber
class_names = ["Perdio" ,"Empato" , "Gano"]


#myClassifier.decisionTreeClassifier(X, Y, feature_names, class_names, teamName)
#myClassifier.SVMClassifier(X,Y, feature_names)

numberOfWinTieLose = dataObject.getNumberOfWinTieLose(matches,teamApiId)
win = str(numberOfWinTieLose[0])
tie = str(numberOfWinTieLose[1])
lose = str(numberOfWinTieLose[2])
title = 'Equipo: ' + teamName + ' -- Temporada:' + season + ' -- Cantidad de partidos:' + str(numberOfMatches) \
        + '\n  Ganados: ' + win + ' Enpatados: ' + tie + ' Perdidos: ' + lose
myPlotObject.plot(X, feature_names, matchResultColor, title, teamName)
#%%


