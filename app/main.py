from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/game/new/{player_name}")
def game_new(player_name: str = "player1"):
    return {"game": "42", "player": player_name, "message" : "New game started"}
