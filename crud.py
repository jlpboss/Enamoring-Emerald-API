from sqlalchemy.orm import Session, aliased, joinedload
from models import *
from schemas import *
from sqlalchemy import and_, or_

def get_menu_items(db: Session):
    query = (
        db.query(Menu_Item)
        .options(
            joinedload(Menu_Item.cuisine_menu).joinedload(Cuisine_Menu.cuisine),
            joinedload(Menu_Item.category_menu).joinedload(Category_Menu.category),
        )
        .all()
    )

    items = {}
    for item in query:
        item_id = item.id
        menu_item_schema = Menu_Item_Schema(
            id=item.id,
            title=item.title,
            cuisine_type=item.cuisine_menu.cuisine.name if item.cuisine_menu else None,
            category=item.category_menu.category.name if item.category_menu else None,
            description=item.description,
            price=float(item.price),
            spicy_level=item.spicy_level,
        )
        items[item_id] = menu_item_schema

    out = list(items.values())

    return out