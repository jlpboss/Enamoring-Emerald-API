from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric

class Base (DeclarativeBase):
    pass

class Menu_Item(Base):
    __tablename__ = "menu_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Column(String)
    description: Mapped[str] = Column(String)
    price: Mapped[float] = Column(Numeric(precision=12, scale=2, asdecimal=False))
    spicy_level: Mapped[int] = Column(Integer)

    cuisine_menu: Mapped["Cuisine_Menu"] = relationship(back_populates="menu_item", cascade="all, delete-orphan")
    category_menu: Mapped["Category_Menu"] = relationship(back_populates="menu_item", cascade="all, delete-orphan")

class Cuisine(Base):
    __tablename__ = "cuisine"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String)

    cuisine_menu: Mapped["Cuisine_Menu"] = relationship(back_populates="cuisine")

class Cuisine_Menu(Base):
    __tablename__ = "cuisine_menu"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    cuisine_id: Mapped[int] = mapped_column(ForeignKey("cuisine.id"))
    menu_item_id: Mapped[int] = mapped_column(ForeignKey("cuisine_menu.id"))

    menu_item: Mapped["Menu_Item"] = relationship(back_populates="cuisine_menu")
    cuisine: Mapped["Cuisine"] = relationship(back_populates="cuisine_menu")

class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String)

    category_menu: Mapped["Category_Menu"] = relationship(back_populates="category")

class Category_Menu(Base):
    __tablename__ = "category_menu"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    menu_item_id: Mapped[int] = mapped_column(ForeignKey("category_menu.id"))

    menu_item: Mapped["Menu_Item"] = relationship(back_populates="category_menu")
    category: Mapped["Category"] = relationship(back_populates="category_menu")