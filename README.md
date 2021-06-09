# Initializing and prepping Alembic for DB upload programatically
### This program that will run Command Line commands and write to files so Alembic will connect to and do first commit of a set of database models

- Purpose: I am making a large program that needs to run on several types of RDBMS. This program will allow users to run 1 program to set up Alembic on whatever RDBMS they would like and set up the tables needed to run the larger program. All they will have to do is pip install the requirements.txt file, add and .env file with their desired DB credentials, and run one python file.