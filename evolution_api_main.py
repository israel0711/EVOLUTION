from fastapi import FastAPI, HTTPException
from evolution_api.models import EvolutionData
from evolution_api.schemas import EvolutionDataCreate, EvolutionDataUpdate
from evolution_api.database import db, get_next_id

app = FastAPI(title="Evolution API")

@app.get("/evolutions", response_model=list[EvolutionData])
def list_evolutions():
    return list(db.values())

@app.get("/evolutions/{evolution_id}", response_model=EvolutionData)
def get_evolution(evolution_id: int):
    evolution = db.get(evolution_id)
    if not evolution:
        raise HTTPException(status_code=404, detail="Evolution not found")
    return evolution

@app.post("/evolutions", response_model=EvolutionData, status_code=201)
def create_evolution(data: EvolutionDataCreate):
    new_id = get_next_id()
    evolution = EvolutionData(id=new_id, **data.dict())
    db[new_id] = evolution
    return evolution

@app.put("/evolutions/{evolution_id}", response_model=EvolutionData)
def update_evolution(evolution_id: int, data: EvolutionDataUpdate):
    evolution = db.get(evolution_id)
    if not evolution:
        raise HTTPException(status_code=404, detail="Evolution not found")
    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(evolution, key, value)
    db[evolution_id] = evolution
    return evolution

@app.delete("/evolutions/{evolution_id}", status_code=204)
def delete_evolution(evolution_id: int):
    if evolution_id not in db:
        raise HTTPException(status_code=404, detail="Evolution not found")
    del db[evolution_id]