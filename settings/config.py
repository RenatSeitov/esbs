from envparse import Env

env = Env()


DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql://postgres:postgres@localhost:5433/postgres"
)
