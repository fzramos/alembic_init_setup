from config import Config
from snowflake.sqlalchemy import URL
db_config = Config()

db_url = URL(
        account = db_config.SNOWFLAKE_ACCOUNT,
        user = db_config.SNOWFLAKE_USER,
        password = db_config.SNOWFLAKE_PASSWORD,
        database = 'ADQ',
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
def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
              return i
    return -1

def first_substring(strings, substring):
    return next((i for i, string in enumerate(strings) if substring in string), -1)

with open("alembic.ini","r+") as f:
    data = f.readlines()
    print(data)
    index_line = first_substring(data, 'sqlalchemy.url = ')
    data[index_line] = f'sqlalchemy.url = {db_url}\n'
    # data[data.index('sqlalchemy.url = ')] = f'sqlalchemy.url = {db_url}\n'
    f.seek(0)
    f.writelines(data)
