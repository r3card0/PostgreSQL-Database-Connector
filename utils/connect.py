import psycopg2 as p2
from .configreader import PostgreSQLConfigReader

class DatabaseConnector():
    def __init__(self,filepath:str):
        self.params = PostgreSQLConfigReader(filepath).config()

    
    def connectdb(self):
        connection = p2.connect(**self.params)
        return connection