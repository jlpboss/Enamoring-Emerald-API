"""Added test tabel

Revision ID: 6380857691b4
Revises: 0f36de424c7d
Create Date: 2023-11-13 15:15:42.136505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6380857691b4'
down_revision: Union[str, None] = '0f36de424c7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('password', sa.String(200)),
    )


def downgrade() -> None:
    op.drop_table('user')
