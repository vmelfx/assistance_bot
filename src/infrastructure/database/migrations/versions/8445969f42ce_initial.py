"""initial

Revision ID: 8445969f42ce
Revises:
Create Date: 2023-07-17 15:50:08.526144+03:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8445969f42ce"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table("user", sa.Column("chat_id", sa.Integer(), nullable=False), sa.PrimaryKeyConstraint("chat_id"))
    op.create_table(
        "todoes",
        sa.Column("task_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("priority", sa.Integer(), nullable=True),
        sa.Column("complete", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.chat_id"],
        ),
        sa.PrimaryKeyConstraint("task_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("todoes")
    op.drop_table("user")
    # ### end Alembic commands ###