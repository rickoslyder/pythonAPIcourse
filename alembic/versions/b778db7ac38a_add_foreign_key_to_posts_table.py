"""Add foreign key to posts table

Revision ID: b778db7ac38a
Revises: 97b8ad515689
Create Date: 2022-03-06 15:51:59.904470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b778db7ac38a"
down_revision = "97b8ad515689"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
