"""create phone number for user column

Revision ID: 7848e0bad24b
Revises: 
Create Date: 2025-05-19 20:41:30.777095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7848e0bad24b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('user', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
