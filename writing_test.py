from config import Config
from snowflake.sqlalchemy import URL
db_config = Config()

db_url = URL(
        account = db_config.SNOWFLAKE_ACCOUNT,
        user = db_config.SNOWFLAKE_USER,
        password = db_config.SNOWFLAKE_PASSWORD,
        database = 'ADQ3',
        schema = 'PUBLIC',
        warehouse = 'COMPUTE_WH',
        role='SYSADMIN'
)

with open("alembic.ini","r+") as f:
    data = f.read()
    rewrite_loc = data.index('sqlalchemy.url')
    print(rewrite_loc)
    f.seek(rewrite_loc)
    print(f.readline())
    print(f.tell())

# This works but since you can't insert, just overwrite, it deletes some comments on the lines below
# Probably just better to just rewrite the whole file
# with open("alembic.ini","r+") as f:
#     # 1218 is the loc of the line I want to rewrite
#     data = f.read()
#     f.seek(data.index('sqlalchemy.url = '))
#     f.write(f'sqlalchemy.url = {db_url}\n')

def first_substring(strings, substring):
    return next((i for i, string in enumerate(strings) if substring in string), -1)

with open("alembic.ini","r+") as f:
    data = f.readlines()
    index_line = first_substring(data, 'sqlalchemy.url = ')
    data[index_line] = f'sqlalchemy.url = {db_url}\n'
    f.seek(0)
    f.writelines(data)

with open("alembic/env.py","r+") as f:
    data = f.readlines()
    model_import = ['from models import Base\n', 'target_metadata = [Base.metadata]\n']
    sf_addition = ['from alembic.ddl.impl import DefaultImpl\n', 'class SnowflakeImpl(DefaultImpl):\n', "    __dialect__ = 'snowflake'\n"]
    index_line = first_substring(data, 'from alembic import context')
    data = data[:index_line] + model_import + sf_addition + data[index_line:]
    # data.insert(index_line + 1, 'from model import Base')
    # data.insert(index_line + 2, 'target_metadata = [Base.metadata]')

    index_line = first_substring(data, 'target_metadata = None')
    data[index_line] = '#target_metadata = None\n'
    f.seek(0)
    f.writelines(data)