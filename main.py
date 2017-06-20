from myData import Data
dataObject = Data()
from myDecisionTree import myDecisionTree
myDecisionTreeObject = myDecisionTree()
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
print (len(months))


matchResultColor = dataObject.getMatchResultColor(matches, teamApiId)
print "Resultado de cada partido: g=green=gano , r=red=perdio , b=blue=enpato"
print matchResultColor

matchResultNumber = dataObject.getMatchResultNumber(matches, teamApiId)
print "Resultado del partido",matchResultNumber

X = np.column_stack((stage, numberOfFoulCommit, posPossesionAverage, numberOfShotOn, months))
print "Vector X \n stage, Foul, Possesion, ShotOn, months \n",X
print X.shape
Y = matchResultNumber
feature_names = ['Stage', 'Cantidad de faltas', '% Posesion','Cantidad de tiros al arco','Mes jugado']
class_names = ["Perdio" ,"Empato" , "Gano"]


myDecisionTreeObject.classifie(X,Y, feature_names,class_names ,teamName)


numberOfWinTieLose = dataObject.getNumberOfWinTieLose(matches,teamApiId)
win = str(numberOfWinTieLose[0])
tie = str(numberOfWinTieLose[1])
lose = str(numberOfWinTieLose[2])
title = 'Equipo: ' + teamName + ' -- Temporada:' + season + ' -- Cantidad de partidos:' + str(numberOfMatches) \
        + '\n  Ganados: ' + win + ' Enpatados: ' + tie + ' Perdidos: ' + lose
myPlotObject.plot(X, feature_names, matchResultColor, title, teamName)



