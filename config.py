import os


postgres_db = os.environ.get("POSTGRES_DB")
postgres_user = os.environ.get("POSTGRES_USER")
postgres_password = os.environ.get("POSTGRES_PASSWORD")
postgres_host = os.environ.get("POSTGRES_HOST")


class Config:
    DATABASE_URL = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}'
