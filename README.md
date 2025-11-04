# PostgreSQL Database Connector

A lightweight Python toolkit for connecting to PostgreSQL and AWS-Redshift databases and executing SQL queries directly from Jupyter Notebooks. This repository provides a simple, cross-platform solution for database operations with minimal configuration.

## Overview

This toolkit consists of four Python classes that work together to:
1. Handle cross-platform file paths (Windows/Linux)
2. Parse database connection parameters from `.ini` configuration files
3. Establish PostgreSQL database connections
4. Execute SQL queries and return results as pandas DataFrames

## Features

- **Cross-platform compatibility**: Automatically converts Windows paths to Linux format
- **Configuration-based connections**: Store connection details securely in `.ini` files
- **Flexible SQL execution**: Run queries from `.sql` files or string variables
- **Jupyter Notebook ready**: Designed for seamless integration with data science workflows
- **Pandas integration**: Returns query results as DataFrames for immediate analysis

## Installation

### Prerequisites

```bash
pip install psycopg2-binary pandas configparser
```

### Clone the Repository

```bash
git clone https://github.com/r3card0/PostgreSQL-Database-Connector.git
```

## Usage

### 1. PathConverter Class

Converts file paths to Linux format, handling both Windows and Linux path separators.

```python
from path_converter import PathConverter

converter = PathConverter()
linux_path = converter.convert_path("C:\\Users\\Documents\\config.ini")
# Returns: /C/Users/Documents/config.ini
```

### 2. ConfigParser Class

Reads database connection parameters from an `.ini` configuration file.

**Example config.ini file:**
```ini
[postgresql]
user = postgres
password = mypassword
host = localhost
port = 5432
database = mydb
```

**Usage:**
```python
from config_parser import PostgreSQLConfigReader

parser = PostgreSQLConfigReader('/path/to/config.ini')
db_params = parser.config()
# Returns: {'host': 'localhost', 'port': 5432, 'database': 'mydb', ...}
```

### 3. DatabaseConnector Class

Establishes connection to PostgreSQL database using the parameters dictionary.

```python
from db_connector import DatabaseConnector

connector = DatabaseConnector(db_params)
connection = connector.connectdb()
```

### 4. QueryExecutor Class

Executes SQL queries and returns results as pandas DataFrames.

```python
from create_df_query import CreateDataframe

executor = CreateDataframe(query,connection)
df = executor.get_dataframe()

# Option 1: Execute from SQL file
executor = CreateDataframe('/path/to/query.sql',connection)
df = executor.get_dataframe()

# Option 2: Execute from string variable
sql_query = "SELECT * FROM users WHERE active = true"
executor = CreateDataframe(sql_query,connection)
df = executor.get_dataframe()
```

## Complete Workflow Example

### In a Jupyter Notebook:

```python
# Import 
import sys
from pathlib import Path

# Add the parent folder of Python to the path
parent_folder = Path.cwd().parent  # Move up one directory from notebooks/
sys.path.insert(0, str(parent_folder))

from utils.create_df_query import CreateDataframe

# Inputs
# database file connection
db_connection = r"c:\Users\friday\setup\database.ini"
# SQL query from file
employees_query = r"c:\Users\friday\sql\employees_stats.sql"

# Run Process From file
df = CreateDataframe(employees_query,db_connection).get_dataframe()

# Or from string
query = """
SELECT 
    customer_id,
    COUNT(*) as order_count,
    SUM(total_amount) as total_spent
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY customer_id
"""
df = CreateDataframe(query,db_connection).get_dataframe()

# Analyze your data
print(df.head())
df.describe()
```

You will see following messages:

```bash
Database connection established sucessfully.
The SQL query source is a variable
Creating the dataframe
Dataframe successfully created.
Database closed successfully.
```

The process closes database connection automatically.



## Configuration File Structure

Your `.ini` file must follow this structure:

```ini
[postgresql]
user = your_username
password = your_password
host = your_corporate_host
port = 5432
database = your_database
```

**Security Note**: Never commit `.ini` files containing credentials to version control. Add them to your `.gitignore`.

## Class Architecture

```
PathConverter
    ↓
ConfigParser → dict(connection_params)
    ↓
DatabaseConnector → connection
    ↓
CreateDataframe → pandas.DataFrame
```

## Error Handling

All classes include basic error handling:
- Invalid file paths will raise `FileNotFoundError`
- Connection failures will raise `psycopg2.OperationalError`
- Invalid SQL syntax will raise `psycopg2.ProgrammingError`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues or questions, please open an issue on GitHub.

## Changelog

### Version 1.0.0
- Initial release
- Cross-platform path conversion
- INI-based configuration parsing
- PostgreSQL connection management
- SQL query execution with DataFrame output
