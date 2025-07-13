from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "my_sql_db"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False,
        "USER": "root",
        "PASSWORD": "M.1029384756.m",
        "PORT": 3306,
        "DATABASE": "fast_blog",
    },
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
