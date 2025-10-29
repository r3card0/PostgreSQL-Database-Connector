# PostgreSQL Database Connector

A lightweight Python toolkit for connecting to PostgreSQL databases and executing SQL queries directly from Jupyter Notebooks. This repository provides a simple, cross-platform solution for database operations with minimal configuration.

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
git clone https://github.com/yourusername/postgres-connector.git
cd postgres-connector
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
host = localhost
port = 5432
database = mydb
user = postgres
password = mypassword
```

**Usage:**
```python
from config_parser import DBConfigParser

parser = DBConfigParser('/path/to/config.ini')
db_params = parser.get_connection_params()
# Returns: {'host': 'localhost', 'port': 5432, 'database': 'mydb', ...}
```

### 3. DatabaseConnector Class

Establishes connection to PostgreSQL database using the parameters dictionary.

```python
from db_connector import DatabaseConnector

connector = DatabaseConnector(db_params)
connection = connector.connect()
```

### 4. QueryExecutor Class

Executes SQL queries and returns results as pandas DataFrames.

```python
from query_executor import QueryExecutor

executor = QueryExecutor(connection)

# Option 1: Execute from SQL file
df = executor.execute_from_file('/path/to/query.sql')

# Option 2: Execute from string variable
sql_query = "SELECT * FROM users WHERE active = true"
df = executor.execute_from_string(sql_query)
```

## Complete Workflow Example

### In a Jupyter Notebook:

```python
# Import all classes
from path_converter import PathConverter
from config_parser import DBConfigParser
from db_connector import DatabaseConnector
from query_executor import QueryExecutor

# Step 1: Convert path if needed (optional)
converter = PathConverter()
config_path = converter.convert_path("C:\\config\\database.ini")

# Step 2: Parse connection parameters
parser = DBConfigParser(config_path)
db_params = parser.get_connection_params()

# Step 3: Connect to database
connector = DatabaseConnector(db_params)
connection = connector.connect()

# Step 4: Execute query and get DataFrame
executor = QueryExecutor(connection)

# From file
df = executor.execute_from_file('/path/to/analytics_query.sql')

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
df = executor.execute_from_string(query)

# Analyze your data
print(df.head())
df.describe()

# Don't forget to close the connection when done
connection.close()
```

## Quick Start Template

Save this template in your Jupyter Notebook:

```python
# Configuration
CONFIG_FILE = '/path/to/your/config.ini'
SQL_FILE = '/path/to/your/query.sql'  # or None if using string

# Initialize
from postgres_connector import PostgresConnector

connector = PostgresConnector(CONFIG_FILE)
df = connector.query_to_dataframe(sql_file=SQL_FILE)
# or
# df = connector.query_to_dataframe(sql_string="SELECT * FROM table")

print(f"Retrieved {len(df)} rows")
df.head()
```

## Configuration File Structure

Your `.ini` file must follow this structure:

```ini
[postgresql]
host = your_host
port = 5432
database = your_database
user = your_username
password = your_password
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
QueryExecutor → pandas.DataFrame
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
