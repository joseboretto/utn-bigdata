import sqlite3
import xml.etree.ElementTree as ET
import pandas as pd

# creamos una carpeta input dentro del proyecto y copiamos la base de datos
connection = sqlite3.connect('input/database.sqlite')


class Data(object):
    def getMatchesFromDataBase(self, teamApiId):
        # obtenemos las filas que queremos del Leicester City
        sqlQuery = ' SELECT * FROM Match' \
                   ' WHERE' \
                   '( home_team_api_id = ' + str(teamApiId) + ' OR away_team_api_id = ' + str(teamApiId) + ' )'+ \
                   ' AND league_id = 1729 ' \
                   ' AND season = \'2015/2016\' '
        print (sqlQuery)
        # ejecutamos la consulta
        return pd.read_sql_query(sqlQuery, connection)

    def get_columnsNames(self):
        cursor = connection.execute('SELECT * FROM Match')
        # obtenemos todas las columnas (features, caracteristicas) == 115 columns
        column_names = [description[0] for description in cursor.description]
        return column_names

    def selectFeaturesFromMatches(self, matches):
        matches_features = matches[[
            # 'id',
            # 'country_id',
            # 'league_id',
            # 'season',
            'stage',
            # 'date''match_api_id',
            'home_team_api_id',
            'away_team_api_id',
            'home_team_goal',
            'away_team_goal',
            # 'home_player_X1',
            # 'home_player_X2',
            # 'home_player_X3',
            # 'home_player_X4',
            # 'home_player_X5',
            # 'home_player_X6',
            # 'home_player_X7',
            # 'home_player_X8',
            # 'home_player_X9',
            # 'home_player_X10',
            # 'home_player_X11',
            # 'away_player_X1',
            # 'away_player_X2',
            # 'away_player_X3',
            # 'away_player_X4',
            # 'away_player_X5',
            # 'away_player_X6',
            # 'away_player_X7',
            # 'away_player_X8',
            # 'away_player_X9',
            # 'away_player_X10',
            # 'away_player_X11',
            # 'home_player_Y1',
            # 'home_player_Y2',
            # 'home_player_Y3',
            # 'home_player_Y4',
            # 'home_player_Y5',
            # 'home_player_Y6',
            # 'home_player_Y7',
            # 'home_player_Y8',
            # 'home_player_Y9',
            # 'home_player_Y10',
            # 'home_player_Y11',
            # 'away_player_Y1',
            # 'away_player_Y2',
            # 'away_player_Y3',
            # 'away_player_Y4',
            # 'away_player_Y5',
            # 'away_player_Y6',
            # 'away_player_Y7',
            # 'away_player_Y8',
            # 'away_player_Y9',
            # 'away_player_Y10',
            # 'away_player_Y11',
            # 'home_player_1',
            # 'home_player_2',
            # 'home_player_3',
            # 'home_player_4',
            # 'home_player_5',
            # 'home_player_6',
            # 'home_player_7',
            # 'home_player_8',
            # 'home_player_9',
            # 'home_player_10',
            # 'home_player_11',
            # 'away_player_1',
            # 'away_player_2',
            # 'away_player_3',
            # 'away_player_4',
            # 'away_player_5',
            # 'away_player_6',
            # 'away_player_7',
            # 'away_player_8',
            # 'away_player_9',
            # 'away_player_10',
            # 'away_player_11',
            # 'goal',
            # 'shoton',
            # 'shotoff',
            # 'foulcommit',
            # 'card',
            # 'cross',
            # 'corner',
            # 'possession',
        ]]
        return matches_features

    def getPossesionAverage(self, matches, homeTeamApiId):
        # Datta escondida en los XML
        # https://www.kaggle.com/njitram/exploring-the-incident-data
        result = []
        numberOfRows = len(matches['possession'])
        possesionMatrix = matches[['possession']]
        homeTeamApiIdMatrix = matches[['home_team_api_id']]

        # recorremos todas las filas
        for x in range(0, numberOfRows):
            possesionXMLstring = possesionMatrix['possession'][x]
            root = ET.fromstring(possesionXMLstring)
            homeposAverage = 0  # la posesion es complementaria, tomamos solo una
            numberOfValues = len(root._children)
            # recorremos todas el xml
            for value in root:
                homeposAverage += int(value.find('./homepos').text)

            # calculamos el promedio
            homeposAverage = homeposAverage / numberOfValues
            # necesitamos saber de que equipo es la possesion
            # el resultado es una matrix de 2xn , el primero siempre es el home.
            if homeTeamApiId == homeTeamApiIdMatrix['home_team_api_id'][x]:
                result.append(homeposAverage)
            else:
                result.append(1 - homeposAverage)

        return result


        # <possession>
        #    <value>
        #       <comment>39</comment>
        #       <event_incident_typefk>352</event_incident_typefk>
        #       <elapsed>23</elapsed>
        #       <subtype>possession</subtype>
        #       <sortorder>0</sortorder>
        #       <awaypos>61</awaypos>
        #       <homepos>39</homepos>
        #       <n>45</n>
        #       <type>special</type>
        #       <id>3645948</id>
        #    </value>
        #    <value>
        #       <comment>36</comment>
        #       <event_incident_typefk>352</event_incident_typefk>
        #       <elapsed>44</elapsed>
        #       <subtype>possession</subtype>
        #       <sortorder>2</sortorder>
        #       <awaypos>64</awaypos>
        #       <homepos>36</homepos>
        #       <n>73</n>
        #       <type>special</type>
        #       <id>3646197</id>
        #    </value>
        #    <value>
        #       <comment>37</comment>
        #       <event_incident_typefk>352</event_incident_typefk>
        #       <elapsed>69</elapsed>
        #       <subtype>possession</subtype>
        #       <sortorder>1</sortorder>
        #       <awaypos>63</awaypos>
        #       <homepos>37</homepos>
        #       <n>123</n>
        #       <type>special</type>
        #       <id>3646619</id>
        #    </value>
        #    <value>
        #       <comment>36</comment>
        #       <elapsed_plus>1</elapsed_plus>
        #       <event_incident_typefk>352</event_incident_typefk>
        #       <elapsed>90</elapsed>
        #       <subtype>possession</subtype>
        #       <sortorder>11</sortorder>
        #       <awaypos>64</awaypos>
        #       <homepos>36</homepos>
        #       <n>167</n>
        #       <type>special</type>
        #       <id>3646942</id>
        #    </value>
        # </possession>

    def getNumberOfFoulCommit(self, matches, homeTeamApiId):
        # Datta escondida en los XML
        # https://www.kaggle.com/njitram/exploring-the-incident-data
        result = []
        numberOfRows = len(matches['foulcommit'])
        possesionMatrix = matches[['foulcommit']]
        homeTeamApiIdMatrix = matches[['home_team_api_id']]
        # recorremos todas las filas
        for x in range(0, numberOfRows):
            # print ('match id ' + str(matches['id'][x]))
            possesionXMLstring = possesionMatrix['foulcommit'][x]
            root = ET.fromstring(possesionXMLstring)
            numberOfFoulCommit = 0  # la posesion es complementaria, tomamos solo una
            numberOfValues = len(root._children)
            # recorremos todas el xml
            for value in root:
                teamXml = value.find('./team')
                if teamXml is not None:
                    if (int(teamXml.text) == homeTeamApiId):
                        numberOfFoulCommit += 1

            # print numberOfFoulCommit
            result.append(numberOfFoulCommit)

        return result
        # <foulcommit>
        #     <value>
        #         <stats>
        #             <foulscommitted>1</foulscommitted>
        #         </stats>
        #         <event_incident_typefk>37</event_incident_typefk>
        #         <coordinates>
        #             <value>42</value>
        #             <value>47</value>
        #         </coordinates>
        #         <elapsed>1</elapsed>
        #         <player2>36012</player2>
        #         <player1>67850</player1>
        #         <sortorder>1</sortorder>
        #         <team>8197</team>
        #         <n>215</n>
        #         <type>foulcommit</type>
        #         <id>3645732</id>
        #     </value>
        # </foulcommit>

    def getWinnerFromTeamId(self, matches, homeTeamApiId):
        numberOfRows = len(matches['id'])
        home_team_api_idMatrix = matches[['home_team_api_id']]
        home_team_goalMatrix = matches[['home_team_goal']]
        away_team_goalMatrix = matches[['away_team_goal']]

        result = []
        # recorremos todas las filas
        for x in range(0, numberOfRows):
            # como le fue al local?
            if home_team_goalMatrix['home_team_goal'][x] == away_team_goalMatrix['away_team_goal'][x]:
                result.append('b')
                continue

            if home_team_goalMatrix['home_team_goal'][x] > away_team_goalMatrix['away_team_goal'][x]:
                homeWon = True
            else:
                homeWon = False
            # como le fue al equipo que estoy analizando?
            if home_team_api_idMatrix['home_team_api_id'][x] == homeTeamApiId:
                homeWon
            else:
                homeWon = not homeWon

            # elijo el color
            if homeWon:
                result.append('g')
            else:
                result.append('r')

        return result

    def getStage(self, matches):
        numberOfRows = len(matches['id'])
        stageMatrix = matches[['stage']]

        result = []
        # recorremos todas las filas
        for x in range(0, numberOfRows):
            stageNumber = stageMatrix['stage'][x]
            result.append(stageNumber)

        return result