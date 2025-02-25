from fastapi import FastAPI
from handler.router import  router
from handler.auth import auth

app = FastAPI()

#router init
app.include_router(router)
app.include_router(auth)