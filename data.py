import sqlite3
import xml.etree.ElementTree as ET
import pandas as pd

# creamos una carpeta input dentro del proyecto y copiamos la base de datos
connection = sqlite3.connect('input/database.sqlite')

class Data(object):
    def getMatchesFromDataBase(self):
        # obtenemos las filas que queremos del Leicester City
        sqlQuery = ' SELECT * FROM Match' \
                   ' WHERE' \
                   ' home_team_api_id = 8197 OR away_team_api_id = 8197 ' \
                   ' AND league_id = 1729 ' \
                   ' AND season = 2015/2016'
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

    def xmlparser(self, matches):
        # Datta escondida en los XML
        # https://www.kaggle.com/njitram/exploring-the-incident-data
        possesionMatrix = matches[['possession']]
        possesion = possesionMatrix['possession'][0]
        print possesion
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
        root = ET.fromstring(possesion)
        awayposAverage = 0
        homeposAverage = 0
        numberOfValues = len(root._children)
        for value in root:
            awayposAverage += int(value.find('./awaypos').text)
            homeposAverage += int(value.find('./homepos').text)

        print awayposAverage, homeposAverage
        awayposAverage = awayposAverage / numberOfValues
        homeposAverage = homeposAverage / numberOfValues

        print awayposAverage, homeposAverage
        return awayposAverage
