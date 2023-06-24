import os

from dotenv import load_dotenv  # noqa: F401

SECRET_KEY = "alura"

SQLALCHEMY_DATABASE_URI = "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
    SGBD="mysql+mysqlconnector",
    usuario=os.getenv("USER_DB"),
    senha=os.getenv("PWD_DB"),
    servidor=os.getenv("HOST"),
    database="jogoteca",
)
