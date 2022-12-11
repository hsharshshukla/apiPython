"""create posts table

Revision ID: 4e7ddc1c967d
Revises: 
Create Date: 2022-12-11 02:35:08.279311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e7ddc1c967d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",sa.Column("id",sa.Integer(),nullable =False,primary_key=True),
    sa.Column("title",sa.String(),nullable=False))
    pass



def downgrade() -> None:
    op.drop_table("posts")
    pass
