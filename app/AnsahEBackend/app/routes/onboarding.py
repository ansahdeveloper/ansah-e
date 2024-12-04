from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Business
from pydantic import BaseModel

router = APIRouter()

class BusinessCreate(BaseModel):
    name: str
    type: str
    website: str
    logo: str = None
    contact_email: str
    support_email: str
    phone: str = None
    return_policy: str
    delivery_policy: str
    refund_policy: str
    shipping_methods: dict = None
    payment_gateway: str = None
    custom_api_details: dict = None

@router.post("/onboard")
async def onboard_business(business: BusinessCreate, db: Session = Depends(get_db)):
    db_business = Business(**business.dict())
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    return {"message": "Business onboarded successfully", "business_id": db_business.id}

