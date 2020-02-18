from fastapi import FastAPI
from pydantic import BaseModel

import time
import random

app = FastAPI()

class Game(BaseModel):
    name: str
    player: str
    level: int = 1
    score: int = 0

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/game/new/{player_name}")
def game_new(player_name: str = "player1"):
    return {"game": "42", "player": player_name, "message": "Welcome %s New game started.".format(player_name)}


@app.get("/game/resume/{player_name}")
def game_resume(player_name: str):
    return {"game": "42", "player": player_name}


@app.post("/game/play")
async def game_play(game: Game):
    time.sleep(12 + (random.randrange(5,60)))
    return game