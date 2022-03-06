"""create posts table

Revision ID: 53a7055b94d7
Revises: 
Create Date: 2022-03-06 14:22:31.082605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "53a7055b94d7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
