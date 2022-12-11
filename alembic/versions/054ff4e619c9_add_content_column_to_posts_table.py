"""add content column to posts table

Revision ID: 054ff4e619c9
Revises: 4e7ddc1c967d
Create Date: 2022-12-11 02:48:01.284694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '054ff4e619c9'
down_revision = '4e7ddc1c967d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
