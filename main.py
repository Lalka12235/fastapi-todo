from fastapi import FastAPI
from handler.router import  router

app = FastAPI()

#router init
app.include_router(router)