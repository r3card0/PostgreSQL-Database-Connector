# PostgreSQL Database Connector

A lightweight Python toolkit for connecting to PostgreSQL and AWS-Redshift databases and executing SQL queries directly in notebooks or Python scripts. This repository provides a simple, cross-platform solution for database operations with minimal configuration.

## Overview

This toolkit consists of:
1. Handle cross-platform file paths (Windows/Linux)
2. Parse database connection parameters from `.ini` configuration files
3. Establish PostgreSQL and AWS Redshift databases connections
4. Execute SQL queries and return results as pandas DataFrames

## Key Features

- **Cross-platform compatibility**: Automatically converts Windows paths to Linux format
- **Configuration-based connections**: Store connection details securely in `.ini` files
- **Flexible SQL execution**: Run queries from `.sql` files or string variables
- **Jupyter Notebook ready**: Designed for seamless integration with data science workflows
- **Pandas integration**: Returns query results as DataFrames for immediate analysis

## Installation

### Prerequisites

* Python 3.10
* Access to a PostreSQL database
* Access to a AWS Redshift database

You can use this repository in two different ways:

1. Clone the repository

    Follows the steps below to clone and work directly with the source code

    Clone repository
    ```bash
    git clone https://github.com/r3card0/PostgreSQL-Database-Connector.git
    ```

2. Install as a dependency

    Alternatively, you can install this repository as a dependency within your own project:

    1. Create a Python virtual environment

        ```python
        python3 -m venv <virtual_env_name>
        ```

    2. Activate virtual environment
        
        ```python
        source <virtual_env_name>/bin/activate
        ```

    3. Install libraries and dependencies using the [requirements.txt](/requirements.txt) file.

        ```python
        pip install -r requirements.txt
        ```

        or install manually with `pip`

        ```python
        pip install git+https://github.com/r3card0/PostgreSQL-Database-Connector.git@v0.1.0
        ```

## Usage

Basic example

```python
from postgresql_database_connector import SQLDataFrameBuilder

# Inputs
# database file connection
connection_parameters = '/mnt/c/Users/user/database.ini' # or r'C:\Users\user\database.ini'

# SQL query from file
sql_query = r"C:\Users\user\employees_stats.sql"

# Or from string
sql_query2 = """
SELECT 
    customer_id,
    COUNT(*) as order_count,
    SUM(total_amount) as total_spent
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY customer_id
"""

df = SQLDataFrameBuilder(connection_parameters,sql_query).build_dataframe()

df2 = SQLDataFrameBuilder(connection_parameters,sql_query2).build_dataframe()

# Analyze your data
print(df.head())
df.describe()
```

You will see following messages:

```bash
Database connection established sucessfully.
SQL query source: variable string
Creating dataframe ...
Dataframe successfully created
Result: 5 records extracted and 1 columns
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

## Libraries and dependencies

Install libraries and dependencies into the virtual environment using the [requirements.txt](/requirements.txt) file or install manually with `pip` command

```bash
pip install psycopg2-binary pandas configparser
```

Install `path_converter` dependency as well:

```bash
pip install git+https://github.com/r3card0/WSL-path-converter.git@v0.1.0 
```

Learn more about [Path Converter](https://github.com/r3card0/WSL-path-converter/blob/main/README.md) dependency



## Error Handling

The class includes basic error handling:
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

### Version 0.1.0
- Initial release
- INI-based configuration parsing
- PostgreSQL and AWS Redshift connection management
- SQL query execution with DataFrame output

## Author
[r3card0](https://github.com/r3card0)

Project Links: https://github.com/r3card0/PostgreSQL-Database-Connector
