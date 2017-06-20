from myData import Data
dataObject = Data()
from myDecisionTree import myDecisionTree
myDecisionTreeObject = myDecisionTree()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# https://www.premierleague.com/clubs/12/club/stats?se=42
season = ' \'2015/2016\' '
LeicesterCity = 8197
ManchesterCity = 8456
Barcelona = 8634
Arsenal = 9825
Chelsea = 8455 # tiene las clases mas balanceadas 12,14,12

teamApiId = Arsenal

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


winnerFromTeamId = dataObject.getWinnerFromTeamId(matches, teamApiId)
print "Resultado de cada partido: g=green=gano , r=red=perdio , b=blue=enpato"
print winnerFromTeamId

matchResult = dataObject.countMatchResult(winnerFromTeamId)
print "Resultado del partido",matchResult
X = np.column_stack((stage, numberOfFoulCommit, posPossesionAverage, numberOfShotOn, months))
print "Vector X \n stage, Foul, Possesion, ShotOn, months \n",X
print X.shape
Y = dataObject.tranformColorsInNumber(winnerFromTeamId)
feature_names = ["stage", "Foul", "Possesion", "ShotOn", "months"]
class_names = ["Perdio" ,"Empato" , "Gano"]
myDecisionTreeObject.classifie(X,Y, feature_names,class_names ,teamName)
# X_new = SelectKBest(chi2, k=2).fit_transform(X, Y)
#
# print "Vector X Slect K best \n",X_new
# print X_new.shape
#
# pca = PCA(n_components=2)
# X_new_pca = pca.fit_transform(X,Y)
# print(pca.explained_variance_ratio_)
# print "Vector X PCA \n ",X_new_pca


df = pd.DataFrame(X, columns=['Stage', 'Cantidad de faltas', '% Posesion', 'Cantidad de tiros al arco', 'Mes jugado'])
# Doc: https://pandas.pydata.org/pandas-docs/stable/visualization.html#scatter-matrix-plot
scatter_matrix(df, figsize=(10, 10), diagonal='hist', color=winnerFromTeamId)
title = 'Equipo: ' + teamName + ' -- Temporada:' + season + ' -- Cantidad de partidos:' + str(numberOfMatches) + '\n' \
        ' Ganados: ' + str(matchResult[0])+' Enpatados: ' + str(matchResult[1])+' Perdidos: ' + str(matchResult[2])
plt.suptitle(title)
# plt.show()

pp = PdfPages(teamName + '- Caracteristicas .pdf')
plt.savefig(pp, format='pdf')
pp.savefig()
pp.close()