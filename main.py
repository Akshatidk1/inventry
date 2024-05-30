import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
import identity.web
from fastapi.templating import Jinja2Templates
from src.routers.inventory.inventory import  router as inventory_router
app = FastAPI()
__version__ = "0.8.0" 
# CORS middleware setup
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Jinja2 templates setup
templates = Jinja2Templates(directory="templates")
def get_session(request: Request):
    return request.session

# Define OAuth2 Password Bearer for token retrieval
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def read_root():
    return {"Status": "Main api Working"}

app.include_router(inventory_router, prefix="/inventory")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
