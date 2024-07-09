import os

import pyfiglet

import pandas as pd
from sqlalchemy import create_engine, Engine, inspect

import resources
import dotenv


# load environment variables
dotenv.load_dotenv()

# print banner
f = pyfiglet.figlet_format("Logistic", font="slant")
print(f)


def create_db_engine() -> Engine | None:
    db_user = os.environ.get("DATABASE_USERNAME")
    db_password = os.environ.get("DATABASE_PASSWORD")
    db_host = os.environ.get("DATABASE_HOST")
    db_port = os.environ.get("DATABASE_PORT")
    db_name = os.environ.get("DATABASE_NAME")
    if not db_host or not db_port or not db_name or not db_user or not db_password:
        return None
    url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    return create_engine(
        url,
        echo=True,
        future=True,
    )


def import_db_tables():
    engine: Engine | None = create_db_engine()
    if not engine:
        return None
    dfs = {}
    for name in ["logistics_shipments"]:
        dfs[name] = pd.read_sql_table(name, engine)
    return dfs


def init_db():
    dfs = import_db_tables()
    if not dfs:
        return
    resources.dfs = dfs


print("Init DB")
init_db()
