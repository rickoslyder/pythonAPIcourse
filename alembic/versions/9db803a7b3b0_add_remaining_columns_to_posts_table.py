"""Add remaining columns to posts table

Revision ID: 9db803a7b3b0
Revises: b778db7ac38a
Create Date: 2022-03-06 16:06:14.435286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9db803a7b3b0"
down_revision = "b778db7ac38a"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default="now()",
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
