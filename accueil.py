import uvicorn
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator, field_validator, Field

from typing import Optional
app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Greeting(BaseModel):
    name: str = Field(...)

    @field_validator('name')  # Notez l'utilisation de field_validator
    @classmethod     # Notez l'utilisation de field_validator

    def name_in_list(cls, v):
        # Convertir le nom en minuscules
        v = v.lower()
        allowed_names = ['gilles', 'marion', 'bonnie', 'polo']  # Liste de noms autorisés
        if v not in allowed_names:
            raise ValueError('Le nom doit être dans la liste autorisée')
        # Convertir la première lettre en majuscule pour le retour
        v = v.capitalize()
        return v

@app.get("/")
async def root():
    return {"message": "Veuillez saisir votre nom"}

@app.post("/greeting/")
async def greeting(greeting: Greeting):
    return {"message": f"Bonjour {greeting.name}"}

if __name__=="__main__":
    uvicorn.run("accueil:app", host="127.0.0.1", port=8000, log_level="info")


