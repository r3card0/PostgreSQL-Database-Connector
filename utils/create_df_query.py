import pandas as pd
import os
from .connect import DatabaseConnector
from .modify_file_path import PathConverter
import psycopg2
from psycopg2 import OperationalError, ProgrammingError

class CreateDataframe:
    def __init__(self,sql_query:str,connection_filepath:str):
        self.query = sql_query
        self.connection_file = connection_filepath
        self.sql = sql = [] # empty list

    def is_file(self):
        """Evaluates if sql_query is a file or a variable"""
        return os.path.isfile(PathConverter(self.query).convert_path())
        
    
    def read_sql_file(self):
        """Reads the SQL script file and returns it as string"""
        convert_filepath = PathConverter(self.query).convert_path()
        
        # open the file and append the sql statements as a list
        try:
            with open(convert_filepath,"r",encoding="utf-8") as file:
                sql_query = file.read()
            # returns a string format
            return sql_query
        except FileNotFoundError:
            raise FileNotFoundError(
                f"SQL file not found: {convert_filepath}."
                "Please verify the file path exists."
            )
        except PermissionError:
            raise PermissionError(
                f"Permission denied to read file: {convert_filepath}"
            )
        except Exception as e:
            raise IOError(f"Error reading SQL file: {e}")

    
    def get_dataframe(self):
        """Creates dataframe from SQL query"""
        connection = None # Avoid UnboundLocalError

        # 1. Establishing connection with PostgreSQL database
        try:
            connection = DatabaseConnector(self.connection_file).connectdb()
            print("Database connection established sucessfully.")
        except OperationalError as e:
            raise OperationalError(
                f"Failed to connect to database. Check your connection settings: {e}"
            )
        except FileNotFoundError as e:
            raise FileNotFoundError(
            f"Connection file not found: {self.connection_file} {e}"
        )
        except Exception as e:
            raise ConnectionError(f"Unexpected error during connection: {e}")
        
        # 2. Determine query source
        try:
            if self.is_file():
                get_query = self.read_sql_file()
                print("SQL query source: file")
            else:
                get_query = self.query
                print("SQL query source: variable string")
        except Exception as e:
            raise ValueError(f"Failed to evaluate query source: {e}")

        # 3. Dataframe creation
        try:
            print("Creating dataframe . . .")
            df_pre = pd.read_sql_query(get_query,connection)
            df = df_pre.copy(deep=True)
            print("Dataframe successfully created.")
            return df
        except ProgrammingError as e:
            raise ProgrammingError(
                f"SQL syntax error. Please verify your query:\n{e}"
            )
        except Exception as e:
            raise RuntimeError(f"Failed to create dataframe: {e}")

        # close connection
        finally:
            try:
                connection.close()
                print("Database closed successfully.")
            except Exception as e:
                print(f"⚠️ Warning: Failed to close connection: {e}")