"""Added Passwords columm

Revision ID: 0f36de424c7d
Revises: 
Create Date: 2023-11-13 15:04:22.795790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f36de424c7d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('menu_items', sa.Column('password', sa.VARCHAR))


def downgrade() -> None:
    op.drop_column('menu_items', 'password')
