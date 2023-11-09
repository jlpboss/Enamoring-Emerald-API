from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import crud
from database import SessionLocal

router = APIRouter(
    prefix="/menu-items"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[schemas.Menu_Item_Schema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_menu_items(db)
    return items