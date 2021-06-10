import subprocess

# subprocess.run("conda env list", shell=True)

# subprocess.run('bash -c "conda activate crypto; python -V"', shell=True)

# subprocess.call(['conda', "activate", 'adq'])
# URL(
#         account = db_config.SNOWFLAKE_ACCOUNT,
#         user = db_config.SNOWFLAKE_USER,
#         password = db_config.SNOWFLAKE_PASSWORD,
#         database = 'ADQ',
#         schema = 'PUBLIC',
#         warehouse = 'COMPUTE_WH',
#         role='SYSADMIN'
# )

a= subprocess.run('alembic init alembic'.split(), capture_output=True, text=True, check=True)
# subprocess.run('alembic init alembic', shell=True)

# b= subprocess.run(f'alembic init alembic'.split(), capture_output=True, text=True, check=True)

# subprocess.run('bash -c "conda activate base; python -V"', shell=True)

