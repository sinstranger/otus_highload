import os


postgres_db = os.environ.get("POSTGRES_DB") #: devops_py_db
postgres_user = os.environ.get("POSTGRES_USER") #: devops_py_user
postgres_password = os.environ.get("POSTGRES_PASSWORD") #: devops_py_password
postgres_host = os.environ.get("POSTGRES_HOST") #: postgres_db


class Config:
    DATABASE_URL = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}'
