import mysql.connector
from mysql.connector.errors import *
from mysql.connector import errorcode
import pandas as pd
import sys

class MySQLWrapper:
    def __init__(self, host, user, password, database, debug=True):
        # Try to connect to the database, and if there were any errors report and quit
        self.host = host
        self.database = database
        self.debug = debug
        self.connection = None
        try:
            self.connection = self.get_connector(user, password)
        except mysql.connector.Error as err:
        
            print('Error connecting to the host.')
            sys.exit(1)
        if self.debug:
            print('Connected to host.')
		# Get the cursor
        self.cursor = self.connection.cursor() 

    def get_connector(self, username, dbpass):
        ''' Connect to the database and return the connector '''
        if self.debug:
            print('Connecting to database...')
		# If there is an active connection ,return it
        if self.connection and self.connection.is_connected():
            if self.debug:
                print('Already connected!')
            return self.connection
        return mysql.connector.connect(user = username, password = dbpass, host = self.host, database = self.database, ssl_disabled=False)

    def execute_query(self, query, params=None):
        ''' Return all the results from a query '''
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
        except InternalError:
            if self.debug:
                print('Error : No results for table')
            return []
        return self.cursor.fetchall() 

    def fetch_df(self, query, params=None):
        result = self.execute_query(query, params)
        columns = [desc[0] for desc in self.cursor.description]
        df = pd.DataFrame(result, columns=columns)
        return df

    def commit(self):
        ''' Commit changes to the remote DB '''
        if self.debug:
            print('Commiting changes...')
        self.connection.commit()

    def close_connection(self):
        ''' Close the connection '''
        self.cursor.close()
        self.connection.close()
        if self.debug:
            print('Connection closed.')

    def close(self):
        ''' Called upon object deletion, make sure the connection to the DB is closed '''
        if self.connection is not None:
            self.close_connection()

    def rollback(self):
        ''' Rollback changes in case of errors of any kind '''
        if self.debug:
            print('Rolling back...')
        self.conn.rollback()

