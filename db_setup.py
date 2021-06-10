import subprocess
from config import Config
from snowflake.sqlalchemy import URL as sfURL
import sqlalchemy.engine.url as url
import os

def main():
    db_setup('snowflake')

def db_setup(db_type='snowflake'):
    db_url = create_db_url(db_type)

    # Starting Alembic
    subprocess.run('alembic init alembic'.split(), text=True, check=True)

    # Modify Alembic files with DB information
    with open("alembic.ini","r+") as f:
        data = f.readlines()
        index_line = first_substring(data, 'sqlalchemy.url = ')
        data[index_line] = f'sqlalchemy.url = {db_url}\n'
        f.seek(0)
        f.writelines(data)
    with open("alembic/env.py","r+") as f:
        data = f.readlines()
        index_line = first_substring(data, 'from alembic import context')
        model_import = ['from models import Base\n', 'target_metadata = [Base.metadata]\n']
        if db_type == 'snowflake':
            sf_addition = ['from alembic.ddl.impl import DefaultImpl\n', 'class SnowflakeImpl(DefaultImpl):\n', "    __dialect__ = 'snowflake'\n"]
            model_import += sf_addition        
        data = data[:index_line] + model_import + data[index_line:]

        index_line = first_substring(data, 'target_metadata = None')
        data[index_line] = '#target_metadata = None\n'
        f.seek(0)
        f.writelines(data)
    
    # Set-up and upload models to database
    subprocess.run(['alembic', 'revision', '--autogenerate', '-m', '“First commit”'], text=True, check=True)
    subprocess.run('alembic upgrade head'.split(), text=True, check=True)
    
def create_db_url(db_type):
    # Get DB username and passwords
    db_config = Config()

    if db_type == 'snowflake':
        db_url = sfURL(
                account = db_config.SNOWFLAKE_ACCOUNT,
                user = db_config.SNOWFLAKE_USER,
                password = db_config.SNOWFLAKE_PASSWORD,
                database = 'ADQ',
                schema = 'PUBLIC',
                warehouse = 'COMPUTE_WH',
                role='SYSADMIN'
        )
    if db_type == 'sqlite':
        db_url = url.make_url(f'sqlite:///{os.path.abspath(os.getcwd())}\ADQ.db')
    return db_url

def first_substring(strings, substring):
    return next((i for i, string in enumerate(strings) if substring in string), -1)

if __name__ == '__main__':
    main()