from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

DATABASE_URL = "mysql+aiomysql://root:M.1029384756.m@my_sql_db:3306/fast_blog"

engine = create_async_engine(
    DATABASE_URL,
)
SessionLocal = async_sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
