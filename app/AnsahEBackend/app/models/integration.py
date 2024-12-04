from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.base import Base

class Integration(Base):
    __tablename__ = "integrations"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("businesses.id"))
    type = Column(String)
    provider = Column(String)
    api_key = Column(String)
    is_active = Column(Boolean, default=True)

