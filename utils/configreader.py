from configparser import ConfigParser
from .modify_file_path import PathConverter

class PostgreSQLConfigReader:
    def __init__(self,filepath:str) -> None:
        self.parser = ConfigParser()
        self.section = 'postgresql'
        self.filename = PathConverter(filepath).convert_path()
        self.db = {}

    def config(self):        
        self.parser.read(self.filename)

        if self.parser.has_section(self.section):
            self.params = self.parser.items(self.section)
            for param in self.params:
                self.db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(self.section,self.filename))
        
        return self.db