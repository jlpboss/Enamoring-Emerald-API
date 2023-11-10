from typing import Optional

from pydantic import BaseModel, EmailStr

class Category_Schema(BaseModel):
    id: int
    name: str

class Category_Menu_Schema(BaseModel):
    id: int
    category_id: int
    menu_items_id: int

class Cuisine_Schema(BaseModel):
    id: int
    name: str

class Cuisine_Menu_Schema(BaseModel):
    id: int
    cuisine_id: int
    menu_items_id: int

class Menu_Item_Schema(BaseModel):
    id: int
    title: str | None
    cuisine_type: str | None
    category: str | None
    description: str | None
    price: float
    spicy_level: int

    def __init__(self, **data):
        super().__init__(**data)

    class Config:
        from_attributes = True