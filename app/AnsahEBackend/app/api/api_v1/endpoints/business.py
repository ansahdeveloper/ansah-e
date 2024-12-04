from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Business)
def create_business(
    business: schemas.BusinessCreate,
    db: Session = Depends(deps.get_db)
):
    return crud.create_business(db=db, business=business)

@router.get("/", response_model=List[schemas.Business])
def read_businesses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db)
):
    businesses = crud.get_businesses(db, skip=skip, limit=limit)
    return businesses

@router.get("/{business_id}", response_model=schemas.Business)
def read_business(
    business_id: int,
    db: Session = Depends(deps.get_db)
):
    db_business = crud.get_business(db, business_id=business_id)
    if db_business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return db_business

@router.put("/{business_id}", response_model=schemas.Business)
def update_business(
    business_id: int,
    business: schemas.BusinessUpdate,
    db: Session = Depends(deps.get_db)
):
    db_business = crud.update_business(db, business_id=business_id, business=business)
    if db_business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return db_business

@router.delete("/{business_id}", response_model=schemas.Business)
def delete_business(
    business_id: int,
    db: Session = Depends(deps.get_db)
):
    db_business = crud.delete_business(db, business_id=business_id)
    if db_business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return db_business

