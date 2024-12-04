from sqlalchemy import Column, Integer, String, Text, JSON
from app.db.base import Base

class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    website = Column(String)
    logo = Column(String, nullable=True)
    contact_email = Column(String)
    support_email = Column(String)
    phone = Column(String, nullable=True)
    return_policy = Column(Text)
    delivery_policy = Column(Text)
    refund_policy = Column(Text)
    shipping_methods = Column(JSON, nullable=True)
    payment_gateway = Column(String, nullable=True)
    custom_api_details = Column(JSON, nullable=True)

