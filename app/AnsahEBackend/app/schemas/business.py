from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, Dict

class BusinessBase(BaseModel):
    name: str
    type: str
    website: HttpUrl
    contact_email: EmailStr
    support_email: EmailStr
    return_policy: str
    delivery_policy: str
    refund_policy: str

class BusinessCreate(BusinessBase):
    logo: Optional[str] = None
    phone: Optional[str] = None
    shipping_methods: Optional[Dict] = None
    payment_gateway: Optional[str] = None
    custom_api_details: Optional[Dict] = None

class BusinessUpdate(BusinessBase):
    pass

class BusinessInDBBase(BusinessBase):
    id: int

    class Config:
        orm_mode = True

class Business(BusinessInDBBase):
    pass

class BusinessInDB(BusinessInDBBase):
    pass

