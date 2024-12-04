from sqlalchemy.orm import Session
from app.models.business import Business
from app.schemas.business import BusinessCreate, BusinessUpdate

def get_business(db: Session, business_id: int):
    return db.query(Business).filter(Business.id == business_id).first()

def get_businesses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Business).offset(skip).limit(limit).all()

def create_business(db: Session, business: BusinessCreate):
    db_business = Business(**business.dict())
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    return db_business

def update_business(db: Session, business_id: int, business: BusinessUpdate):
    db_business = get_business(db, business_id)
    if db_business:
        update_data = business.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_business, field, value)
        db.commit()
        db.refresh(db_business)
    return db_business

def delete_business(db: Session, business_id: int):
    db_business = get_business(db, business_id)
    if db_business:
        db.delete(db_business)
        db.commit()
    return db_business

