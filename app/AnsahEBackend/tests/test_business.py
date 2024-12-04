from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.db.base import Base, engine
from app.api import deps
from app import crud, schemas

client = TestClient(app)

def override_get_db():
    try:
        db = Session(autocommit=False, autoflush=False, bind=engine)
        yield db
    finally:
        db.close()

app.dependency_overrides[deps.get_db] = override_get_db

def test_create_business():
    business_data = {
        "name": "Test Business",
        "type": "E-commerce",
        "website": "https://testbusiness.com",
        "contact_email": "contact@testbusiness.com",
        "support_email": "support@testbusiness.com",
        "return_policy": "30-day return policy",
        "delivery_policy": "Free shipping on orders over $50",
        "refund_policy": "Full refund within 14 days"
    }
    response = client.post("/api/v1/businesses/", json=business_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == business_data["name"]
    assert "id" in data

def test_read_business():
    business = crud.create_business(next(override_get_db()), schemas.BusinessCreate(**{
        "name": "Test Read Business",
        "type": "Service",
        "website": "https://testreadbusiness.com",
        "contact_email": "contact@testreadbusiness.com",
        "support_email": "support@testreadbusiness.com",
        "return_policy": "No returns for services",
        "delivery_policy": "N/A",
        "refund_policy": "No refunds"
    }))
    response = client.get(f"/api/v1/businesses/{business.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == business.name
    assert data["id"] == business.id

def test_update_business():
    business = crud.create_business(next(override_get_db()), schemas.BusinessCreate(**{
        "name": "Test Update Business",
        "type": "Retail",
        "website": "https://testupdatebusiness.com",
        "contact_email": "contact@testupdatebusiness.com",
        "support_email": "support@testupdatebusiness.com",
        "return_policy": "14-day return policy",
        "delivery_policy": "Standard shipping",
        "refund_policy": "Store credit only"
    }))
    update_data = {
        "name": "Updated Test Business",
        "type": "E-commerce and Retail"
    }
    response = client.put(f"/api/v1/businesses/{business.id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["type"] == update_data["type"]

def test_delete_business():
    business = crud.create_business(next(override_get_db()), schemas.BusinessCreate(**{
        "name": "Test Delete Business",
        "type": "Wholesale",
        "website": "https://testdeletebusiness.com",
        "contact_email": "contact@testdeletebusiness.com",
        "support_email": "support@testdeletebusiness.com",
        "return_policy": "Bulk returns only",
        "delivery_policy": "Freight shipping",
        "refund_policy": "30-day money-back guarantee"
    }))
    response = client.delete(f"/api/v1/businesses/{business.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == business.id
    
    # Verify the business no longer exists
    response = client.get(f"/api/v1/businesses/{business.id}")
    assert response.status_code == 404

