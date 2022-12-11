"""add last few columns to posts table

Revision ID: 7692a8bc728a
Revises: aec39abb8920
Create Date: 2022-12-11 03:06:10.646440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7692a8bc728a'
down_revision = 'aec39abb8920'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
