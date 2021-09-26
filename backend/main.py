"""Mingler App."""

import typing
import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.responses import FileResponse

from functions.mingle import generate_pairings

app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory="public/static"), name="static")
app.mount("/public", StaticFiles(directory="public"), name="public")


class Group(BaseModel):
    people: typing.List[str]


@app.get("/")
def read_index():
    return FileResponse("public/index.html")

@app.post("/")
def mingle(group: Group):
    pairings = generate_pairings(group.people)
    return pairings


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
