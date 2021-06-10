# Initializing and prepping Alembic for DB upload programatically
### This program that will run Command Line commands and write to files so Alembic will connect to and do first commit of a set of database models

- Purpose: I am making a large program that needs to run on several types of RDBMS. This program will allow users to run 1 program to set up Alembic on whatever RDBMS they would like and set up the tables needed to run the larger program. All they will have to do is pip install the requirements.txt file, add and .env file with their desired DB credentials, and run one python file.

# Setup:
1. In command line, paste and run the command
```shell
pip install -r requirements.txt
```
2. Add a .env file to the project root with this format and your DB credentials:
```
SNOWFLAKE_ACCOUNT=xxxxx
SNOWFLAKE_USER=xxxxx
SNOWFLAKE_PASSWORD=xxxx
```
3. In your RDBMS of choice, create an empty database called ADQ
    - for a Snowflake set-up
        * See sql_commands.sql for necessary SQL commands
    - for SQLite3 set-up
        * Simply add an ADQ.db file to the project root
3. In db_setup.py, change the line 6 argument to one of
    - 'snowflake'
    - 'postgres'
    - 'sqlite'
4. Run db_setup.py