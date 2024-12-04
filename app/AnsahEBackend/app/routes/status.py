from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Business
from ..utils.integrations import get_order_status
from pydantic import BaseModel

router = APIRouter()

class StatusRequest(BaseModel):
    business_id: int
    order_id: str

@router.post("/status")
async def check_status(request: StatusRequest, db: Session = Depends(get_db)):
    business = db.query(Business).filter(Business.id == request.business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    
    status = get_order_status(business, request.order_id)
    return {"status": status}

