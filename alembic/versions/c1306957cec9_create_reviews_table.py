"""create reviews table

Revision ID: c1306957cec9
Revises: 8f34cce381b1
Create Date: 2026-05-23 11:45:53.681930

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1306957cec9'
down_revision: Union[str, Sequence[str], None] = '8f34cce381b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('review_text', sa.String, nullable=False),
        sa.Column('reviewer_name', sa.String, nullable=False),
        sa.Column('book_id', sa.Integer(), nullable=False)
    )

    op.create_foreign_key(
        'fk_reviews_books',
        'reviews',
        'books',
        ['book_id'],
        ['id']
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('reviews')
