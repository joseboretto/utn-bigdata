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
import os
plotly.__version__

import matplotlib.pyplot as plt



# https://www.premierleague.com/clubs/12/club/stats?se=42

BayerMunich = 9823
LeicesterCity = 8197
ManchesterCity = 8456
Barcelona = 8634
Arsenal = 9825 # Ganados: 20 Enpatados: 11 Perdidos: 7
Chelsea = 8455 # tiene las clases mas balanceadas 12,14,12
AtleticoDeMadrid = 9906


seasonB = ' \'2014/2015\' '
seasonC = ' \'2015/2016\' '
#SELECIONO PARAMETROS
season = '('+seasonB +','+ seasonC+')'
teamApiId = AtleticoDeMadrid

#CONSULTAS SQL
print ('#CONSULTAS SQL')
teamName = dataObject.getTeamName(teamApiId)
matches = dataObject.getMatchesFromDataBase(teamApiId , season)
numberOfMatches = len(matches)

#ETL
posPossesionAverage = dataObject.getPossesionAverage(matches, teamApiId)
numberOfFoulCommit = dataObject.getNumberOfFoulCommit(matches, teamApiId)
numberOfShotOn = dataObject.getNumberOfShotOn(matches, teamApiId)
corners = dataObject.getNumberOfCorner(matches, teamApiId)
crosses = dataObject.getNumberOfCross(matches, teamApiId)
#tabla
stage = dataObject.getStage(matches)
#plot
matchResultColor = dataObject.getMatchResultColor(matches, teamApiId)
matchResultNumber = dataObject.getMatchResultNumber(matches, teamApiId)

#JUNTO TODOS LOS DATOS LIMPIOS
feature_names = ['posesion','cantidad de faltas','tiros al arco','corners','cruces']
X = np.column_stack((posPossesionAverage,numberOfFoulCommit,numberOfShotOn,corners,crosses))
target_names = ["Perdio" , "Empato" , "Gano"]
Y = matchResultNumber

#MUESTRO EN UNA TABLA
matrixTable={}
matrixTable['0.id.stage']=stage
matrixTable['1.posesion']=posPossesionAverage
matrixTable['2.cantidad de faltas']=numberOfFoulCommit
matrixTable['3.tiros al arco']=numberOfShotOn
matrixTable['4.corners']=corners
matrixTable['5.cruces']=crosses
matrixTable['Resultados']=matchResultNumber
matrixTable['Color']=matchResultColor
dataFrameX = pd.DataFrame(matrixTable)

print tabulate(dataFrameX, headers='keys', tablefmt='psql')


#PREPARO EL TITULO DE LOS DATOS
numberOfWinTieLose = dataObject.getNumberOfWinTieLose(matches,teamApiId)
win = str(numberOfWinTieLose[0])
tie = str(numberOfWinTieLose[1])
lose = str(numberOfWinTieLose[2])
title = 'Equipo: ' + teamName + ' -- Temporada:' + season + ' -- Cantidad de partidos:' + str(numberOfMatches) \
        + '\n  Ganados: ' + win + ' Enpatados: ' + tie + ' Perdidos: ' + lose

# save table
if not os.path.exists(teamName):
    os.makedirs(teamName)

text_file = open(teamName + '/' +teamName + "- table.txt", "w")
text_file.write(title + "\n" + "\n Rojo(-1)=Perdio , Amarillo(0)=Enpato  , Azul(1)=Gano \n\n\n"+ tabulate(dataFrameX, headers='keys', tablefmt='psql'))
text_file.close()


# GRAFICO TODOS LOS PARTIDOS EN DISTINTOS EJES
# myPlotObject.plot(X, feature_names, matchResultColor, title, teamName)


# GRAFICO LIMITES DE DESICION DE FORMA RECTA
# myClassifier.decisionTreeClassifierDesicionBoundaryStraigh(X, Y, feature_names, target_names, teamName,title,matchResultColor)


###GRAFICO SCATER MATRIX Y SUPERFICIES DE DESICION
# myClassifier.decisionTreeClassifierDesicionBoundaryStraighDepth(X, Y, feature_names, target_names, teamName,title,matchResultColor,1)
myClassifier.decisionTreeClassifierDesicionBoundaryStraighDepth(X, Y, feature_names, target_names, teamName,title,matchResultColor,2)
myClassifier.decisionTreeClassifierDesicionBoundaryStraighDepth(X, Y, feature_names, target_names, teamName,title,matchResultColor,5)



# GRAFICO LIMITES DE DESICION ARBOL DE DESICION
# myClassifier.decisionTreeClassifier(X, Y, feature_names, target_names, teamName)
# myClassifier.decisionTreeClassifierMaxDepth(X, Y, feature_names, target_names, teamName,5)




