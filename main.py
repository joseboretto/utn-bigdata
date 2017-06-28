from tabulate import tabulate

from myData import Data
dataObject = Data()
from myClassifier import myClassifier
myClassifier = myClassifier()
from myPlot import myPlot
myPlotObject = myPlot()
import numpy as np
import pandas as pd
#table
from IPython.display import display, HTML
import plotly
plotly.__version__

import matplotlib.pyplot as plt



# https://www.premierleague.com/clubs/12/club/stats?se=42

BayerMunich = 9823
LeicesterCity = 8197
ManchesterCity = 8456
Barcelona = 8634
Arsenal = 9825 # Ganados: 20 Enpatados: 11 Perdidos: 7
Chelsea = 8455 # tiene las clases mas balanceadas 12,14,12

seasonA = ' \'2013/2014\' '
seasonB = ' \'2014/2015\' '
seasonC = ' \'2015/2016\' '
#SELECIONO PARAMETROS
season = '('+seasonA +','+ seasonB +','+ seasonC+')'
teamApiId = Chelsea

#CONSULTAS SQL
print ('#CONSULTAS SQL')
teamName = dataObject.getTeamName(teamApiId)
matches = dataObject.getMatchesFromDataBase(teamApiId , season)

#ETL
numberOfMatches = len(matches)
posPossesionAverage = dataObject.getPossesionAverage(matches, teamApiId)
numberOfFoulCommit = dataObject.getNumberOfFoulCommit(matches, teamApiId)
numberOfShotOn = dataObject.getNumberOfShotOn(matches, teamApiId)
stage = dataObject.getStage(matches)
yellowCards = dataObject.getNumberOfCards(matches, teamApiId, 'y')
corners = dataObject.getNumberOfCorner(matches, teamApiId)
crosses = dataObject.getNumberOfCross(matches, teamApiId)
matchResultColor = dataObject.getMatchResultColor(matches, teamApiId)
matchResultNumber = dataObject.getMatchResultNumber(matches, teamApiId)

#JUNTO TODOS LOS DATOS LIMPIOS
feature_names = ['Corners','Foules', 'Tiros al arco']
X = np.column_stack((crosses,numberOfFoulCommit, numberOfShotOn))
target_names = ["Perdio" , "Empato" , "Gano"]
Y = matchResultNumber

#MUESTRO EN UNA TABLA
matrixTable={}
matrixTable['Corners']=crosses
matrixTable['Foules']=numberOfFoulCommit
matrixTable['Tiros al arco']=numberOfShotOn
matrixTable['z Resultado']=matchResultNumber
dataFrameX = pd.DataFrame(matrixTable)
# display(dataFrameX)
print tabulate(dataFrameX, headers='keys', tablefmt='psql')

#PREPARO EL TITULO DE LOS DATOS
numberOfWinTieLose = dataObject.getNumberOfWinTieLose(matches,teamApiId)
win = str(numberOfWinTieLose[0])
tie = str(numberOfWinTieLose[1])
lose = str(numberOfWinTieLose[2])
title = 'Equipo: ' + teamName + ' -- Temporada:' + season + ' -- Cantidad de partidos:' + str(numberOfMatches) \
        + '\n  Ganados: ' + win + ' Enpatados: ' + tie + ' Perdidos: ' + lose


#GRAFICO TODOS LOS PARTIDOS EN DISTINTOS EJES
myPlotObject.plot(X, feature_names, matchResultColor, title, teamName)

#GRAFICO LIMITES DE DESICION DE FORMA CURVA
myClassifier.decisionTreeClassifierDesicionBoundaryCurve(X, Y, feature_names, target_names, teamName,title)
myClassifier.decisionTreeClassifierDesicionBoundaryCurveStep2(X, Y, feature_names, target_names, teamName,title)

# GRAFICO LIMITES DE DESICION DE FORMA RECTA
myClassifier.decisionTreeClassifierDesicionBoundaryStraigh(X, Y, feature_names, target_names, teamName,title)

# GRAFICO LIMITES DE DESICION ARBOL DE DESICION
myClassifier.decisionTreeClassifier(X, Y, feature_names, target_names, teamName)





