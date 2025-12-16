# 🔌PostgreSQL Database Connector

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-fbec5d?style=for-the-badge&logo=pandas&logoColor=blue) 
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Redshift](https://img.shields.io/badge/AWS%20Redshift-232F3E?style=for-the-badge&logo=amazonredshift&logoColor=white)

A lightweight Python toolkit for connecting to PostgreSQL and AWS-Redshift databases and executing SQL queries directly in notebooks or Python scripts. This repository provides a simple, cross-platform solution for database operations with minimal configuration.

## 🧭 Overview

This toolkit consists of:
1. Handle cross-platform file paths (Windows/Linux)
2. Parse database connection parameters from `.ini` configuration files
3. Establish PostgreSQL and AWS Redshift databases connections
4. Execute SQL queries and return results as pandas DataFrames

## 🛠️ Key Features

- **Cross-platform compatibility**: Automatically converts Windows paths to Linux format
- **Configuration-based connections**: Store connection details securely in `.ini` files
- **Flexible SQL execution**: Run queries from `.sql` files or string variables
- **Jupyter Notebook ready**: Designed for seamless integration with data science workflows
- **Pandas integration**: Returns query results as DataFrames for immediate analysis

## ⚙️ Installation

### Prerequisites

* Python 3.10 or higher
* Access to a PostreSQL database
* Access to a AWS Redshift database
* File `.ini` with connection parameters

You can use this repository in two different ways:

### 1. Clone the repository

    Follows the steps below to clone and work directly with the source code

    Clone repository
    ```bash
    git clone https://github.com/r3card0/PostgreSQL-Database-Connector.git
    ```

### 2. Create a Python Virtual Environment

> ⚠️ Make sure you are using a WSL (Window Subsystem for Linux) terminal to run the package installation commands.

In a WSL terminal, run the following process

1. Create a virtual environment. Select the virtual environment's name; e.g. *venv_process* 

    ```bash
    python3 -m venv venv_process
    ```

2. Activate the virtual environment:

    ```bash
    source venv_process/bin/activate
    ```

### 3. 📦 Install PostgreSQL Database Connector Dependency

Once the virtual environment is installed and activated, install PostgreSQL Database Connector dependency by executing the following command:

```
pip install git+https://github.com/r3card0/PostgreSQL-Database-Connector.git@v0.1.0
```
        ```

## ⚡ Class Methods

|Class Method|Objective|Parameter(s)|Result(s)|
|-|-|-|-|
|`read_sql_file()`|Reads the SQL script comming from a file or from a variable and returns it as string| SQL script from a file or from a varible|Return a string. `str` : `SELECT * FROM employees;`|
|`build_dataframe()`|Creates dataframe from SQL query. Make connection with PostgreSQL or AWS-Redshift database|SQL query| Dataframe of pandas|

## Versions

|Version|Description|
|-|-|
|**v0.1.0**|Initial version|

- Initial release
- INI-based configuration parsing
- PostgreSQL and AWS Redshift connection management
- SQL query execution with DataFrame output

## 🚗 Usage

**Basic Example**

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
Result: 5 records and 1 column(s) extracted
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

This solution uses Path Converter dependency which helps to convert Windows path to WSL path. Learn more about [Path Converter](https://github.com/r3card0/WSL-path-converter/blob/main/README.md) dependency



## Error Handling

The class includes basic error handling:
- Invalid file paths will raise `FileNotFoundError`
- Connection failures will raise `psycopg2.OperationalError`
- Invalid SQL syntax will raise `psycopg2.ProgrammingError`


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📃License

This project is licensed under the MIT License

## 🚀 Project Motivation

* This project was created as a practical solution to avoid reprocessing during data preparation
* Build a reusable foundation that connects SQL and pandas in a clear and maintainable way
* Make life easier by automating repetitive data extraction tasks, allowing greater focus on interpretation
* Support both quick analyses and larger projects

## 🔗 References
**psycopg**

* [psycopg.org - documentation](https://www.psycopg.org/docs/)

**configparser**
* [Python.org - configparser](https://docs.python.org/3/library/configparser.html)

**Pandas**

* [Pandas - DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)
* [Pandas - read_sql_query](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)

**pyproject.toml file**

* [SetUpTools - Configuring setuptools using pyproject.toml files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
* [SetUpTools - Package Discovery](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html)
* [Python Packaging User Guide - Writting your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
* [Python Packaging User Guide - src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
* [Rogger van der Geer - An Updated Guide to Setuptools and Pyproject.toml](https://xebia.com/blog/an-updated-guide-to-setuptools-and-pyproject-toml/)

# 👤 Author

* GitHub: [r3card0](https://github.com/r3card0)
* LinkedIn: [Ricardo](https://www.linkedin.com/in/ricardordzsaldivar/)
