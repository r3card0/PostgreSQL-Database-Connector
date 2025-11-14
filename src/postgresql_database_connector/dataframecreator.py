# dependencies
from configparser import ConfigParser
from path_converter import PathConverter
from psycopg2 import OperationalError, ProgrammingError

# libraries
import psycopg2 as p2
import pandas as pd
import os

class SQLDataFrameBuilder:
    def __init__(self,connection_filepath:str,query:str):
        self.query = query
        self.connection_filename = PathConverter(connection_filepath).to_wsl()
        self.query_valid_path = PathConverter(self.query).to_wsl()

    def _config(self):
        parser = ConfigParser()
        section = 'postgresql'
        db = {}

        parser.read(self.connection_filename)

        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section,self.connection_filename))
        
        return db
    
    def _connectdb(self):
        params = self._config()

        connection = p2.connect(**params)

        return connection
        
    
    def _is_file(self):
        """Returns True if self.query is a filepath, False if is not """
        return os.path.isfile(self.query_valid_path)
    
    def read_sql_file(self):
        """Reads the SQL script file and returns it as string"""
        # open the file and append the sql statements as a list
        try:
            with open(self.query_valid_path,"r",encoding="utf-8") as file:
                sql_query = file.read()
            
            # Returns a string format
            return sql_query
        except FileNotFoundError:
            raise FileNotFoundError(
                f"SQL file not found: {self.query}."
                "Please verify the file path exists."
            )
        except PermissionError:
            raise PermissionError(
                f"Permission denied to read file: {self.query}"
            )
        except Exception as e:
            raise IOError(f"Error reading SQL file: {e}")
        
    def build_dataframe(self):
        """Creates dataframe from SQL query"""
        connection = None # Avoid UnboundLocalError

        # 1. Establishing connection with PostgreSQL/Redshift database
        try:
            connection = self._connectdb()
            print("Database connection established sucessfully.")
        except OperationalError as e:
            raise OperationalError(
                f"Failed to connect to database. Check your connection settings: {e}"
            )
        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"Connection file not found: {self.connection_filename} {e}"
            )
        except Exception as e:
            raise ConnectionError(f"Unexpected error during connection: {e}")
        
        # 2. Determine query source
        try:
            if self._is_file():
                get_query = self.read_sql_file()
                print("SQL query source: file")
            else:
                get_query = self.query
                print("SQL query source: variable string")
        except Exception as e:
            raise ValueError(f"Failed to evaluate query source: {e}")
        
        # 3. Dataframe creation
        try:
            print("Creating dataframe ...")
            df_pre = pd.read_sql_query(get_query,connection)
            df = df_pre.copy(deep=True)
            print("Dataframe successfully created")
            _records = df.shape[0]
            _columns = df.shape[1]
            print(f"Result: {_records} records and {_columns} column(s) extracted")
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
        