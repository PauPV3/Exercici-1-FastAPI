from fastapi import FastAPI
from pydantic import BaseModel
import consultes

app = FastAPI()

class Alumne(BaseModel):
    nom: str
    cognoms: str
    edat: int
    idAula: int


@app.get("/alumne/list")
def get_all_alumnes():
    return consultes.get_all_alumnes()

@app.get("/alumne/show/{id}")
def get_alumne(id: int):
    return consultes.get_alumne(id)

@app.post("/alumne/add")
def add_alumne(alumne: Alumne):
    return consultes.add_alumne(alumne)

@app.put("/alumne/update/{id}")
def update_alumne(id: int, alumne: Alumne):
    return consultes.update_alumne(id, alumne)

@app.delete("/alumne/delete/{id}")
def delete_alumne(id: int):
    return consultes.delete_alumne(id)

@app.get("/alumne/listAll")
def list_all_alumnes():
    return consultes.list_all_alumnes()
