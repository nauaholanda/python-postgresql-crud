"""create books table

Revision ID: 8f34cce381b1
Revises: 
Create Date: 2026-05-23 11:34:48.549169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f34cce381b1'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('author', sa.String, nullable=False),
        sa.Column('rating', sa.Float, default=0)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('books')
