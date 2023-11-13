"""Added account table

Revision ID: 30a6a91f201e
Revises: 6380857691b4
Create Date: 2023-11-13 15:48:16.377447

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30a6a91f201e'
down_revision: Union[str, None] = '6380857691b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_id', table_name='user')
    op.drop_table('user')
    op.alter_column('category', 'name',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.drop_constraint('category_name_key', 'category', type_='unique')
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    op.create_index(op.f('ix_category_menu_id'), 'category_menu', ['id'], unique=False)
    op.alter_column('cuisine', 'name',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.drop_constraint('cuisine_name_key', 'cuisine', type_='unique')
    op.create_index(op.f('ix_cuisine_id'), 'cuisine', ['id'], unique=False)
    op.create_index(op.f('ix_cuisine_menu_id'), 'cuisine_menu', ['id'], unique=False)
    op.alter_column('menu_items', 'title',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.alter_column('menu_items', 'description',
               existing_type=sa.VARCHAR(length=2048),
               nullable=True)
    op.alter_column('menu_items', 'price',
               existing_type=sa.NUMERIC(precision=12, scale=2),
               nullable=True)
    op.alter_column('menu_items', 'spicy_level',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('menu_items_title_key', 'menu_items', type_='unique')
    op.create_index(op.f('ix_menu_items_id'), 'menu_items', ['id'], unique=False)
    op.drop_column('menu_items', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu_items', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_menu_items_id'), table_name='menu_items')
    op.create_unique_constraint('menu_items_title_key', 'menu_items', ['title'])
    op.alter_column('menu_items', 'spicy_level',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('menu_items', 'price',
               existing_type=sa.NUMERIC(precision=12, scale=2),
               nullable=False)
    op.alter_column('menu_items', 'description',
               existing_type=sa.VARCHAR(length=2048),
               nullable=False)
    op.alter_column('menu_items', 'title',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.drop_index(op.f('ix_cuisine_menu_id'), table_name='cuisine_menu')
    op.drop_index(op.f('ix_cuisine_id'), table_name='cuisine')
    op.create_unique_constraint('cuisine_name_key', 'cuisine', ['name'])
    op.alter_column('cuisine', 'name',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.drop_index(op.f('ix_category_menu_id'), table_name='category_menu')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.create_unique_constraint('category_name_key', 'category', ['name'])
    op.alter_column('category', 'name',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_index('ix_user_id', 'user', ['id'], unique=False)
    # ### end Alembic commands ###
