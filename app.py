from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from make import make_cuisine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 料理を作る際に送られる情報
class Info(BaseModel):
    ingredients: str
    kcal: int
    time: int

# テスト
@app.get('/')
def test():
    return {'Hello': 'World!!!!'}

# 与えられた情報から料理を作成
@app.post('/make')
def return_recipe(info: Info):
    return make_cuisine(
        info.ingredients, 
        info.kcal, 
        info.time
    )