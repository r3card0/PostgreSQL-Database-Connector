import pandas as pd
import os
from .connect import DatabaseConnector
from .modify_file_path import PathConverter

class CreateDataframe:
    def __init__(self,sql_query:str,connection_filepath:str):
        self.query = sql_query
        self.connection_file = connection_filepath
        self.sql = sql = [] # empty list

    # evaluates if sql_query is a file or a variable
    def is_file(self):
        if os.path.isfile(PathConverter(self.query).convert_path()):
            return True
        else:
            return False
        
    def get_dataframe(self):
        # establishing connection with PostgreSQL database
        try:
            connection = DatabaseConnector(self.connection_file).connectdb()
            print("Database connection established sucessfully.")
        except Exception as e:
            print(f"Failed to connect to the database: {e}")
        
        # 2. Evaluates query source
        try:
            if self.is_file() == True:
                get_query = self.read_sql_file()
                print("The SQL query source is a file")
            else:
                get_query = self.query
                print("The SQL query source is a variable")
        except Exception as e:
            print(f"Failure to evaluates the query source: {e}")

        # 3. Dataframe creation
        try:
            print("Creating the dataframe")
            df_pre = pd.read_sql_query(get_query,connection)
            df = df_pre.copy(deep=True)
            print("Dataframe successfully created.")
        except Exception as e:
            print(f"Failure to create Dataframe: {e}")

        # close connection
        finally:
            try:
                connection.close()
                print("Database closed successfully.")
            except Exception as e:
                print(f"Failure to close connection: {e}")

        return df

    
    # Reads the sql script file given by the file path and returns it by string format
    def read_sql_file(self):
        convert_filepath = PathConverter(self.query).convert_path()
        
        # open the file and append the sql statements as a list
        with open(convert_filepath,"r",encoding="utf-8") as file:
            for line in file:
                self.sql.append(line)

        #  convert the list to a string format
        sql_query = """""".join(self.sql)
        # returns a string format
        return sql_query



