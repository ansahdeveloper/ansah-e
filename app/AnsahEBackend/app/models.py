from sqlalchemy import Column, Integer, String, Text, Boolean, JSON
from .database import Base

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

class Integration(Base):
    __tablename__ = "integrations"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, index=True)
    type = Column(String)  # e.g., "shipping", "payment", "support"
    provider = Column(String)
    api_key = Column(String)
    is_active = Column(Boolean, default=True)

