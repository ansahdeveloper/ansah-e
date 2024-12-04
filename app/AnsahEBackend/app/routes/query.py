from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Business
from ..utils.ai_model import generate_response
from pydantic import BaseModel

router = APIRouter()

class Query(BaseModel):
    business_id: int
    customer_query: str

@router.post("/query")
async def handle_query(query: Query, db: Session = Depends(get_db)):
    business = db.query(Business).filter(Business.id == query.business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    
    # Generate response using AI model
    response = generate_response(query.customer_query, business)
    
    # Here you would typically also log this query to your integrated customer support system
    # For example: log_to_zendesk(query, response, business)
    
    return {"response": response}

