import subprocess
# alembic revision --autogenerate -m “First commit”
# alembic upgrade head
subprocess.run(['alembic', 'revision', '--autogenerate', '-m', '“First commit”'], capture_output=True, text=True, check=True)
subprocess.run('alembic upgrade head'.split(), capture_output=True, text=True, check=True)
