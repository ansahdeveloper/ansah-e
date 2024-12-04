from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Business
from pydantic import BaseModel

router = APIRouter()

class PolicyUpdate(BaseModel):
    return_policy: str = None
    delivery_policy: str = None
    refund_policy: str = None

@router.put("/policies/{business_id}")
async def update_policies(business_id: int, policies: PolicyUpdate, db: Session = Depends(get_db)):
    business = db.query(Business).filter(Business.id == business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    
    for field, value in policies.dict(exclude_unset=True).items():
        setattr(business, field, value)
    
    db.commit()
    return {"message": "Policies updated successfully"}

@router.get("/policies/{business_id}")
async def get_policies(business_id: int, db: Session = Depends(get_db)):
    business = db.query(Business).filter(Business.id == business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    
    return {
        "return_policy": business.return_policy,
        "delivery_policy": business.delivery_policy,
        "refund_policy": business.refund_policy
    }

