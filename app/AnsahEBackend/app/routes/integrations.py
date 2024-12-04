from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Integration
from pydantic import BaseModel

router = APIRouter()

class IntegrationCreate(BaseModel):
    business_id: int
    type: str
    provider: str
    api_key: str

@router.post("/integrations")
async def add_integration(integration: IntegrationCreate, db: Session = Depends(get_db)):
    db_integration = Integration(**integration.dict())
    db.add(db_integration)
    db.commit()
    db.refresh(db_integration)
    return {"message": "Integration added successfully", "integration_id": db_integration.id}

