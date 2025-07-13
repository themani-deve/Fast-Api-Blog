import uvicorn
from fastapi import FastAPI
from Routers.users import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/api/account")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
