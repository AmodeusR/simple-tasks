from fastapi import FastAPI
from routes import tasks_router

app = FastAPI()
app.include_router(tasks_router)
