from sqlalchemy.orm import Session
from fastapi import HTTPException

from db import model, schema
from core.utils import current_sysdate, current_systime

def create_customer(customer: schema.CustomerCreate, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.phone_number == customer.phone_number)
        .first()
    )
    if db_customer:
        raise HTTPException(
            status_code=409,
            detail="Phone number exists"
        )
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.email == customer.email)
        .first()
    )
    if db_customer:
        raise HTTPException(
            status_code=409,
            detail="Email exists"
        )
    
    db_customer = model.Customer(
        first_name = customer.first_name,
        last_name = customer.last_name,
        birth_date = customer.birth_date,
        address = customer.address,
        phone_number = customer.phone_number,
        email = customer.email,
        job_title = customer.job_title,
        updated_datetime = current_systime()
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def select_all_customer(db: Session):
    return db.query(model.Customer).all()

def select_customer_by_id(customer_id: int, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.customer_id == customer_id)
        .first()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return db_customer

def select_customer_by_first_name(first_name: str, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.first_name == first_name)
        .all()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return db_customer

def select_customer_by_phone_number(phone_number: str, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.phone_number == phone_number)
        .first()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return db_customer

def select_customer_by_email(email: str, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.email == email)
        .first()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return db_customer

def update_customer(customer_id: int, customer: schema.CustomerUpdate, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.phone_number == customer.phone_number)
        .first()
    )
    if db_customer:
        raise HTTPException(
            status_code=409,
            detail="Phone number exists"
        )
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.email == customer.email)
        .first()
    )
    if db_customer:
        raise HTTPException(
            status_code=409,
            detail="Email exists"
        )
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.customer_id == customer_id)
        .first()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    update_data = customer.dict()
    for key, value in update_data.items():
        if value is not None:
            setattr(db_customer, key, value)
    setattr(db_customer, 'updated_datetime', current_systime())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_customer(customer_id: int, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.customer_id == customer_id)
        .first()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    db.delete(db_customer)
    db.commit()
    return db_customer