from contextlib import asynccontextmanager

import uvicorn
from Db.engine import Base, engine
from fastapi import FastAPI
from Routers.users import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(user_router, prefix="/api/account")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
