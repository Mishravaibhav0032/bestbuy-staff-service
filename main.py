from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uuid

app = FastAPI()

class Staff(BaseModel):
    name: str
    position: str
    department: str
    email: str
    phone: str

db: Dict[str, Staff] = {}

@app.post("/staff")
def create_staff(staff: Staff):
    staff_id = str(uuid.uuid4())
    db[staff_id] = staff
    return {"id": staff_id, **staff.dict()}

@app.get("/staff/{staff_id}")
def read_staff(staff_id: str):
    if staff_id not in db:
        raise HTTPException(status_code=404, detail="Staff not found")
    return {"id": staff_id, **db[staff_id].dict()}

@app.put("/staff/{staff_id}")
def update_staff(staff_id: str, staff: Staff):
    if staff_id not in db:
        raise HTTPException(status_code=404, detail="Staff not found")
    db[staff_id] = staff
    return {"id": staff_id, **staff.dict()}

@app.delete("/staff/{staff_id}")
def delete_staff(staff_id: str):
    if staff_id not in db:
        raise HTTPException(status_code=404, detail="Staff not found")
    del db[staff_id]
    return {"message": "Staff deleted"}
