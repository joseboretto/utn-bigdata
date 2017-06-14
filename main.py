from data import Data
import matplotlib.pyplot as plt

# Leicester City , teamApiId = 8197
# Manchester City , teamApiId =  8456
teamApiId = 8456
dataObject = Data()
matches = dataObject.getMatchesFromDataBase(teamApiId)
# print (matches)

posPossesionAverage = dataObject.getPossesionAverage(matches, teamApiId)
print ""
print (posPossesionAverage)
print (len(posPossesionAverage))

numberOfFoulCommit = dataObject.getNumberOfFoulCommit(matches, teamApiId)
print (numberOfFoulCommit)
print (len(numberOfFoulCommit))


stage = dataObject.getStage(matches)
print (stage)
print (len(stage))

winnerFromTeamId =  dataObject.getWinnerFromTeamId(matches,teamApiId)
print winnerFromTeamId

plt.xlabel('POSESION %')
plt.ylabel('CANTIDAD DE FALTAS')
plt.scatter(posPossesionAverage, numberOfFoulCommit, color=winnerFromTeamId)
# plt.axis([0, 6, 0, 20])
plt.show()