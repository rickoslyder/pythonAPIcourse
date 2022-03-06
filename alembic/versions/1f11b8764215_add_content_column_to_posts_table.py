"""add content column to posts table

Revision ID: 1f11b8764215
Revises: 53a7055b94d7
Create Date: 2022-03-06 14:57:02.143021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1f11b8764215"
down_revision = "53a7055b94d7"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
